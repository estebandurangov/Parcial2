from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.ClimaModel import *  
from config.database import Session

from services.ClimaService import ClimaService as Service 

clima_router = APIRouter()

tags = ['Clima']

@clima_router.post('/v1/clima', tags=tags, response_model=dict, summary="ingresar los datos del clima de una ciudad", status_code=201)
def create_clima_v1(clima: ClimaCreate) -> dict:
    db = Session
    nuevo_pais = Service(db).create_clima(clima)
    return JSONResponse(status_code=201, content={'message': f"Se ha registrado el clima para la ciudad: {clima.ciudad}"})

@clima_router.get('/v1/clima/{pais}/{ciudad}', tags=tags, response_model=ClimaRead, summary="consultar la información del clima de una ciudad.")
def get_clima_by_pais_ciudad_v1(pais: str, ciudad:str):
    db = Session
    result = Service(db).get_clima_by_pais_ciudad(pais, ciudad)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Pais o ciudad no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))