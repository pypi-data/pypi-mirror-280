import logging
import os
from datetime import datetime
from pathlib import Path

from langchain.pydantic_v1 import BaseModel, ValidationError

from .shaper import ShaperConfigFile, prepare_key

logger = logging.getLogger(__name__)


class ShaperInfo(BaseModel):
    id: str
    name: str | None = None
    filename: str | None = None
    content: ShaperConfigFile | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class ShaperStore:
    path: Path
    shaper_infos: list[ShaperInfo] = []

    def __init__(self, path: Path):
        self.path = path

    def refresh(self):
        self.shaper_infos = []
        self.list()

    def list(self) -> list[ShaperInfo]:
        for filename in os.listdir(self.path):
            if filename.endswith(".json"):
                shaper_name = filename[:-5].split("__")
                if len(shaper_name) < 2:
                    continue
                shaper_id = shaper_name[0]
                shaper_name = shaper_name[1]

                # Get when file was created
                created_at = datetime.fromtimestamp(
                    os.path.getctime(self.path / filename)
                )
                # created_at = created_at.isoformat()
                # Get when file was last modified
                updated_at = datetime.fromtimestamp(
                    os.path.getmtime(self.path / filename)
                )
                # updated_at = updated_at.isoformat()

                self.shaper_infos.append(
                    ShaperInfo(
                        id=shaper_id,
                        name=shaper_name,
                        filename=filename,
                        created_at=created_at,
                        updated_at=updated_at,
                    )
                )
        return self.shaper_infos

    def find_shaper_file(self, shaper_arg: str) -> Path:
        """
        Find the shaper file based on the shaper argument.
        """
        # Refresh the shaper store
        self.refresh()
        # Check if the shaper argument is already a file
        shaper_file = Path(shaper_arg)
        if shaper_file.is_file():
            return shaper_file

        # If not a file, try to find it in the shaper store
        shaper_file = self.get_filepath_by_id(shaper_arg) or self.get_filepath_by_name(
            shaper_arg
        )

        if not shaper_file or not shaper_file.is_file():
            # Handle the error as appropriate for your application
            return None

        return shaper_file

    def get_filepath_by_id(self, id: str):
        for shaper_info in self.shaper_infos:
            if shaper_info.id.startswith(id.split("-")[0]):
                filename = shaper_info.filename
                shaper_path = self.path / filename
                return shaper_path
        return None

    def get_filepath_by_name(self, name: str):
        for shaper_info in self.shaper_infos:
            key = prepare_key(name)
            if shaper_info.name.startswith(name) or shaper_info.name.startswith(key):
                filename = shaper_info.filename
                shaper_path = self.path / filename
                return shaper_path
        return None

    def get_by_id(self, id: str):
        for shaper_info in self.shaper_infos:
            if shaper_info.id.startswith(id.split("-")[0]):
                filename = shaper_info.filename
                shaper_path = self.path / filename
                with open(shaper_path, "r") as f:
                    try:
                        shaper = ShaperConfigFile.parse_raw(f.read())
                    except ValidationError:
                        logger.error("Error parsing file %s", filename)
                        return None
                shaper_info.content = shaper
                return shaper_info
        return None

    def get_by_name(self, name: str) -> ShaperInfo | None:
        matching_shapers = [p for p in self.shaper_infos if p.name.startswith(name)]

        # Sort shapers by updated_at in descending order and get the most recent one
        if matching_shapers:
            latest_shaper = max(
                matching_shapers, key=lambda p: p.updated_at or datetime.min
            )

            filename = latest_shaper.filename
            shaper_path = self.path / filename
            with open(shaper_path, "r") as f:
                try:
                    shaper = ShaperConfigFile.parse_raw(f.read())
                except ValidationError:
                    logger.error("Error parsing file %s", filename)
                    return None
            latest_shaper.content = shaper
            return latest_shaper
        else:
            return None
