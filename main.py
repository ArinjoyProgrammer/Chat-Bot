import discord
from discord.ext import commands
import os

token = 'OTEyMjE0NjI3MTQ2OTI0MTIy.YZssEw.gymK2BoShTQ8Qh-bZBeLgRcvcHs'
prefixes = 'C!', 'c!'

client = commands.Bot(command_prefix=prefixes)


@client.event
async def on_ready():
  print("Bot is ready!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
