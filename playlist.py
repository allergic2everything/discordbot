import discord
from dotenv import load_dotenv
from discord.ext import commands 
import os 
import requests
import json 
import api 

load_dotenv() 
TOKEN = os.getenv("TOKEN")

intents = discord.Inteents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="$$", intents=intents)

#call api function to get data 
data = api.get_data("https://api.deezer.com/https:/deezer.page.link/PCfwyvu8PGTsteSEA")

@bot.command()
async def play(ctx) : 
    play_response = requests.get(data) 
    play = play_response.text

    await ctx.send(play) 
