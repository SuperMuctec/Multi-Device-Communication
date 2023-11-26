import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content

bot = commands.Bot(command_prefix='!', intents=intents)

def binary_to_text(binary_str):
    binary_values = binary_str.split()
    text_result = ''.join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text_result

def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.startswith("00100001011100110110010101110010011101100110010101110010"):
        a = message.content
        a = a[len("00100001011100110110010101110010011101100110010101110010"):].strip()
        a = "Processing Request"
        await message.channel.send(a)

bot.run("MTE3ODM2OTk5MzIyNjg1MDM4NA.GUNeFz.bZ4b2o3QRzGdVI1TOaCk0TlxJUNk2_tJcruT08")