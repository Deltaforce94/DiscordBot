import youtube_dl
import discord
import requests
import responses
import random
import json
import asyncio

from keep_alive import keep_alive
from discord.ext import commands

token = "bot token goes here"
weather_api_key = "d49be36c092040338e23e3943f3bd66f"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

bullingMode = False
alarmMode = False

# Cosas de Youtube DL
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
  'format': 'bestaudio/best',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
  'source_address':
  '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):

  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)
    self.data = data
    self.title = data.get('title')
    self.url = ""

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(
      None, lambda: ytdl.extract_info(url, download=not stream))
    if 'entries' in data:
      # take first item from a playlist
      data = data['entries'][0]
    filename = data['title'] if stream else ytdl.prepare_filename(data)
    return filename


#Final cosas de Youtube DL


@bot.event
async def on_ready():
  print("Bot cargado y listo")


@bot.command()
async def bullylili(ctx):
  """
    Activar o desactivar el modo bulling a Lili
    """
  global bullingMode
  bullingMode = not bullingMode
  await ctx.send(f"Modo Bulling a Lili = {bullingMode}")


@bot.command()
async def flipcoin(ctx):
  """
    Tira una moneda, para ver si sale cara o cruz.
    """
  result = random.choice(["Cara", "Cruz"])
  await ctx.send(f"El resultado es: {result}")


@bot.command()
async def joke(ctx):
  """
    Envia un chiste aleatorio de Chuck Norris
    """
  url = 'https://api.chucknorris.io/jokes/random'
  response = requests.get(url)
  data = json.loads(response.text)
  await ctx.send(data['value'])


@bot.command()
async def weather(ctx, ciudad):
    """
    Verificar el clima en una ciudad específica utilizando la API de Weatherbit.
    Uso: !weather <ciudad>
    """
    url = f"https://api.weatherbit.io/v2.0/current?city={ciudad}&lang=es&key={weather_api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    if "data" in data:
        datos_clima = data["data"][0]
        descripcion = datos_clima["weather"]["description"]
        temperatura = datos_clima["app_temp"]
        humedad = datos_clima["rh"]

        await ctx.send(
            f"Clima en {ciudad}: {descripcion}, Temperatura: {temperatura}°C, Humedad: {humedad}%")
    else:
        await ctx.send("No se pudo obtener información sobre el clima.")


@bot.command()
async def joined(ctx, who: discord.Member):
  """
    Informa de cuando se unio un usuario concreto al servidor.
    """
  #await ctx.send(who.joined_at)
  await ctx.send(f"El usuario {who.name} se unió en esta fecha: {who.joined_at}")



@bot.command()
async def remindme(ctx, minutes, asunto):
  """
    Crea un recordatorio para no olvidar algo.
    Uso: !remindme <minutes>
    """
  try:
    minutes = int(minutes)
  except ValueError:
    await ctx.send("Introduce unos minutos validos")
    return

  await ctx.send(f"Entendido, te lo recordare en {minutes} minuto(s).")
  await asyncio.sleep(minutes * 60)
  await ctx.send(
    f"Hey {ctx.author.mention}, Han pasado {minutes} minuto(s). Es hora de {asunto}"
  )


@bot.command()
async def insultar(ctx, nombre):
  """
    Insulta a alguien llamado Quniverk de forma aleatoria.
    Usage: !insultar <nombre>
    """
  if nombre.lower() == "quniverk":
    insulto = random.choice(responses.insultos)
    await ctx.send(insulto)
  else:
    await ctx.send(f"No puedo insultar a alguien que no se llame Quniverk.")


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
  if not ctx.message.author.voice:
    await ctx.send("{} is not connected to a voice channel".format(
      ctx.message.author.name))
    return
  else:
    channel = ctx.message.author.voice.channel
  await channel.connect()


@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_connected():
    await voice_client.disconnect()
  else:
    await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='play', help='To play song')
async def play(ctx, url):
  try:
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
      filename = await YTDLSource.from_url(url, loop=bot.loop)
      voice_channel.play(
        discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
    await ctx.send('**Now playing:** {}'.format(filename))
  except:
    await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_playing():
    await voice_client.pause()
  else:
    await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_paused():
    await voice_client.resume()
  else:
    await ctx.send(
      "The bot was not playing anything before this. Use play_song command")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
  voice_client = ctx.message.guild.voice_client
  if voice_client.is_playing():
    await voice_client.stop()
  else:
    await ctx.send("The bot is not playing anything at the moment.")


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith('!'):
    await message.delete(
    )  # Borra el mensaje después de procesarlo como comando
  elif 'genero' in message.content:
    await message.channel.send("roger roger")
  elif 'tiktok' in message.content:
    await message.add_reaction('🤮')
  elif 'lili' in message.author.name:
    if bullingMode:
      await message.channel.send(responses.reemplazar_vocales(message.content))

  await bot.process_commands(message)


keep_alive()
bot.run(token)
