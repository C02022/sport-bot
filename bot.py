import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os

from apikeys import *

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

# This is needed so we know that the bot is ready to start receiving commands in our terminal
@client.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game('Yooooooo')) # bot's status to idle/invisible/do not disturb (it defaults to online btw). 'nextcord.game' shows a 'playing' status
    print("The bot is now ready for use")
    print("--------------------------------")

# COG STUFF
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3]) # 'filename[:-3]' removes '.py' at the end of the filenmae of the cog

if __name__ == '__main__':
    for extension in initial_extensions:
        print(f"{extension[5:]} is loaded!")
        bot.load_extension(extension)

if __name__ == "__main__":
    bot.run(SPORT_BOT_TOKEN)