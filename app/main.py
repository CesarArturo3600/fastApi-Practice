# librerias

from fastapi import FastAPI

from app.core.database import Base

# funciones o objetos(instancias)




# crear las tablas
Base.metadata.create_all()


# crea instancia de FastAPI en variable app

app = FastAPI(
    title='API',
    description='My first API',
    version='1.0.0',
    debug=True)




# funcion decorada que devuelve un objeto JSON
@app.get('/')
def root():
    return {'message':'welcome to my first API'}




