import discord
import json
import random
from keep_alive import keep_alive
from discord.ext import commands, tasks
from discord import client
from itertools import cycle

#clients
client = commands.Bot(command_prefix="m.")
status = cycle(['Fai m.help per vedere i vari comandi!'])

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
  em = discord.Embed(title = "Help", description = "Usa m.help <comando> per avere informazioni su quel comando.", color = ctx.author.color)

  em.add_field(name = "Comandi", value = "TiroPA - Passaggio - Dribbling - Contrasto - Tiro")

  await ctx.send(embed = em)

#helps
@help.command()
async def tiropa(ctx):

  em = discord.Embed(title = "TiroPA", description = "Usalo per tirare (Sport: Palla Avvelenata)! - Colpito = Hai colpito l'avversario - Bloccata = Il tuo avversario ha bloccato il tiro - Bersaglio Mancato = Hai sbagliato la mira e non hai colpito - E' consigliato scrivere il nome di chi vuoi colpire per semplificare le cose mentre si gioca. (esempio: m.tiro Poyos)")

  em.add_field(name = "**Syntax**", value = "m.tiropa")

  await ctx.send(embed = em)

@help.command()
async def passaggio(ctx):

  em = discord.Embed(title = "Passaggio", description = "Usalo per passare la palla (Sport: Calcio)! - Palla passata = Hai passato la palla al tuo compagno - Palla intercettata = Hai sbagliato il passaggio e un avversario ha intercettato il passaggio - Qui sta a te decidere se vuoi anche scrivere il nome del tuo compagno al quale vuoi passare la palla")

  em.add_field(name = "**Syntax**", value = "m.passaggio")

  await ctx.send(embed = em) 

@help.command()
async def dribbling(ctx):

  em = discord.Embed(title = "Dribbling", description = "Usalo se vuoi provare a dribblare un avversario (Sport: Calcio)! - Avversario Superato = Sei riuscito a dribblare l'avversario - Dribbling non riuscito = Non sei riuscito a superare l'avversario, che ha recuperato il pallone - Fallo subito = Nel cercare di non farsi dribblare da te, l'avversario ha commesso fallo - Fallo commesso = Nel tentativo di superare l'avversario, hai usato troppo il fisico e hai commesso fallo")

  em.add_field(name = "**Syntax**", value = "m.dribbling")

  await ctx.send(embed = em)
@help.command()
async def contrasto(ctx):

  em = discord.Embed(title = "Contrasto", description = "Usalo se vuoi provare a contrastare un avversario e recuperare il pallone (Sport: Calcio)! - Contrasto riuscito = Sei riuscito a usare il fisico per riprendere il pallone - Contrasto non riuscito = Non sei riuscito a recuperare il pallone e l'avversario ti ha superato - Fallo commesso = Hai usato troppo il fisico/hai mosso male la gamba/piede per recuperare il pallone e hai commesso fallo sull'avversario - Fallo subito = Mentre cercavi di recuperare la palla, l'avversario per proteggerla ha usato troppo il fisico, commettendo fallo su di te")  

  em.add_field(name = "**Syntax**", value = "m.contrasto")

  await ctx.send(embed = em)

@help.command()
async def tiro(ctx):

  em = discord.Embed(title = "Tiro", description = "Usalo quando vuoi tirare (Sport: Calcio)! - Gol = Hai tirato e sei riuscito a segnare - Parata = Hai provato a segnare ma il portiere avversario l'ha parata - Palo/Traversa = Hai provato a tirare ma hai colptio il palo o la traversa - Tiro fuori = Hai tirato male e la palla è andata fuori - Questo comando si può usare sia su azione che su punizioni e rigori")  

  em.add_field(name = "**Syntax**", value = "m.tiro")

  await ctx.send(embed = em)

#lista comandi
  

#Random words
@client.command()
async def tiropa(ctx):
  tiropa_responses = ['Colpito',
   'Bloccata',
   'Bersaglio Mancato']
  await ctx.send(f'{random.choice(tiropa_responses)}')

@client.command()
async def passaggio(ctx):
  pass_responses = ['Palla passata',
   'Passaggio intercettato']
  await ctx.send(f'{random.choice(pass_responses)}')
  
@client.command()
async def dribbling(ctx):
  drib_responses = ['Avversario superato',
   'Dribbling non riuscito',
   'Fallo subito', 'Fallo commesso']
  await ctx.send(f'{random.choice(drib_responses)}')

@client.command()
async def contrasto(ctx):
  drib_responses = ['Contrasto riuscito',
   'Contrasto non riuscito',
   'Fallo commesso', 'Fallo subito']
  await ctx.send(f'{random.choice(drib_responses)}')
  
@client.command()
async def tiro(ctx):
  tiro_responses = ['Gol',
   'Parata',
   'Palo/Traversa', 'Tiro fuori']
  await ctx.send(f'{random.choice(tiro_responses)}')
  
keep_alive()
client.run('XXX') #XXX = Inserisci il token del bot
