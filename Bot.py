import discord
from discord.ext import commands
import os

client = discord.Client()
token = "Nzg4Njc3NTkzODA4ODk2MDAw.X9m_Pw.y0IcPDeznRbUmP-L7FxDEQJrBUM"
bot = discord.Client()
client = commands.Bot(command_prefix="a!")
client.load_extension('eval')

@client.event
async def on_ready():
    print('Bot: {0.user}'.format(client))

@client.command(aliases=["p", "h"])
async def pomoc(ctx):
    await ctx.send("Test")

client.run(token)
