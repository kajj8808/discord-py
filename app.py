import os
import discord
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    print(f"on_message : {message}")


@bot.command()
async def hello(ctx):
    print(ctx)
    await ctx.send("Hi!")

bot.run(token=token)
