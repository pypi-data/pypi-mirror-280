from pathlib import Path
from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field


class FileItemEntity(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    name: Optional[str] = Field(None)
    path: Optional[str] = Field(None)
    is_file: Optional[bool] = Field(False)
    is_folder: Optional[bool] = Field(False)
    children: List['FileItemEntity'] = Field(default=[])

    @staticmethod
    def build_from_path(path: Path) -> 'FileItemEntity':
        return FileItemEntity(
                name=path.name,
                path=str(path.absolute()),
                is_file=path.is_file(),
                is_folder=path.is_dir(),
            )
