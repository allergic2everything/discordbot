#imports
import discord 
from dotenv import load_dotenv
from discord.ext import commands 
import os

#loading token 
load_dotenv()

TOKEN = os.getenv('TOKEN')

#bot creation 
intents = discord.Intents.default()
intents.message_content = True

#need this to do a command
bot = commands.Bot(command_prefix="$$", intents=intents)




#class
class SimpleView(discord.ui.View) :
    @discord.ui.button(label="heyy") 
    async def hello (self, interaction : discord.Interaction, button: discord.ui.Button) :
        await interaction.response.send_message("hello world")



#_____________________________________
def add(a, b) : 
    return a + b

def subtract(a, b) : 
    return a - b

def multiply (a, b) :
    return a*b

def divide (a, b) : 
    return a/b 

def goodbye () :
    return "Goodbyeee"
#_____________________________________
# calculator function
@bot.command()
async def calc(ctx, arg1, operation, arg2) :
    a = int(arg1)
    b = int(arg2)
    if operation == "add" : 
        await ctx.send(add(a, b))
    if operation == "subtract" : 
        await ctx.send(subtract(a, b))
    if operation == "multiply" : 
        await ctx.send(multiply(a, b))
    if operation == "divide" : 
        await ctx.send(divide(a, b))
#_____________________________________
@bot.command() 
async def button(ctx):
    #a = int(num1)
   # b = int(num2) 
    view = SimpleView() 

    await ctx.send(view=view) 

@bot.command() 
async def gbye(ctx) : 
    await ctx.send(goodbye())


bot.run(TOKEN)
