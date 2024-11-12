import os
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
API_URL = os.getenv("API_URL")
INITIAL_MESSAGE = "¡Hola! Soy el robot del laboratorio de InTeractiOn. Puedes preguntarme sobre la base de conocimiento del lab."
HELP_MESSAGE = "Aquí las descripciones de los comandos"
