from typing import Any

from fastapi_storages import S3Storage
from fastapi_storages.integrations.sqlalchemy import FileType as _FileType

from src.settings import get_settings


class PublicAssetS3Storage(S3Storage):
    AWS_ACCESS_KEY_ID = get_settings().POSTGRES_PASSWORD
    AWS_SECRET_ACCESS_KEY = get_settings().AWS_SECRET_ACCESS_KEY
    AWS_S3_BUCKET_NAME = get_settings().AWS_S3_BUCKET_NAME
    AWS_S3_ENDPOINT_URL = get_settings().AWS_S3_ENDPOINT_URL
    AWS_DEFAULT_ACL = get_settings().AWS_DEFAULT_ACL
    AWS_S3_USE_SSL = get_settings().AWS_S3_USE_SSL


class FileType(_FileType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(storage=PublicAssetS3Storage(), *args, **kwargs)


storage = PublicAssetS3Storage()
