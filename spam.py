import discord, asyncio

from discord.ext import commands

import random

message = "speak"

token = "NTkwMDIxMDQ0Mjc0OTg3MDI4.G55Uvd.1j5jMHEcNJd0i60FIdkktiKQBWj4c2k7ki7wjM"

#Bot prefix, like ?help

prefix = "&"

#Prefix

client = discord.Client()

client = commands.Bot(command_prefix=prefix,self_bot=True)

#Farm

@client.command(name='start', aliases=['spam'])

async def _fish_dank(ctx): # b'\xfc'

    await ctx.message.delete()

    count = 0

    while True:

        try:

            count += 1

            await ctx.send(message,count)


            print(f'[AUTO-SPAM] Message number: {count} sent')

        except Exception as e:

            print(f"[ERROR]: {e}")

           

#onReady

@client.event

async def on_ready():

	print(f"Logged in. Write {prefix}start to begin!")

client.run(token)

