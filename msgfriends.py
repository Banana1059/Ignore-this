import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('Just ignore this message, im testing my selfbot agian.')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.friends}")
client.run('NTkwMDIxMDQ0Mjc0OTg3MDI4.G55Uvd.1j5jMHEcNJd0i60FIdkktiKQBWj4c2k7ki7wjM')
