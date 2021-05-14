import codecs

import discord
import requests
from bs4 import BeautifulSoup


client = discord.Client()


@client.event
async def on_ready():
    print('Estamo activo papi con el nombre: {0.user}'.format(client))


@client.event
async def on_guild_join(guild):
    bot_channel = client.get_channel(677621356665372681)
    if bot_channel and bot_channel.permissions_for(guild.me).send_messages:
        await bot_channel.send(mensaje_bienvenida)   # .format(guild.name))


@client.event
async def on_voice_state_update(member, before, after):
    print("EYEYEYEY QUE PASA AQUI")
    if after.channel and not member.bot:
        bot_channel = client.get_channel(842892349361094717)
        if bot_channel:
            await bot_channel.send('Oye, tú, {}, qué haces entrando en {}'.format(member.name, after.channel.name))
        else:
            print("Oye aquí no se detecta el general...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'comandos' in message.content:
        await message.channel.send('¿Cómo que comandos, te crees que soy tu chacha? Sí soy.\n'
                                   'Si dices hola digo hola, si me llamas guapo pues tu mas, luego esta don quijote... '
                                   'y si pones "yo soy muy aleatorio", demuestro que yo más')

    if message.content in ['holiwis', 'hola', 'hey', 'ey', 'jelou', 'wenas', 'buenas']:
        await message.channel.send('Jelou bro 😎')

    if message.content.startswith('eres') or 'guapo' in message.content:
        await message.channel.send('Tu más uwu')

    if message.content == 'aki don kijote':
        await message.channel.send(respuesta_quijotesca)

    if 'yo soy muy aleatorio' in message.content:
        r = requests.get("https://es.wikipedia.org/wiki/Especial:Aleatoria")
        soup = BeautifulSoup(r.text, "lxml")
        mensaje = soup.select_one('div#mw-content-text').select_one("p").text
        mensaje += '\n\n'
        mensaje += 'Salsa: ' + r.url
        await message.channel.send(mensaje)

if __name__ == '__main__':
    respuesta_quijotesca = "nooo no digas eso"
    mensaje_bienvenida = "Hola a todos <3"
    with codecs.open("clavessecretisimas.txt", "r", "utf-8") as f:
        client.run(f.readline())
        respuesta_quijotesca = f.readline()
        mensaje_bienvenida = f.readline()
