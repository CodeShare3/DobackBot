import discord, sqlite3, Setting, selenium, asyncio
from discord.ext import commands
from discord.ext.commands import bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
from bs4 import BeautifulSoup

culid = Setting.culid
password = Setting.culpw
fees = Setting.fees
masterid = Setting.master_id


class Core(commands.Cog, name="충전"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="충전")
    async def 충전(self, ctx):
        if ctx.author.bot:
            return
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id,))
            user_info = cur.fetchone()
            if user_info == None:
                embed = discord.Embed(title="충전 실패", description="가입이 되어있지 않습니다.")
                await ctx.send(embed=embed)
            else:
                options = webdriver.ChromeOptions()
                options.headless = True
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                options.add_argument("headless")
                driver = webdriver.Chrome(options=options)
                driver.get('https://m.cultureland.co.kr/mmb/loginMain.do?agent_url=%2Fcsh%2FcshGiftCard.do')
                driver.find_element_by_xpath('//*[@id="txtUserId"]').send_keys(culid)
                try:
                    embed = discord.Embed(title="핀 코드 입력", description="핀 코드를 `-` 포함하여 입력해주세요.")
                    await ctx.author.send(embed=embed)
                    embed = discord.Embed(title="충전 신청 완료", description="dm을 확인해주세요.")
                    await ctx.send(embed=embed)
                except:
                    embed = discord.Embed(title="충전 실패", description="DM을 차단하셨거나 메시지 전송 권한이 없습니다.")
                    await ctx.send(embed=embed)
                    return None

                def check(msg):
                    return (isinstance(msg.channel, discord.channel.DMChannel) and (
                                len(msg.content) == 21 or len(msg.content) == 19) and (ctx.author.id == msg.author.id))

                try:
                    pin = await self.bot.wait_for("message", timeout=60, check=check)
                except asyncio.TimeoutError:
                    embed = discord.Embed(title="충전 실패", description="시간이 초과되었습니다.")
                    await ctx.author.send(embed=embed)
                    driver.close()
                    pass
                    return None
                pw_number = 0
                driver.find_element_by_xpath('//*[@id="passwd"]').click()
                try:
                    while True:
                        try:
                            if password[pw_number] == "~" or password[pw_number] == "!" or password[pw_number] == "@" or \
                                    password[pw_number] == "#" or password[pw_number] == "+":
                                try:
                                    if password[pw_number] == "~":
                                        driver.find_element_by_xpath(f'//img[@alt="물결표시"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "!":
                                        driver.find_element_by_xpath(f'//img[@alt="느낌표"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "@":
                                        driver.find_element_by_xpath(f'//img[@alt="골뱅이"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "#":
                                        driver.find_element_by_xpath(f'//img[@alt="샾"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "~":
                                        driver.find_element_by_xpath(f'//img[@alt="더하기"]').click()
                                        pw_number = pw_number + 1
                                except:
                                    driver.find_element_by_xpath(f'//img[@alt="특수키"]').click()
                                    if password[pw_number] == "~":
                                        driver.find_element_by_xpath(f'//img[@alt="물결표시"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "!":
                                        driver.find_element_by_xpath(f'//img[@alt="느낌표"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "@":
                                        driver.find_element_by_xpath(f'//img[@alt="골뱅이"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "#":
                                        driver.find_element_by_xpath(f'//img[@alt="샾"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "~":
                                        driver.find_element_by_xpath(f'//img[@alt="더하기"]').click()
                                        pw_number = pw_number + 1
                            else:
                                try:
                                    if password[pw_number] == "Q" or password[pw_number] == "W" or password[
                                        pw_number] == "E" or \
                                            password[pw_number] == "R" or password[pw_number] == "T" or password[
                                        pw_number] == "Y" or password[pw_number] == "U" or password[pw_number] == "I" or \
                                            password[
                                                pw_number] == "O" or password[pw_number] == "P" or password[
                                        pw_number] == "A" or \
                                            password[
                                                pw_number] == "S" or password[pw_number] == "D" or password[
                                        pw_number] == "F" or \
                                            password[
                                                pw_number] == "G" or password[pw_number] == "H" or password[
                                        pw_number] == "J" or \
                                            password[
                                                pw_number] == "K" or password[pw_number] == "L" or password[
                                        pw_number] == "Z" or \
                                            password[
                                                pw_number] == "X" or password[pw_number] == "C" or password[
                                        pw_number] == "V" or \
                                            password[
                                                pw_number] == "B" or password[pw_number] == "N" or password[
                                        pw_number] == "M":
                                        driver.find_element_by_xpath(f'//img[@alt="대문자{password[pw_number]}"]').click()
                                        pw_number = pw_number + 1
                                    if password[pw_number] == "q" or password[pw_number] == "w" or password[
                                        pw_number] == "e" or \
                                            password[pw_number] == "r" or password[pw_number] == "t" or password[
                                        pw_number] == "y" or password[pw_number] == "u" or password[pw_number] == "i" or \
                                            password[
                                                pw_number] == "o" or password[pw_number] == "p" or password[
                                        pw_number] == "a" or \
                                            password[
                                                pw_number] == "s" or password[pw_number] == "d" or password[
                                        pw_number] == "f" or \
                                            password[
                                                pw_number] == "g" or password[pw_number] == "h" or password[
                                        pw_number] == "j" or \
                                            password[
                                                pw_number] == "k" or password[pw_number] == "l" or password[
                                        pw_number] == "z" or \
                                            password[
                                                pw_number] == "x" or password[pw_number] == "c" or password[
                                        pw_number] == "v" or \
                                            password[
                                                pw_number] == "b" or password[pw_number] == "n" or password[
                                        pw_number] == "m":
                                        driver.find_element_by_xpath(f'//img[@alt="{password[pw_number]}"]').click()
                                        pw_number = pw_number + 1
                                except:
                                    driver.find_element_by_xpath(f'//img[@alt="특수키"]').click()
                                    if password[pw_number] == "Q" or password[pw_number] == "W" or password[
                                        pw_number] == "E" or \
                                            password[pw_number] == "R" or password[pw_number] == "T" or password[
                                        pw_number] == "Y" or password[pw_number] == "U" or password[pw_number] == "I" or \
                                            password[
                                                pw_number] == "O" or password[pw_number] == "P" or password[
                                        pw_number] == "A" or \
                                            password[
                                                pw_number] == "S" or password[pw_number] == "D" or password[
                                        pw_number] == "F" or \
                                            password[
                                                pw_number] == "G" or password[pw_number] == "H" or password[
                                        pw_number] == "J" or \
                                            password[
                                                pw_number] == "K" or password[pw_number] == "L" or password[
                                        pw_number] == "Z" or \
                                            password[
                                                pw_number] == "X" or password[pw_number] == "C" or password[
                                        pw_number] == "V" or \
                                            password[
                                                pw_number] == "B" or password[pw_number] == "N" or password[
                                        pw_number] == "M":
                                        try:
                                            driver.find_element_by_xpath(
                                                f'//img[@alt="대문자{password[pw_number]}"]').click()
                                            pw_number = pw_number + 1
                                        except:
                                            driver.find_element_by_xpath(f'//img[@alt="쉬프트"]').click()
                                            driver.find_element_by_xpath(
                                                f'//img[@alt="대문자{password[pw_number]}"]').click()
                                            pw_number = pw_number + 1
                                    if password[pw_number] == "q" or password[pw_number] == "w" or password[
                                        pw_number] == "e" or \
                                            password[pw_number] == "r" or password[pw_number] == "t" or password[
                                        pw_number] == "y" or password[pw_number] == "u" or password[pw_number] == "i" or \
                                            password[
                                                pw_number] == "o" or password[pw_number] == "p" or password[
                                        pw_number] == "a" or \
                                            password[
                                                pw_number] == "s" or password[pw_number] == "d" or password[
                                        pw_number] == "f" or \
                                            password[
                                                pw_number] == "g" or password[pw_number] == "h" or password[
                                        pw_number] == "j" or \
                                            password[
                                                pw_number] == "k" or password[pw_number] == "l" or password[
                                        pw_number] == "z" or \
                                            password[
                                                pw_number] == "x" or password[pw_number] == "c" or password[
                                        pw_number] == "v" or \
                                            password[
                                                pw_number] == "b" or password[pw_number] == "n" or password[
                                        pw_number] == "m":
                                        try:
                                            driver.find_element_by_xpath(f'//img[@alt="{password[pw_number]}"]').click()
                                            pw_number = pw_number + 1
                                        except:
                                            driver.find_element_by_xpath(f'//img[@alt="쉬프트"]').click()
                                            driver.find_element_by_xpath(f'//img[@alt="{password[pw_number]}"]').click()
                                            pw_number = pw_number + 1
                                try:
                                    if password[pw_number] == "1" or password[pw_number] == "2" or password[
                                        pw_number] == "3" or \
                                            password[pw_number] == "4" or password[pw_number] == "5" or password[
                                        pw_number] == "6" or password[pw_number] == "7" or password[pw_number] == "8" or \
                                            password[
                                                pw_number] == "9" or password[pw_number] == "0":
                                        driver.find_element_by_xpath(f'//img[@alt="{password[pw_number]}"]').click()
                                        pw_number = pw_number + 1
                                except:
                                    if password[pw_number] == "1" or password[pw_number] == "2" or password[
                                        pw_number] == "3" or \
                                            password[pw_number] == "4" or password[pw_number] == "5" or password[
                                        pw_number] == "6" or password[pw_number] == "7" or password[pw_number] == "8" or \
                                            password[pw_number] == "9" or password[pw_number] == "0":
                                        driver.find_element_by_xpath(f'//img[@alt="특수키"]').click()
                                        driver.find_element_by_xpath(f'//img[@alt="{password[pw_number]}"]').click()
                                        pw_number = pw_number + 1
                        except IndexError:
                            driver.find_element_by_xpath(f'//img[@alt="입력완료"]').click()
                            driver.find_element_by_class_name("btn_block").click()
                            pin1 = pin.content[0:4]
                            pin2 = pin.content[5:9]
                            pin3 = pin.content[10:14]
                            pin4 = pin.content[15:21]
                            driver.find_element_by_name("scr11").send_keys(pin1)
                            driver.find_element_by_name("scr12").send_keys(pin2)
                            driver.find_element_by_name("scr13").send_keys(pin3)
                            driver.find_element_by_name("scr14").click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[0]}"]').click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[1]}"]').click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[2]}"]').click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[3]}"]').click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[4]}"]').click()
                            driver.find_element_by_xpath(f'//img[@alt="{pin4[5]}"]').click()
                            driver.find_element_by_xpath('//*[@id="btnCshFrom"]').click()
                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                            dom = etree.HTML(str(soup))
                            driver.close()
                            cndwjsduqn = dom.xpath('//*[@id="wrap"]/div[3]/section/div/table/tbody/tr/td[3]/b')[0].text
                            cndwjsrmador = dom.xpath('//*[@id="wrap"]/div[3]/section/dl/dd')[0].text
                            if cndwjsduqn == "이미 등록된 문화상품권" or cndwjsduqn == "등록제한(10번 등록실패)" or cndwjsduqn == "상품권 번호 불일치":
                                embed = discord.Embed(title="충전 실패", description=cndwjsduqn, color=0x000000)
                                await ctx.author.send(embed=embed)
                                print(str(ctx.author.id) + "님이 충전을 실패하셨습니다.")
                            else:
                                cndwjsrmador = cndwjsrmador.split("원")[0]
                                try:
                                    cndwjsrmador_fees = int(cndwjsrmador) / 100 * int(fees)
                                except ValueError:
                                    cndwjsrmador_1 = cndwjsrmador.split(",")[0]
                                    cndwjsrmador_2 = cndwjsrmador.split(",")[1]
                                    cndwjsrmador_fees = int(str(cndwjsrmador_1) + str(cndwjsrmador_2)) / 100 * int(fees)
                                con = sqlite3.connect("Database.db")
                                cur = con.cursor()
                                cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id,))
                                money = cur.fetchone()
                                con = sqlite3.connect("Database.db")
                                cur = con.cursor()
                                cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;",(int(cndwjsrmador_fees) + int(money[1]), ctx.author.id))
                                con.commit()
                                embed = discord.Embed(title="충전 성공")
                                embed.add_field(name="충전 금액", value=str(cndwjsrmador_fees + "원"), inline=False)
                                embed.add_field(name="잔액", value=str(int(cndwjsrmador_fees) + int(money[1]) + "원"))
                                await ctx.author.send(embed=embed)
                                print(str(ctx.author.id) + "님이 " + cndwjsrmador_fees + "원을 충전하셨습니다.")
                            break
                except:
                    embed = discord.Embed(title="충전 실패", description="일시적인 오류입니다.")
                    await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))