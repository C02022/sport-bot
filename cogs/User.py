import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Role

from apikeys import *

class User(nextcord.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command that allows the user to select what sport role they would like to be given for respective pings & such
    @nextcord.slash_command(name = "sport roles", description = "Select what sport role to be given", guilds_ids=[TEST_SERVER_ID])
    async def sport_roles(self, interaction : Interaction):
        # IDEA: Perhaps create an embed like the images you pinned in the 'bot-reference' channel and then just have the bot react 
        # to the embed with the sports before sending it in the discord channel
        pass

        
def setup(bot):
    bot.add_cog(User(bot))