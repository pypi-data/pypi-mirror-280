import json
import logging
import sys
from typing import Any, Generator

from tqdm import tqdm

from .json_schema import InvalidMode, JsonSchemaBuilder
from .process import process_line
from .run import Run, RunStatus

logger = logging.getLogger(__name__)


def convert_output_to_str(output: Any) -> str:
    if isinstance(output, dict):
        logger.info("Output is a dict")
        return json.dumps(output)
    elif isinstance(output, list):
        logger.info("Output is a list")
        return json.dumps(output)
    else:
        logger.info("Output is a string")
        return str(output)


def print_data_output(output: str | dict | list):
    string_output = convert_output_to_str(output)
    print(string_output, file=sys.stdout, flush=True)


def print_info(info: str, *args, **kwargs):
    """
    Print info to stderr, to avoid interfering with the output.
    """
    print(info, *args, **kwargs, file=sys.stderr)


def write_to_file(output: str | dict | list, file_path: str):
    with open(file_path, "a") as f:
        f.write(json.dumps(output))
        f.write("\n")


class Runner:
    llm = None
    sandbox = None
    store = None
    quiet = False
    progress = False
    output_file = None
    json_schema_builder = None
    invalid_mode: InvalidMode

    def __init__(
        self,
        llm,
        sandbox,
        store,
        quiet=False,
        progress=False,
        output_file=None,
        input_schema=None,
        invalid_mode: InvalidMode = InvalidMode.abort,
    ):
        self.llm = llm
        self.sandbox = sandbox
        self.store = store
        self.quiet = quiet
        self.progress = progress
        self.output_file = output_file
        self.json_schema_builder = (
            JsonSchemaBuilder().init_from_schema(input_schema) if input_schema else None
        )
        self.invalid_mode = invalid_mode

    def terminate(self):
        if self.sandbox:
            self.sandbox.close()

    def process(
        self,
        lines: Generator[Any, None, None],
        run: Run,
        return_outputs=False,
    ) -> Run:
        logger.info("Process data")
        run.start()
        shaper = run.shaper

        if self.output_file is not None:
            print_info(f"Writing to file: {self.output_file}")

        output = None

        activate_progress_bar = (
            self.progress is True
            and self.quiet is False
            and sys.stdout.isatty() is True
        )

        if activate_progress_bar:
            line_bar = tqdm(leave=True, position=0, file=sys.stderr)
        else:
            line_bar = None

        if return_outputs:
            run.outputs = []

        final_status = None

        for idx, line in enumerate(lines):
            logger.info("Processing line: %s", idx)

            if line_bar is not None:
                line_bar.update(1)
                line_bar.refresh()

            # Initialize the schema builder with the frist seen data
            if self.json_schema_builder is None:
                self.json_schema_builder = JsonSchemaBuilder().init_from_data(line)

            if shaper.input_schema is None:
                # If no schmea, create a new one
                logger.info("Creating schema on the first line of data")
                shaper.input_schema = self.json_schema_builder.schema
                logger.info(f"Schema: {shaper.input_schema}")
            else:
                # Check if the line is valid against the schema
                valid, error = self.json_schema_builder.validate(line)
                if not valid and self.invalid_mode == InvalidMode.abort:
                    logger.error(
                        f"Line: {idx+1} is not valid against the schema: {error}\n\nAborting processing"
                    )
                    run.end(status=RunStatus.FAILED)
                    return run
                elif not valid and self.invalid_mode == InvalidMode.ignore:
                    logger.info(
                        f"Line: {idx+1} is not valid against the schema: {error}\n\nIgnoring error"
                    )
                    pass
                elif not valid and self.invalid_mode == InvalidMode.skip:
                    logger.info(
                        f"Line: {idx+1} is not valid against the schema: {error}\n\nSkipping line"
                    )
                    continue
                else:
                    logger.info(f"Line: {idx+1} is valid against the schema")

            for ri in range(shaper.repeat):
                logger.info("Repeat Iteration: %s", ri)
                if self.quiet is False and sys.stdout.isatty() is False:
                    print_info(f"Processing line: {idx} Repeat Iteration: {ri}")
                output = process_line(
                    llm=self.llm,
                    sandbox=self.sandbox,
                    line=line,
                    shaper=shaper,
                    store=self.store,
                    run=run,
                    progress=activate_progress_bar,
                )

                # Handle if the run fails, in the case the output data is None
                if final_status is None and output is None:
                    final_status = RunStatus.FAILED

                if return_outputs:
                    run.outputs.append(output)
                elif self.output_file is None:
                    if line_bar is not None:
                        string_output = convert_output_to_str(output)
                        line_bar.write(string_output, file=sys.stdout)
                    else:
                        print_data_output(output)
                else:
                    # Write to file
                    write_to_file(output, self.output_file)

        if line_bar is not None:
            line_bar.write("--- info", file=sys.stderr)
            line_bar.close()

        # If all the outputs have been present the run is a success
        if not final_status:
            final_status = RunStatus.SUCCESS

        run.end(status=final_status)

        logger.info("Data processed")
        return run
