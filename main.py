import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv 
import os 
import asyncio

# Load discord token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode = 'w')
intents = discord.Intents.default()

intents.message_content = True  #manually adjust intents to change scope of bot
intents.members = True

bot = commands.Bot(command_prefix='es!', intents =intents)
everyones_role="everyones"

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded cog: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load cog {filename[:-3]}: {e}")

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())
