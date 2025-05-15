# librerias

import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# configuracion de mensajes en consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# configuracion de enrutado correcto a .env
APP_PATH = Path(__file__).resolve().parent.parent.parent
ENV_PATH = APP_PATH / ".env"

# validando existencia de archivo .env
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
    logger.info(f"archivo .env encontrado en {ENV_PATH}")
else:
    logger.info(f"archivo .env no encontrado en {ENV_PATH}")


class Settings(BaseSettings):
    DEBUG:bool = os.getenv('DEBUG','False').lower() in('true','1','t')
    #propiedades validas y valores predeterminados desde .env
    USE_MYSQL: bool = os.getenv("USE_MYSQL", "False").lower() in ("true", "1", "t")
    DB_USERNAME: str = os.getenv("DB_USERNAME", "admin")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = os.getenv("DB_PORT", "8000")
    DB_NAME: str = os.getenv("DB_NAME", "products_db")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # verifica la existencia de la base de datos y el tipo de BD
    @property
    def database_url(self):
        if self.USE_MYSQL:
            logger.info(f"conexion a base de datos {self.DB_NAME} correcta")
            return f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            logger.warning(f"no existe conexion a base de datos")
    # configura el schema de Settings
    model_config = {
        "env_file": str(ENV_PATH),
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


settings = Settings()