from dataclasses import dataclass #updating entity
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig: #dataIngestionConfig is one type of return function can created using decorator @dataclass as entity
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict