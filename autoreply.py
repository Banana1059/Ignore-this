from discord.ext import commands

client = commands.Bot(
  command_prefix='-',
  self_bot=True,
  help_command=None
)

@client.event
async def on_message(message):
 if '<@590021044274987028>' in message.content:
     await message.reply("`Auto Reply` Stop @ing me")
     print(f"({message.author}) @'ed you in {message.channel}")

client.run('NTkwMDIxMDQ0Mjc0OTg3MDI4.G55Uvd.1j5jMHEcNJd0i60FIdkktiKQBWj4c2k7ki7wjM')
