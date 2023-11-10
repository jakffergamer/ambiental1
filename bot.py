import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random

#NO BORRAR 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios, también se define que el bot funcione con ! 
bot = commands.Bot(command_prefix='?', intents=intents) 

#Para saber si hemos iniciado sesión
@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")
    print("...........")


#Así se hacen los comandos para que el bot opere
@bot.command()  
async def consejos(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    consejos=[
        "caminar es muy sano",
        "la bicicleta es mejor",
        "no votes la basura en la calle"
    ]
    await ctx.send( random.choice(consejos) )  #acá es lo que el BOT va a responderte cuando escribas !Micomando
    
@bot.command() 
async def videos(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    links=[
        "https://www.youtube.com/watch?v=SATxaT0rZiw",
        "https://www.youtube.com/watch?v=L9hPgnIToiM",
        "https://www.youtube.com/watch?v=JkqK7iem_AU"
    ]
    await ctx.send( random.choice(links) )

@bot.command() 
async def retos(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    retos=[
        "construye 2 jugtes con basura reciclada",
        "planta 2 plantas",
        "ayuda a limpiar tu vecindario"
    ]
    await ctx.send( random.choice(retos) )
@bot.command() 
async def webs(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    webs=[
        "https://www.fundacionaquae.org/wiki/como-salvar-planeta/",
        "https://www.greenpeace.org/mexico/blog/49009/50-tips-para-cuidar-el-planeta/",
        "https://eacnur.org/es/blog/acciones-cuidar-medio-ambiente-casa-tc_alt45664n_o_pstn_o_pst"
    ]
    
    await ctx.send( random.choice(webs) )
@bot.command() 
async def info(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    info=[
        "este bot te da consejos y links para cuidar el medio ambiente .los comando son: consejos,retos,videos y webs"
    ]
    
    await ctx.send(info )



bot.run("token")