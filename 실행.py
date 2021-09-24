try:
    import discord, Setting, os, sqlite3
    from discord.ext import commands

    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        pass

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(Setting.token)
except:
    pass