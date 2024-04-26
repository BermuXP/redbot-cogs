import discord
import requests
import json
from typing import Any, Dict, Union
import httpx
from redbot.core import app_commands, commands

rootUrl = "https://gameinfo-ams.albiononline.com/api/gameinfo/"

class Albion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(albionuser="Get the albion user's info.")
    async def albionuser(self, interaction: discord.Interaction, username: str):
        x = requests.get(rootUrl + "search?q=" + username)
        parsed_data = json.loads(x.text)
        if parsed_data["players"]:
            player = parsed_data["players"][0]
            embed = discord.Embed(
                title=player["Name"],
                description="",
                color=0x00FFFF
            )
            embed.add_field(name="Kill Fame", value=player['KillFame'], inline=False)
            embed.add_field(name="Death Fame", value=player['DeathFame'], inline=False)
            embed.add_field(name="Guild", value=player["GuildName"], inline=False)
            await interaction.respond(embed=embed)
        else:
            await interaction.respond("User not found")
