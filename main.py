#import modules

print('[INFO] Importing MODULES')
import discord
from discord.ext import commands
import json
import time


time.sleep(0.5) 


print('[INFO] Loading DATA')
with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]

time.sleep(0.5) 


print('[INFO] LOADING BOT')
client = commands.Bot(command_prefix = '-',intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print("[Connected]")
    activity = discord.Game(name="discord.gg/devscafe", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

time.sleep(0.5) 


print('[INFO] LOADING EVENTS')


@client.event 
async def on_member_join(member):
	guild = client.get_guild(842076879749120021)
	channel = client.get_channel(842076879749120025) #MUST BE A VOICE CHANNEL
	await channel.edit(name="Members : "+ f" {guild.member_count}")



time.sleep(0.5) 

print('[INFO] CONNECTING TO API')

client.run(token)
