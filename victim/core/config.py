"""config core"""
import os
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get("POSTGRES_SERVER"))


class Settings(BaseSettings):
    """Setting class"""
    ENV = os.environ.get("ENV")
    SENTRY_KEY = os.environ.get('SENTRY_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES = 60*60*30
    API_V1_STR: str = "/api/v2"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")
    AWS_BUCKET = os.environ.get("AWS_BUCKET")
    AWS_SPACES_FOLDER = os.environ.get("AWS_SPACES_FOLDER")
    AWS_URL = os.environ.get("AWS_URL")
    AWS_ENDPOINT = os.environ.get("AWS_ENDPOINT")
    AWS_CDN = os.environ.get("AWS_CDN")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')

    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'kendeptrai'
    LOGIN_SSO_LINK: str = os.environ.get('LOGIN_SSO_LINK') or 'http://omzkong-login.enabledemo.com'
    FE_URL: str = os.environ.get('FE_URL') or 'https://dev-dewix.omzones.com'
    OMZ_API_URL = os.environ.get('OMZ_API_URL') or 'https://omzkong-test.enabledemo.com'
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:  # pylint: disable=no-self-argument,invalid-name
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
