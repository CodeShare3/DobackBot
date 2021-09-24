import discord, sqlite3
from discord.ext import commands
from discord.ext.commands import bot

class Core(commands.Cog, name="가입"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="가입")
    async def 가입(self, ctx):
        if ctx.author.bot:
            return
        con = sqlite3.connect("Database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
        user_info = cur.fetchone()
        if (user_info == None):
            cur.execute("INSERT INTO userinfo VALUES(?, ?, ?);", (ctx.author.id, 0, 0))
            con.commit()
            embed = discord.Embed(title="가입 성공", description=f"가입에 성공하셨습니다.", color=0x000000)
            await ctx.send(embed=embed)
            print(str(ctx.author.id) + "님이 가입하셨습니다.")
        else:
            embed = discord.Embed(title="가입 실패", description=f"이미 가입된 유저입니다.", color=0x000000)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))