# 🤖 Asistente Virtual de Soporte Técnico

Trabajo de Enfoque — Módulo de Modelos de Inteligencia Artificial  
Curso de Especialización de Inteligencia Artificial y Big Data · DAVANTE

---

## 📋 Descripción

Asistente virtual basado en **Procesamiento de Lenguaje Natural (PLN)** orientado al soporte técnico empresarial. El sistema interpreta consultas de usuarios en lenguaje natural, las clasifica por intención y devuelve soluciones predefinidas o escala la consulta a un técnico humano cuando es necesario.

---

## 🧠 Tecnologías utilizadas

| Tecnología | Uso en el proyecto |
|---|---|
| **spaCy** | Preprocesado del texto: tokenización, lematización y eliminación de stopwords |
| **Scikit-Learn** | Clasificador de intenciones (TF-IDF + Naive Bayes) |
| **FastAPI** | API REST para exponer el asistente como servicio web |
| **Uvicorn** | Servidor ASGI para ejecutar la aplicación |
| **HTML/CSS/JS** | Interfaz web del chat |

---

## ▶️ Ejecución

```bash
python -m uvicorn main:app --reload
```

Abre el navegador en:
```
http://localhost:8000
```

---

## 🗂️ Categorías de consultas soportadas

| Categoría | Ejemplos |
|---|---|
| **Contraseña** | "Olvidé mi contraseña", "Mi cuenta está bloqueada" |
| **Red** | "No tengo internet", "El WiFi no conecta" |
| **Hardware** | "El ordenador no enciende", "La pantalla está en negro" |
| **Software** | "La aplicación da error", "El programa no responde" |
| **Escalado** | "Necesito hablar con un técnico", "Necesito ayuda humana" |

---

## 🔌 API REST

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Sirve la interfaz web |
| POST | `/consulta` | Procesa la consulta del usuario |
| GET | `/health` | Comprueba el estado de la API |

**Ejemplo de petición:**
```json
POST /consulta
{
  "mensaje": "no tengo internet"
}
```

**Ejemplo de respuesta:**
```json
{
  "respuesta": "Para solucionar problemas de conexión: ..."
}
```

---

## ⚠️ Limitaciones conocidas

El clasificador puede perder precisión con consultas muy coloquiales, regionalismos o errores ortográficos, debido al tamaño reducido del dataset de entrenamiento.
