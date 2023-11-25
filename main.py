import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents) 

@bot.command()
async def пинг(ctx):
    await ctx.send('понг')

@bot.command()
async def инвайт(ctx):
    await ctx.send('ссылка на наше логово: https://discord.gg/8bfGAp7hqE (только крысям всяким не показывай)')

@bot.command()
async def крыса(ctx, probably_rats: commands.Greedy[discord.Member]):
    for mb_rat in probably_rats:
        print(mb_rat)
        name = mb_rat.name.lower()
        if name.find("rat") != -1 or name.find("крыс") != -1:
            await ctx.send('тревога! крысь ' + name + ' обнаружена!')
        else:
            await ctx.send(name + ' вроде как не крысь')

bot.run('[ДАННЫЕ УДАЛЕНЫ]')
