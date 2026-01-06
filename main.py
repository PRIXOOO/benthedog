from random import random


import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import time

import random
TOKEN = 'token'
client = commands.Bot(command_prefix='.', help_command=None)
SendN = discord.client
Activer = False
@client.event
async def on_ready():
    print(':)')
Test = 1
Talk = 1        
Journal = 1
players = {}
SendM =  1
Connected = 1 
voice = 0
@client.command(pass_context=True)
async def help(ctx):
    global SendM
    if SendM == 1:
        user = ctx.message.author
        SendM = 0
        embed= discord.Embed(
            title="Ben the Dog", 
            description="get ur Ben in ur server ;)",             
            color=discord.Color.blue()
            )

        embed.set_author(name="Ben the dog", url="https://lelien.com", icon_url="https://cdn.download.it/gen_screenshots/pt-BR/windows/talking-ben/large/image-01-535x535.png")

        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/592621158526255104/FKVURf62_400x400.jpg")

        embed.add_field(name="**Activate Ben(important)**", value="> Just do **`.ben`** for activate Ben(be sure to be inside a channel)", inline=False) 
        embed.add_field(name="**Call Ben**", value="Type  ***`.call`*** if u want to call it,  sand just do again  ***`.call`*** if u want to hang up the phone", inline=True)
        embed.add_field(name="**Newspaper**", value="do ***`.newspaper`*** if u want to open newspaper, do again ***`.newspaper`*** if u want to close it", inline=True)
        await user.send(embed=embed)

        await ctx.message.add_reaction('📧')
        SendM = 1
    # This works ^

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("You can type `.help` for more info", reference=message)
    await client.process_commands(message)




@client.command(pass_context=True)
async def ben(ctx):

    channel = ctx.message.author.voice.channel
    global voice
    global Test
    global Talk
    global Connected

    if not channel:
        await ctx.send("No !")
        return
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        
        await voice.move_to(channel)
        print("il est dans un chat vocale")
    else:
        voice = await channel.connect()
        if Connected == 1:
            Connected = 0
            await ctx.send("**Ben** is activated (type `.help` for commands)")
            @client.event
            async def on_message(message):
                    source = FFmpegPCMAudio('BenM.mp3')
                    global Talk
                    global Journal
                    global voice
                    if message.content == ".call":
                        if Journal == 1:
                            if Talk == 0 :
                                source = FFmpegPCMAudio('BenM.mp3')
                                print("Acroche")
                                voice.play(source)
                                await ctx.send("Bye")   
                                time.sleep(3)
                                Talk = 1 
                            else :
                                source1 = FFmpegPCMAudio('Ben.mp3')    
                                Talk = 0
                                print("Decroche")
                                voice.play(source1)
                                time.sleep(4)
                                await ctx.send("**Ben ?**(type on the chat)")
                                await ctx.send("https://tenor.com/view/phone-call-talking-ben-gif-14574349")
                    
                    if message.content == ".newspaper":
                        if Talk == 1:
                            if Journal == 1:
                                Journal = 0
                                OJournal = FFmpegPCMAudio('OpenJournal.wav')
                                voice.play(OJournal)
                                await ctx.send("*(Ben opens the newspaper)*")
                                time.sleep(4)
                                Sound1 = FFmpegPCMAudio('BenJ.mp3')
                                voice.play(Sound1)
                            else:
                                await ctx.send("*(Ben close the newspaper)*")
                                time.sleep(1)
                                voice.stop()
                                Journal = 1
                                CJournal = FFmpegPCMAudio('closejournal.wav')
                                voice.play(CJournal)
                                time.sleep(3)
                    if client.user.mentioned_in(message):
                        await message.channel.send("You can type `.help` for more info", reference=message)
                        await client.process_commands(message)
                    if message.content == ".ben":
                            channel1 = ctx.message.author.voice.channel
                            if not channel1:
                                await ctx.send("No !")
                                return
                            if voice and voice.is_connected():

                                 await voice.move_to(channel1)
                                 print("il est dans un chat vocale")
                            else:
                                 await channel1.connect()
                                 voice = get(client.voice_clients, guild=ctx.guild)
                            if not channel:
                                await ctx.send("No !")
                                return
                    
                    if message.content == ".leave":
                        Leave = ctx.voice_client
                        await Leave.disconnect()



                    if message.channel.id is not ctx.channel.id:
                        return
                    else:
                        if message.author != client.user:
                            if Journal == 1:
                                if Talk == 0:
                                    No = FFmpegPCMAudio('No.mp3')
                                    Yes = FFmpegPCMAudio('Yes.mp3')
                                    Haa = FFmpegPCMAudio('Haa.mp3')
                                    Huu = FFmpegPCMAudio('Huu.mp3')
                                    x =random.randrange(1,5)
                                    if not voice.is_playing():
                                        if x == 3 : 
                                            voice.play(Haa)
                                            await ctx.send("Hahahaa")

                            
                                        if x == 2 :
                                            voice.play(No)
                                            await ctx.send("No :pensive:")

                                        if x == 4 : 
                                            voice.play(Huu)
                                            await ctx.send("Huuu :triumph:")

                                        if x == 1 :
                                            voice.play(Yes)
                                            await ctx.send("Yes !")

        else:
            await ctx.send("**Ben** is desactivated (type .help for commands)")
            voice = await channel.disconnect()
          
        


client.run(TOKEN)
