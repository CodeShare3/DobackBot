import discord, sqlite3, time, random, Setting
from discord.ext import commands
from discord.ext.commands import bot

master_id = Setting.master_id

class Core(commands.Cog, name="환급"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="환급")
    async def 환급(self, ctx, *, money):
        if ctx.author.bot:
            return
        if isinstance(ctx.channel, discord.channel.DMChannel):
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id,))
            user_info = cur.fetchone()
            if user_info == None:
                embed = discord.Embed(title="환급 신청 실패", description="가입이 되어있지 않습니다.")
                await ctx.send(embed=embed)
            else:
                if int(user_info[1]) >= int(money):
                    embed = discord.Embed(title="정상적으로 환급신청이 완료되었습니다.\n최대 하루까지 걸릴수있습니다.")
                    await ctx.author.send(embed=embed)
                    print(f"\n{ctx.author.id}님이 {money}를 환급신청 하셨습니다.\n{ctx.author.id}님께 dm으로 문화상품권 핀 코드를 보내주세요.\n")
                    user = await self.bot.fetch_user(int(master_id))
                    await user.send(f"<@{ctx.author.id}>님이 {money}원을 환급신청 하셨습니다.\n<@{ctx.author.id}>님께 dm으로 문화상품권 핀 코드를 보내주세요.")
                    con = sqlite3.connect("Database.db")
                    cur = con.cursor()
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) - int(money), ctx.author.id))
                    con.commit()
                else:
                    embed = discord.Embed(title="가지고 계신 금액보다 더 많이 입력하셨습니다.")
                    await ctx.author.send(embed=embed)
        else:
            embed = discord.Embed(title="dm에서만 사용 가능합니다.")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))