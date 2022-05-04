import discord
import json
import random
from keep_alive import keep_alive
from discord.ext import commands, tasks
from discord import client
from itertools import cycle

#clients
client = commands.Bot(command_prefix="mo.")
status = cycle(['Il mio comando è mo.help!', 'NEWS: sono il nuovo BOT :D', 'Il mio prefix è mo.'])

client.remove_command("help")

@client.event
async def on_ready():
  change_status.start()
  print('Il Bot è online!')

@tasks.loop(seconds=30)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

#categorie
@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "usa mo.help <comando> per l'informazioni di questo comando.", color = ctx.author.color)

  em.add_field(name = "Giochi", value = "pa - calcio - basket")

  em.add_field(name = "Informazioni", value = "github")

  await ctx.send(embed = em)

#helps
@help.command()
async def pa(ctx):

  em = discord.Embed(title = "Palla Avvelenata", description = "Palla Avvelenata della Prof.ssa Pyra")

  em.add_field(name = "**Syntax**", value = "mo.pa")

  await ctx.send(embed = em)

@help.command()
async def calcio(ctx):

  em = discord.Embed(title = "Calcio", description = "Il calcio della Prof.ssa Pyra")

  em.add_field(name = "**Syntax**", value = "mo.calcio")

  await ctx.send(embed = em)

@help.command()
async def basket(ctx):

  em = discord.Embed(title = "Basket", description = "Il basket della Prof.ssa Pyra")

  em.add_field(name = "**Syntax**", value = "mo.basket")

  await ctx.send(embed = em)

@help.command()
async def github(ctx):

  em = discord.Embed(title = "GitHub", description = "link GitHub per il codice di questo BOT")

  em.add_field(name = "**Syntax**", value = "mo.github")

  await ctx.send(embed = em)

#lista comandi
@client.command()
async def github(ctx):
  await ctx.send("GitHub link: https://github.com/ZacianKing/teamkirbystudios-motorino")

#Random words
@client.command()
async def pa(ctx):
  tiro_responses = ['Colpito',
   'Bloccato',
   'Schivato']
  await ctx.send(f'{random.choice(tiro_responses)}')

@client.command()
async def calcio(ctx):
  tiro_responses = ['GOL',
   'Tiro bloccato',
   'Giocatore schivato',
   'Fallo (Cartellino Giallo)',
   'Fallo (Cartellino Rosso)',
   'Dribbla']
  await ctx.send(f'{random.choice(tiro_responses)}')

@client.command()
async def basket(ctx):
  tiro_responses = ['Canestro (+2 Punti)',
   'Canestro (+3 Punti)',
   'Giocatore schivato',
   'Palleggia']
  await ctx.send(f'{random.choice(tiro_responses)}')

keep_alive()
client.run('XXX') #XXX <- Mettete il token del vostro bot
