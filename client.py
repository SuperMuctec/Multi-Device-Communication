import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Code is ready")
    n = input("Enter text to convert to binary: ")
    channel_id = 1095047694499708988
    channel = bot.get_channel(channel_id)
    await channel.send("00100001011100110110010101110010011101100110010101110010 "+"Login Request Received")


bot.run("MTE3ODM2OTY0NzczNzg0NzkxOA.G8Z6in._xByACsMZSNCk5OZd7a3uhzOIsW7MXjyhAMln0")