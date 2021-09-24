import discord, sqlite3, time, random
from discord.ext import commands
from discord.ext.commands import bot

class Core(commands.Cog, name="도박"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="도박")
    async def 도박(self, ctx, *, money):
        if ctx.author.bot:
            return
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id,))
            user_info = cur.fetchone()
            if user_info == None:
                embed = discord.Embed(title="도박 실패", description="가입이 되어있지 않습니다.")
                await ctx.send(embed=embed)
            else:
                if 1000 <= int(money):
                    if int(money) <= int(user_info[1]):
                        embed = discord.Embed(title="주사위 굴리는중...", description="1~3 : 0배\n4~5 : 2배\n6 : 3배")
                        m = await ctx.send(embed=embed)
                        time.sleep(5)
                        wntkdnl = random.choice(["1", "1", "1", "1", "2", "2", "2", "3", "3", "4", "4", "5", "5", "6"])
                        if wntkdnl == "1":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) - int(money), ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈을 전부 잃으셨습니다.")
                            await m.edit(embed=embed)
                        if wntkdnl == "2":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) - int(money), ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈을 전부 잃으셨습니다.")
                            await m.edit(embed=embed)
                        if wntkdnl == "3":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) - int(money), ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈을 전부 잃으셨습니다.")
                            await m.edit(embed=embed)
                        if wntkdnl == "4":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) + int(money), ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈이 2배가 되었습니다.")
                            await m.edit(embed=embed)
                        if wntkdnl == "5":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) + int(money), ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈이 2배가 되었습니다.")
                            await m.edit(embed=embed)
                        if wntkdnl == "6":
                            con = sqlite3.connect("Database.db")
                            cur = con.cursor()
                            cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(user_info[1]) + int(money) * 3, ctx.author.id))
                            con.commit()
                            embed = discord.Embed(description=wntkdnl + "가 나왔습니다.\n배팅하신 돈이 3배가 되었습니다.")
                            await m.edit(embed=embed)
                    else:
                        embed = discord.Embed(title="도박 실패", description="가지고 계신 돈보다 더 많이 배팅하셨습니다.")
                        await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="도박 실패", description="1000원 이상의 돈을 배팅해주세요.")
                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))