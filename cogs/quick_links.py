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
        """Sends ESUC's linktree 🌲"""
        embed = discord.Embed(
            title="ESUC Link Tree",
            description=f"[Click here view our link tree.]({LINK_TREE})",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def slg(self, ctx):
        """Sends student leader guide 📖"""
        embed = discord.Embed(
            title="SEAS Student Leaders Guide",
            description=f"[Click here view the student leaders guide.]({STUDENT_LEADERS_GUIDE})",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def eweek(self, ctx):
        """Sends E-Week Website 💻"""
        embed = discord.Embed(
            title="Bruin Engineers Week",
            description=f"[Click here view our site.]({E_WEEK})",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def calendar(self, ctx):
        """Sends Engineering Unified Calendar 📅"""
        embed = discord.Embed(
            title="Unified Engineering Calendar",
            description=f"[Click here to add our calendar.]({CALENDAR})",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def site(self, ctx):
        """Sends our club website"""
        embed = discord.Embed(
            title="Unified Engineering Calendar",
            description=f"[Click here to view our website.]({WEBSITE})",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(QuickLinks(bot))