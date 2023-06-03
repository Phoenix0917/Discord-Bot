import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv('tokens.env')
token = os.getenv('DISCORD_TOKEN') # bots identifier token
GUILD_NAME = os.getenv('DISCORD_GUILD') # guild name this particular instance will go to
roleAssignMsgID = int(os.getenv('ROLE_ASSIGNER'))
SONG_LIST_CHANNEL_ID = int(os.getenv('SONG_LIST_CHANNEL'))

listSongs = []
numSongs = 0
pointSongs = 0
msgSongs = "unassigned"

intents = discord.Intents.all()
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    #roleAssignTxt = await guild.fetch_message(886769077010456646)
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    for guild in bot.guilds: # list of all guilds bot has access to
        if guild.name == GUILD_NAME: # select one guild I have programmed in env file
            break
    roleToAssign = discord.utils.get(guild.roles, name='Member')
    await member.add_roles(roleToAssign)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == roleAssignMsgID:
        if payload.emoji.name == '🎸':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Guitarist') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role
        elif payload.emoji.name == '🐟':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Bassist') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role
        elif payload.emoji.name == '🎙️':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Vocalist') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role
        elif payload.emoji.name == '🥁':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Drummer') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role
        elif payload.emoji.name == '🎹':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Keyboardist') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role
        elif payload.emoji.name == '🎷':           
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToAssignRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that sent this reaction
            roleToAssign = discord.utils.get(guild.roles, name='Saxophonist') # find the role that is associated with this reaction
            await memberToAssignRole.add_roles(roleToAssign) # assign the role

    global listSongs
    global numSongs
    global pointSongs
    global msgSongs
    try: 
        if payload.message_id == msgSongs.id:
            for role in payload.member.roles:
                if role.name == "Officers":
                    if payload.emoji.name == '⬇️':
                        if pointSongs == numSongs:
                            pointSongs = 0
                        else:
                            pointSongs = pointSongs + 1
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)

                    if payload.emoji.name == '⬆️':
                        if pointSongs == 0:
                            pointSongs = numSongs
                        else:
                            pointSongs = pointSongs - 1
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)

                    if payload.emoji.name == '🔁':
                        listSongs[pointSongs]['Status'] = "Try Again"
                        if pointSongs == numSongs:
                            pointSongs = 0
                        else:
                            pointSongs = pointSongs + 1
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)

                    if payload.emoji.name == '☑️':
                        listSongs[pointSongs]['Status'] = "Completed"
                        if pointSongs == numSongs:
                            pointSongs = 0
                        else:
                            pointSongs = pointSongs + 1
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)

                    if payload.emoji.name == '⏯️':
                        listSongs[pointSongs]['Status'] = "In Progress"
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)

                    if payload.emoji.name == '❌':
                        listSongs[pointSongs]['Status'] = "Not Started"
                        listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                        count = 0
                        for dictionary in listSongs:
                            if pointSongs == count:
                                listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            else:
                                listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                            count = count + 1
                        listMessage = "```" + listMessage + "```"
                        await msgSongs.edit(content=listMessage)
                        await msgSongs.remove_reaction(payload.emoji, payload.member)
                elif role.name == "Member":
                    await msgSongs.remove_reaction(payload.emoji, payload.member)
    except:
        return

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == roleAssignMsgID:
        if payload.emoji.name == '🎸':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Guitarist') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

        if payload.emoji.name == '🐟':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Bassist') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

        if payload.emoji.name == '🎙️':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Vocalist') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

        if payload.emoji.name == '🥁':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Drummer') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

        if payload.emoji.name == '🎹':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Keyboardist') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

        if payload.emoji.name == '🎷':
            for guild in bot.guilds: # list of all guilds bot has access to
                if guild.name == GUILD_NAME: # select one guild I have programmed in env file
                    break
            memberToRemoveRole = discord.utils.get(guild.members, id=payload.user_id) # find the member that removed this reaction
            roleToRemove = discord.utils.get(guild.roles, name='Saxophonist') # find the role that is associated with this reaction
            await memberToRemoveRole.remove_roles(roleToRemove) # remove the role

@bot.command(name = 'add_list')
async def add_list(ctx):
    channel = bot.get_channel(SONG_LIST_CHANNEL_ID)
    if ctx.channel.id == channel.id: # checks that this is the songs list channel
        if len(ctx.message.attachments) == 1: # checks that exactly one attatchment is on the message (I think each message can have a maximum of one attatchment, others are in other messages)
            if ctx.message.attachments[0].content_type == 'text/plain; charset=utf-8': # checks that list is in .txt format
                # load txt document up
                await ctx.message.attachments[0].save("songs.txt")
                file = open("songs.txt", "r")

                # cleans out all old messages (lists of songs)
                await channel.purge(limit=100) 

                # defines global variables to assign and print later
                global listSongs
                listSongs = []
                global numSongs
                numSongs = 0
                global pointSongs
                pointSongs = 0
                global msgSongs
                msgSongs = "unassigned"

                # creates listSongs 
                while True:
                    nameSong = file.readline()
                    nameSong = nameSong.replace("\n", "")
                    if ("" == nameSong): # EOF detected
                        numSongs = numSongs - 1
                        break
                    listSongs.append({})
                    if len(nameSong) > 28:
                        nameSong = nameSong[0:25] + '...'
                    listSongs[numSongs]['Name'] = nameSong
                    listSongs[numSongs]['Status'] = "Not Started"
                    numSongs = numSongs + 1

                # formats table to output initial version of list
                listMessage = "".ljust(3) + "Songs".ljust(30) + "Status".ljust(20) + '\n' + '--------------------------------------------'.ljust(60) + '\n'
                first = True
                for dictionary in listSongs:
                    if first == True:
                        listMessage = listMessage + " >".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                    else:
                        listMessage = listMessage + "".ljust(3) + dictionary['Name'].ljust(30) + dictionary['Status'].ljust(20) + '\n'
                    first = False
                listMessage = "```" + listMessage + "```"
                msgSongs = await channel.send("loading...")
                await msgSongs.edit(content=listMessage)

                # adds reaction buttons to text
                reactions = ['⬆️', '⬇️', '⏯️', '☑️', '🔁', '❌']
                for emoji in reactions:
                    await msgSongs.add_reaction(emoji)

            else:
                await channel.send("Please only upload a file type of .txt")
        else:
            await channel.send("Please attatch exactly one file to the command message")



bot.run(token)


# need env for each server bot is on and for each bot


# client is bot, guild is everything in server