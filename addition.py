import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def brainrot_mode(ctx):
    await ctx.send(f'ngl imo ts pmo fr🥀')

@bot.command()
async def quiz_country1(ctx):
    await ctx.send(f"Mention 1 country that is communist and the most populated.")

@bot.command()
async def quiz_country2(ctx):
    await ctx.send(f"What continent is trinidad and tobago located?")

@bot.command()
async def quiz_food_origin1(ctx):
    await ctx.send(f"which island in Indonesia does papeda came from?")

@bot.command()
async def quiz_food_origin2(ctx):
    await ctx.send(f"what country does Enchiladas came from")

@bot.command()
async def quiz_math1(ctx):
    await ctx.send(f"simplify 8x + 4 + 3(2x-3)")

@bot.command()
async def quiz_math2(ctx):
    await ctx.send(f"factorise 4x^2 - 23x + 15")

@bot.command()
async def have_you_eaten(ctx):
    await ctx.send(f"I dont eat im a bot i eat air")

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTM2ODIwNzM3MDAwMTU4MDA0Mw.Gtz6Td.ug7zx4x1kzejfcihIYvumV7TUEPj_A9UuMTQz8")
