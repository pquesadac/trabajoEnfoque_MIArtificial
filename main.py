from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from chatbot import procesar_consulta
 

app = FastAPI(
    title="Asistente Virtual de Soporte Técnico",
    description="API REST para el asistente virtual basado en PLN",
    version="1.0.0"
)
 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 

app.mount("/static", StaticFiles(directory="static"), name="static")
 
 

class Consulta(BaseModel):
    mensaje: str
 
 
class Respuesta(BaseModel):
    respuesta: str
 
 

# Endpoints
@app.get("/")
def inicio():
    """Sirve la interfaz web del chatbot."""
    return FileResponse("static/dashboard.html")
 
 
@app.post("/consulta", response_model=Respuesta)
def atender_consulta(consulta: Consulta):
    """
    Recibe la consulta del usuario en formato JSON:
    { "mensaje": "no tengo internet" }
    Devuelve la respuesta generada por el asistente.
    """
    respuesta = procesar_consulta(consulta.mensaje)
    return Respuesta(respuesta=respuesta)
 
 
@app.get("/health")
def health_check():
    """Endpoint para verificar que la API está en funcionamiento."""
    return {"estado": "ok", "servicio": "Asistente Virtual de Soporte Técnico"}