import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('MTA4ODEwNjU1NDIyNzY4NzQ3NQ.GU8lxv.2kRYtB_L21cjupckdcAoeSe3q0qEh7S_dB-pY8'))