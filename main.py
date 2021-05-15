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
            mensajito = 'Tío, qué acabas de hacer {}'.format(member.mention)
            if before.channel == after.channel:
                if after.self_deaf and not before.self_deaf:
                    mensajito = 'Ya se ha cansado de nosotros don {}'.format(member.mention)
                elif before.self_deaf and not after.self_deaf:
                    mensajito = 'Hagamos las paces {}'.format(member.mention)

                elif after.self_mute and not before.self_mute:
                    mensajito = 'Noooo tío {} por ke te muteas'.format(member.mention)
                elif before.self_mute and not after.self_mute:
                    mensajito = 'Hombre, ya ha vuelto nuestro amiguito {}. ¿Qué pasa, guapetón?'\
                        .format(member.mention)

                elif after.self_stream and not before.self_stream:
                    mensajito = 'A ver qué cosa bakana nos quieres enseñar ahora {}'.format(member.mention)
                elif before.self_stream and not after.self_stream:
                    mensajito = '{} se finí 😔🤟'.format(member.mention)

                elif after.self_video and not before.self_video:
                    mensajito = 'Uy qué cara más bonita bb 😍 {}'.format(member.mention)
                elif before.self_video and not after.self_video:
                    mensajito = '{} c fue'.format(member.mention)
            else:
                mensajito = 'Oye, tú, {}, qué haces entrando en {}'.format(member.mention, after.channel.name)
            await bot_channel.send(mensajito)
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

    if message.content.lower() in ['holiwis', 'hola', 'hey', 'ey', 'jelou', 'wenas', 'buenas']:
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
