from functools import lru_cache
from pathlib import Path
from typing import BinaryIO
from mimetypes import guess_type
import uuid

import boto3

from src.settings import get_settings


class S3Storage:
    default_content_type = "application/octet-stream"
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    AWS_S3_ENDPOINT_URL: str
    AWS_DEFAULT_ACL: str
    AWS_S3_CUSTOM_DOMAIN: str = ""
    AWS_S3_USE_SSL: bool
    AWS_QUERYSTRING_AUTH: bool = False

    def __init__(self) -> None:
        assert not self.AWS_S3_ENDPOINT_URL.startswith(
            "http"
        ), "URL should not contain protocol"

        self._http_scheme = "https" if self.AWS_S3_USE_SSL else "http"
        self._url = f"{self._http_scheme}://{self.AWS_S3_ENDPOINT_URL}"
        session = boto3.session.Session()
        self._s3 = session.resource(
            service_name="s3",
            endpoint_url=self._url,
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
        )
        self._bucket = self._s3.Bucket(name=self.AWS_S3_BUCKET_NAME)

    def get_path(self, name: str) -> str:
        return "{}://{}/{}/{}".format(
            self._http_scheme,
            self.AWS_S3_ENDPOINT_URL,
            self.AWS_S3_BUCKET_NAME,
            name,
        )

    async def write(self, file: BinaryIO, key: str) -> str:
        """Adds file to s3 storage and changes filename to uuid.uuid4()+file suffix"""
        file.seek(0, 0)
        key = self.generate_new_filename(key)
        self._bucket.upload_fileobj(
            file,
            key,
            ExtraArgs={
                'ContentType': guess_type(key)[0],
                'ACL': 'public-read',
            },
)
        return key

    async def delete(self, key: str) -> str:
        self._s3.Object(self.AWS_S3_BUCKET_NAME, key).delete()  # Boto3 sucks
        return key

    def generate_new_filename(self, filename: str) -> str:
        suffix = Path(filename).suffix
        filename = f"{uuid.uuid4().hex}{suffix}"
        while self._check_object_exists(filename):
            filename = f"{uuid.uuid4().hex}{suffix}"
        return filename

    def _check_object_exists(self, key: str) -> bool:
        try:
            self._bucket.Object(key).load()
        except boto3.exceptions.botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False

        return True


class PublicAssetS3Storage(S3Storage):
    AWS_ACCESS_KEY_ID = get_settings().AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = get_settings().AWS_SECRET_ACCESS_KEY
    AWS_S3_BUCKET_NAME = get_settings().AWS_S3_BUCKET_NAME
    AWS_S3_ENDPOINT_URL = get_settings().AWS_S3_ENDPOINT_URL
    AWS_DEFAULT_ACL = get_settings().AWS_DEFAULT_ACL
    AWS_S3_USE_SSL = get_settings().AWS_S3_USE_SSL


@lru_cache
def s3_session_maker():
    return PublicAssetS3Storage()
