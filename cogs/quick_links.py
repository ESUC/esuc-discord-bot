import discord
from discord.ext import commands

# Links, update when needed
LINK_TREE="https://linktr.ee/esuc"
STUDENT_LEADERS_GUIDE="https://www.seasoasa.ucla.edu/studentleaderguide-2025-2026/"
E_WEEK="https://www.esuc.ucla.edu/bruin-engineers-week/"
CALENDAR="https://calendar.google.com/calendar/u/0/r?cid=NW4yYWFvZHVvbWZsbnIzNjk5NTFhbXRsc2dAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
WEBSITE="https://www.esuc.ucla.edu/"

class QuickLinks(commands.Cog):
    """Commands for sending quick links."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def linktree(self, ctx):
        """Sends ESUC's linktree"""
        embed = discord.Embed(
            title="ESUC Link Tree",
            description=f"[Click here view our link tree]({LINK_TREE})",
            color=discord.Color.blue()
        )

async def setup(bot):
    await bot.add_cog(QuickLinks(bot))