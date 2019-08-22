import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("hi")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="{} SERVER | {} USER". format(len(client.guilds), len(client.users))))


@client.event
async def on_message(message):
    if message.content.startswith("/회원가입"):
        haewon = message.guild.get_member(int(message.author.id))
        haewonga = discord.utils.get(message.guild.roles, name="회원")
        await haewon.add_roles(haewonga)
        await message.channel.send("권한발급완료")
    



client.run("NjE0MDUwMDM5MTM1ODYyODI0.XV50sg.lGZAUA3TMQ244g9z9TYVH9pLnGk")
