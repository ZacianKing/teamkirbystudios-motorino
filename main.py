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

  em.add_field(name = "Comandi", value = "tiro")

  await ctx.send(embed = em)

#helps
@help.command()
async def tiro(ctx):

  em = discord.Embed(title = "Tiro", description = "Palla Avvelenata della Prof.ssa Pyra")

  em.add_field(name = "**Syntax**", value = "mo.tiro")

  await ctx.send(embed = em)

#lista comandi
  

#Random words
@client.command()
async def tiro(ctx):
  tiro_responses = ['Hit',
   'Block',
   'Miss']
  await ctx.send(f'{random.choice(tiro_responses)}')

keep_alive()
client.run('XXX') #XXX = Inserisci il token del bot
