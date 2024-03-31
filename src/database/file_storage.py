from typing import Any

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType as _FileType

from src.settings import get_settings

storage = FileSystemStorage(path=get_settings().FILE_STORAGE_PATH)


class FileType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=storage, *args, **kwargs)
