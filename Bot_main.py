# Importar las bibliotecas necesarias
import discord  # Biblioteca para trabajar con la API de Discord
from discord.ext import commands  # Módulo para controlar el bot basado en comandos
import requests  # Biblioteca para hacer solicitudes HTTP
import pyttsx3  # Biblioteca para la síntesis de voz

# Inicializar el sintetizador de voz
engine = pyttsx3.init()  # Crear un objeto para la síntesis de voz

# Inicializar el objeto del bot
intents = discord.Intents.default()  # Configurar los permisos para el bot
intents.message_content = True  # Habilitar la capacidad de leer el contenido de los mensajes
bot = commands.Bot(command_prefix="!", intents=intents)  # Crear un bot con el prefijo de comando especificado

# Función para obtener un dato curioso aleatorio a través de una API
def get_fact() -> str:
    """
    Recupera un dato curioso aleatorio desde la API.

    Retorna:
        str: El texto del dato o un mensaje de error
    """
    base_url = "https://uselessfacts.jsph.pl/random.json?language=en"  # URL para obtener un dato curioso aleatorio
    response = requests.get(base_url)  # Hacer una solicitud GET a la API

    if response.status_code == 200:  # Si la solicitud fue exitosa (código 200)
        data = response.json()  # Analizar la respuesta en formato JSON
        return data.get("text", "No se pudo obtener el dato.")  # Devolver el texto del dato
    else:
        return "No se pudo obtener la información. Por favor, inténtalo más tarde."  # Devolver un mensaje de error

# Función para la síntesis de voz
def speak(text: str):
    """
    Vocaliza el texto proporcionado usando pyttsx3.

    Parámetros:
        text (str): Texto que se va a vocalizar
    """
    engine.say(text)  # Pasar el texto para la síntesis
    engine.runAndWait()  # Realizar la síntesis de voz y esperar a que termine

# Comando para obtener un dato curioso
@bot.command()
async def fact(ctx):
    """
    Comando para recuperar un dato curioso aleatorio y vocalizarlo.

    Parámetros:
        ctx: Contexto del comando (información sobre la invocación del comando)
    """
    random_fact = get_fact()  # Obtener un dato curioso aleatorio
    await ctx.send(f"Aquí tienes un dato curioso: {random_fact}")  # Enviar el dato al canal de Discord
    speak(random_fact)  # Vocalizar el dato

# Ejecutar el bot
bot.run("Token")  # Ejecutar el bot con el token especificado