import discord
import asyncio
import os

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
        await message.channel.send("권한발급완료했습니다.")
        be = discord.utils.get(message.guild.roles, name="비회원")
        await be.remove_roles(be)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
