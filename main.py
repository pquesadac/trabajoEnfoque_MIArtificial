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
    return FileResponse("static/dashboard.html")
 
 
@app.post("/consulta", response_model=Respuesta)
def atender_consulta(consulta: Consulta):   
    respuesta = procesar_consulta(consulta.mensaje)
    return Respuesta(respuesta=respuesta)
 
 
@app.get("/health")
def health_check():
    return {"estado": "ok", "servicio": "Asistente Virtual de Soporte Técnico"}
