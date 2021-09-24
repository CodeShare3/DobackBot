import discord, sqlite3
from discord.ext import commands
from discord.ext.commands import bot

class Core(commands.Cog, name="잔액"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="잔액")
    async def 잔액(self, ctx):
        if ctx.author.bot:
            return
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id,))
            user_info = cur.fetchone()
            if user_info == None:
                embed = discord.Embed(title="잔액 조회 실패", description="가입이 되어있지 않습니다.")
                await ctx.send(embed=embed)
            else:
                try:
                    embed = discord.Embed(title="dm을 확인해주세요.")
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title=f"{ctx.author.name}님의 잔액", description=f"잔액: {user_info[1]}원")
                    await ctx.author.send(embed=embed)
                except:
                    embed = discord.Embed(title=f"잔액 조회 실패", description=f"DM을 차단하셨거나 메시지 전송 권한이 없습니다.")
                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))