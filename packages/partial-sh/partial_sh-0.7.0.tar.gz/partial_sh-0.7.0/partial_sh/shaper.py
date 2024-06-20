import logging
import re
from datetime import datetime
from pathlib import Path
from uuid import uuid4

import typer
from langchain.pydantic_v1 import BaseModel

from .instruction import InstructionMetadata, Modes

logger = logging.getLogger(__name__)


def prepare_key(s):
    s = s.lower().replace(" ", "_")
    # Remove special characters except for underscore
    return re.sub(r"[^a-z0-9_]", "", s)


class InvalidJson(Exception):
    pass


class ShaperConfigFile(BaseModel):
    id: str
    name: str | None = None
    created_at: str
    updated_at: str
    instructions: list[InstructionMetadata]
    functions: dict[str, str] = {}
    input_schema: dict | None = None
    repeat: int = 1


class Shaper:
    id: str
    name: str | None = None
    created_at: str
    updated_at: str
    instructions: list[InstructionMetadata] = []
    functions: dict[str, str] = {}
    repeat: int = 1
    input_schema: dict | None = None
    regenerate: bool = False

    def __init__(self):
        pass

    def new(
        self,
        name: str,
        instructions: list[str],
        functions: dict[str, str] = {},
        repeat: int = 1,
        regenerate: bool = False,
        mode: Modes | None = None,
        input_schema: dict | None = None,
    ):
        self.id = str(uuid4())
        self.name = name
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        self.instructions = [
            InstructionMetadata(instruction=instruction, mode=mode)
            for instruction in instructions
        ]
        self.functions = functions
        self.input_schema = input_schema
        self.repeat = repeat
        self.regenerate = regenerate
        return self

    def get_prep_name(self):
        # If name is not provided, use the first instruction
        if self.name is None or self.name == "":
            first_instruction = (self.instructions or [None])[0]
            if (
                first_instruction is None
                or first_instruction.instruction is None
                or first_instruction.instruction == ""
            ):
                return None
            prep_name = first_instruction.instruction
        else:
            prep_name = self.name

        return prepare_key(prep_name)[:50]

    def get_slug(self):
        key = self.id.split("-")[0]

        prep_name = self.get_prep_name()
        if prep_name is None:
            return key
        key = self.id.split("-")[0] + "__" + prep_name
        return key

    def load(self, shaper_config: ShaperConfigFile):
        self.id = shaper_config.id
        self.created_at = shaper_config.created_at
        self.updated_at = shaper_config.updated_at
        self.instructions = shaper_config.instructions
        self.functions = shaper_config.functions
        self.input_schema = shaper_config.input_schema
        self.repeat = shaper_config.repeat
        return self

    def load_from_file(self, file: Path):
        """
        Load shaper from json file.
        """
        if file.is_file():
            try:
                shaper_config = ShaperConfigFile.parse_file(file)
            except ValueError as e:
                e = InvalidJson(
                    f"Error parsing shaper json file is invalid: {file.absolute()}\n{e}"
                )
                raise typer.Exit(e)
        self.load(shaper_config)
        return self

    def save_to_file(self, file: Path):
        """
        Save shaper to json file.
        """
        shaper_config = ShaperConfigFile(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
            updated_at=datetime.now().isoformat(),
            instructions=self.instructions,
            functions=self.functions,
            input_schema=self.input_schema,
            repeat=self.repeat,
        )
        with open(file, "w") as f:
            json_content = shaper_config.json(indent=4)
            f.write(json_content)

    def lookup_code(self, instruction: str):
        key = prepare_key(instruction)
        return self.functions.get(key)

    def save_code(self, instruction: str, code: str):
        key = prepare_key(instruction)
        self.functions[key] = code
        return self

    def remove_code(self, instruction: str):
        key = prepare_key(instruction)
        self.functions.pop(key)
        return self
