import discord
import asyncio
client = discord.Client()

@client.event
async def broadcast():
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == ("idk"):
                ctx.send("e")
asyncio.run(broadcast())

client.run("NTkwMDIxMDQ0Mjc0OTg3MDI4.GZtP70.iHb-KpeCOIjZpgrEELQOikLR3IgDmb_aYzpSEc")
