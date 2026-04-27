import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
 
nlp = spacy.load("es_core_news_sm")
 

datos_entrenamiento = [
    # Contraseña
    ("no puedo acceder a mi cuenta", "contrasena"),
    ("olvidé mi contraseña", "contrasena"),
    ("quiero cambiar mi clave", "contrasena"),
    ("no recuerdo mi contraseña", "contrasena"),
    ("resetear contraseña", "contrasena"),
    ("mi cuenta está bloqueada", "contrasena"),
 
    # Red / Internet
    ("no tengo internet", "red"),
    ("no me conecta el wifi", "red"),
    ("la conexión va muy lenta", "red"),
    ("se ha caído la red", "red"),
    ("no puedo navegar", "red"),
    ("problemas de conexión", "red"),
 
    # Hardware
    ("el ordenador no enciende", "hardware"),
    ("la pantalla está en negro", "hardware"),
    ("el teclado no funciona", "hardware"),
    ("el ratón no responde", "hardware"),
    ("el equipo se apaga solo", "hardware"),
    ("hace ruido el ordenador", "hardware"),
 
    # Software
    ("la aplicación no abre", "software"),
    ("el programa da error", "software"),
    ("se ha colgado el sistema", "software"),
    ("no puedo instalar el software", "software"),
    ("la app se cierra sola", "software"),
    ("error al ejecutar el programa", "software"),
 
    # Translado del problema a un tecnico
    ("necesito hablar con un técnico", "escalado"),
    ("quiero que me llame alguien", "escalado"),
    ("esto no lo puede resolver el bot", "escalado"),
    ("necesito ayuda humana", "escalado"),
    ("hablar con una persona", "escalado"),
]
 

respuestas = {
    "contrasena": (
        "Para restablecer tu contraseña, sigue estos pasos:\n"
        "1. Ve a la página de inicio de sesión.\n"
        "2. Haz clic en '¿Olvidaste tu contraseña?'.\n"
        "3. Introduce tu correo electrónico y sigue las instrucciones.\n"
        "Si el problema persiste, contacta con soporte."
    ),
    "red": (
        "Para solucionar problemas de conexión:\n"
        "1. Reinicia el router desconectándolo 30 segundos.\n"
        "2. Comprueba que el cable de red está bien conectado.\n"
        "3. Desactiva y vuelve a activar el WiFi en tu dispositivo.\n"
        "Si el problema continúa, puede ser una incidencia del proveedor."
    ),
    "hardware": (
        "Para problemas de hardware:\n"
        "1. Comprueba que todos los cables están bien conectados.\n"
        "2. Reinicia el equipo completamente.\n"
        "3. Si el equipo no enciende, verifica que recibe alimentación eléctrica.\n"
        "Si el problema persiste, será necesaria una revisión técnica presencial."
    ),
    "software": (
        "Para problemas de software:\n"
        "1. Cierra la aplicación y vuelve a abrirla.\n"
        "2. Reinicia el equipo.\n"
        "3. Comprueba que el software está actualizado a la última versión.\n"
        "4. Si el error persiste, desinstala y vuelve a instalar la aplicación."
    ),
    "escalado": (
        "Entendido. Voy a transferirte con un técnico especializado.\n"
        "Por favor, indica tu nombre y número de empleado para agilizar la gestión.\n"
        "Tiempo estimado de espera: 5-10 minutos."
    ),
    "desconocido": (
        "Lo siento, no he podido entender tu consulta.\n"
        "Por favor, intenta reformularla o indica si deseas hablar con un técnico."
    ),
}
 

textos = [d[0] for d in datos_entrenamiento]
etiquetas = [d[1] for d in datos_entrenamiento]
 
clasificador = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("nb", MultinomialNB()),
])
clasificador.fit(textos, etiquetas)
 
 
# Esta es la funcion de preprocesado con spacy
def preprocesar(texto: str) -> str:
    doc = nlp(texto.lower())
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return " ".join(tokens)
 
 

# Esta es la funcion principal
def procesar_consulta(texto_usuario: str) -> str:
    texto_limpio = preprocesar(texto_usuario)
 
    if not texto_limpio:
        return respuestas["desconocido"]
 
    intencion = clasificador.predict([texto_limpio])[0]
    return respuestas.get(intencion, respuestas["desconocido"])
