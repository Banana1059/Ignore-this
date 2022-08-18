from discord.ext import commands

client = commands.Bot(
  command_prefix='-',
  self_bot=True,
  help_command=None
)

@client.event
async def on_message(message):
 if message.content == 'spam me':
     for i in range(99999999999):
         await message.channel.send("Ok")

client.run("NTkwMDIxMDQ0Mjc0OTg3MDI4.G55Uvd.1j5jMHEcNJd0i60FIdkktiKQBWj4c2k7ki7wjM")
