import discord, asyncio
token = 'ODAzNDg3MDYxNjAwNTAxNzYx.YA-fow.7wG1XFdh_5oZBYchJehMDAoki0g'
client = discord.Client()
@client.event
async def on_ready():
    print('로그인 되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message):
    if message.content == "타이머":
        await asyncio.sleep(1740)
        await message.channel.send(f"{message.author.mention}, 다음 경뿌까지 1분 남았습니다.")
    
    if message.content == "철민":
        await message.channel.send("등신")

client.run(token)