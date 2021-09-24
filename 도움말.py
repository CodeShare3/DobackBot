import discord, sqlite3, time, random
from discord.ext import commands
from discord.ext.commands import bot

class Core(commands.Cog, name="도움말"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="도움말")
    async def 도움말(self, ctx):
        if ctx.author.bot:
            return
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            embed = discord.Embed(description="!가입 : 가입하기\n!충전 : 문화상품권 충전\n!도박 : 랜덤 주사위 도박\n!환급 : 문화상품권 환급 신청\n!잔액조회 : 유저 잔액 조회")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))