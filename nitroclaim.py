import discord
import requests
import json

token = 'NTkwMDIxMDQ0Mjc0OTg3MDI4.GZtP70.iHb-KpeCOIjZpgrEELQOikLR3IgDmb_aYzpSEc'

client = discord.Client()

@client.event
async def on_ready():
    print('Online')

@client.event
async def on_message(message):
    if message.content.startswith("https://discord.gift/" + str(13)):
         """
         make it store the code after the discord.gift/ part, but note most 
         gifts come in the https://discord.gift/ format, you should either use 
         regex for this opertaion or just set two variables so if the message 
         content includes https and discord.gift it stores it as a different 
         variable.
         """
         redeemheaders = {
         'Authorization': token, #dont replace this.
         'content-type': 'application/json',
         'payment_source_id': 'null'
         }
         r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ codevariable + '/redeem', headers=redeemheaders)
         r = r.text.json()
         print(r)


client.run(token)
