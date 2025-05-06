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
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    



settings = Settings()



