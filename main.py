import discord
from discord.ext import commands
import logging
import nest_asyncio
from dotenv import load_dotenv 
import os 

# Load discord token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode = 'w')
intents = discord.Intents.default()

intents.message_content = True  #manually adjust intents to change scope of bot
intents.members = True

bot = commands.Bot(command_prefix='es!', intents =intents)
everyones_role="everyones"

@bot.event
async def on_ready():
    print("Meow")

async def main():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    await bot.run(token, log_handler=handler, log_level = logging.DEBUG)

if __name__ == "__main__":
    asyncio.run(main())
