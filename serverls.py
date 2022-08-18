import discord

client = discord.Client()
token = ('NTkwMDIxMDQ0Mjc0OTg3MDI4.G55Uvd.1j5jMHEcNJd0i60FIdkktiKQBWj4c2k7ki7wjM')
@client.event
async def on_connect():
    count = 0
    for guild in client.guilds:
        try:
            count += 1
            print(f'Server:{guild} \n Count:{count}')
        except:
            print("nope")

client.run(token)
