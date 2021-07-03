# Imports
import glob
import os
import discord
import youtube_dl
import random
import json
import asyncio
from time import sleep
from discord.ext import commands
from discord import Color


# Class to hold functions for Fishing commands
class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help list
    @commands.command()
    async def eco(self, ctx):
        if await self.channel_check(ctx) is True:
            await self.create_fisher(ctx.author)
            cmds = ["```!cast - Cast your line out to the ocean",
                    "\n!total - Shows the total amount of fish you've caught",
                    "\n!pb - Shows the best fish you've caught",
                    "\n!best - Shows the best fish in the server",
                    "\n!last - Shows the last fish you've caught",
                    "\n!classes - Shows list of possible class rankings for fish```",
                    ]
            await ctx.send('\n'.join(cmds))
        else:
            await ctx.send(f"Hey dummy put that command in the <#843892871396720700> channel.")

            # Add fishers to list

        async def create_citizen(self, context):
            case = True
            users = await self.get_eco_data()
            async for member in context.guild.fetch_members(limit=None):
                if str(member.id) in users:
                    case = True
                else:
                    users[str(member.id)] = {}
                    users[str(member.id)]["username"] = str(member)
                    users[str(member.id)]["wallet"] = 100
                    users[str(member.id)]["deaths"] = 0
                    users[str(member.id)]["jails"] = 0
                    users[str(member.id)]["fudges"] = 0
                    users[str(member.id)]["armor"] = 0

                with open("C:/Python/BerdBot/json/economy.json", "w") as f:
                    json.dump(users, f, indent=4)
                case = False

    # Get bank info
    async def get_fishing_data(self):
        with open("C:/Users/You/Documents/MEGA/PyCharm/Projects/BerdBot/json/economy.json", "r") as f:
            users = json.load(f)
        return users

    # Make sure commands are in the bot channel
    async def channel_check(self, ctx):
        if ctx.message.channel.name == "bot-spam-🔌" or ctx.message.channel.name == "bot-test-🔌":
            return True
        else:
            return False


# Setup function for cog
def setup(client):
    client.add_cog(Economy(client))
