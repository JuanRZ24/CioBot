import discord
from discord.ext import commands
import requests 
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
VOCES_DISPONIBLES = {
    "cio": os.getenv('VOICECIO_ID'), 
    "yahir": os.getenv('VOICEYAHIR_ID'),
    "lloron": os.getenv('VOICELLORON_ID'),
    "checho" : os.getenv('VOICECHECHO_ID')
}
TOKEN_DISCORD = os.getenv('DISCORD_TOKEN')

voz_actual = VOCES_DISPONIBLES["cio"]

# Configuración de Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def generar_audio_elevenlabs(texto,voice_id):
    """Envía el texto a ElevenLabs y guarda el audio en un archivo"""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": texto,
        "model_id": "eleven_multilingual_v2", 
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open('audio_eleven.mp3', 'wb') as f:
            f.write(response.content)
        return True
    else:
        print(f"Error ElevenLabs: {response.text}")
        return False

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def voces(ctx):
    """Muestra la lista de voces disponibles"""
    nombres = ", ".join(VOCES_DISPONIBLES.keys())
    await ctx.send(f"🎙️ **Voces disponibles:** {nombres}\nUsa `!cambiarvoz <nombre>` para elegir una.")

@bot.command()
async def cambiarvoz(ctx, nombre_voz: str):
    global voz_actual

    nombre_voz = nombre_voz.lower()

    if nombre_voz in VOCES_DISPONIBLES:
        voz_actual = VOCES_DISPONIBLES[nombre_voz]
        await ctx.send(f" voz cambiada a **{nombre_voz}**")
    else:
        await ctx.send(f"esa voz no existe pendejo, usa !voces para ver la lista") 

@bot.command()
async def habla(ctx, *, texto: str):
    if not ctx.author.voice:
        await ctx.send("¡Entra a un canal de voz primero!")
        return

    canal_usuario = ctx.author.voice.channel
    voice_client = ctx.voice_client

    if voice_client is None:
        voice_client = await canal_usuario.connect()
    elif voice_client.channel != canal_usuario:
        await voice_client.move_to(canal_usuario)


    exito = generar_audio_elevenlabs(texto,voz_actual)

    if exito:
        if voice_client.is_playing():
            voice_client.stop()

        source = discord.FFmpegPCMAudio('audio_eleven.mp3')
        voice_client.play(source)

        while voice_client.is_playing():
            await asyncio.sleep(1)
 
    if os.path.exists('audio_eleven.mp3'):
             os.remove('audio_eleven.mp3')
    else:
        await ctx.send("Me quedé sin créditos o hubo un error en la API.")

@bot.command()
async def vete(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

# TU TOKEN DE DISCORD AQUÍ
bot.run(TOKEN_DISCORD)

