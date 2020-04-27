"""
Shaun {
Notes to consider when programming:
- Try making commands cross server friendly, if not then it can't be helped but you never know
  when you might want the bot on another server
- The server prefix is currentl 'd!' and it would be more hassle to have it as a var so use that for
  commands that don't require developer knowledge
}
Stan {

}
Jess {

}
"""

import discord, time, random, asyncio, re, json, os

os.system("ls")

def has_role(the_message, rolename):
    if discord.utils.get(the_message.guild.roles, name=rolename) in the_message.author.roles:
        return True
    else:
        return False

def get_role(the_message, rolename):
    return discord.utils.get(the_message.guild.roles , name=rolename).id

def embed_field(title, *fields):
    embed = discord.Embed(title=title, colour=discord.Colour(0x0000A0))
    for i in fields:
        embed.add_field(name=i[0], value=i[1])

    return embed

def get_options(option):
    pass

class MyClient(discord.Client):
    async def on_ready(self):
        print('------')
        print(self.user.name)
        print(self.user.id)
        print('good to go!')
        print('------')

    async def on_member_join(member):
        member.add_roles(get_role(member, 'Unidentified'))
        with open("DiscordUsers.json", "r") as file:
            discord_users = json.load(file)

        await update_data(discord_user=member)

        with open("DiscordUsers.json", "w") as file:
            json.dump(discord_users, file, sort_keys=True, indent=4, separators=(',', ': '))

    async def on_message(self, message):
        e_content = message.content


        await update_data(discord_user=message.author)
        await update_experience(discord_user=message.author, exp=random.randint(1, 10), the_message=message)

        def command_error(error_type, permission_needed, bad_command, the_message):
            if error_type == "Permission":
                return embed_field("Bad Command", ["You just used the %s command!"%bad_command, "You are lacking the *minimum* permission of <@&%s>\nThis means that the command was not completed!"%get_role(the_message, permission_needed)])
            elif error_type == "Useage":
                return embed_field("Bad Command", ["You just used the %s command!"%bad_command, "You are using this command incorrectly, please check the useage by checking the bot docs or doing '?help <commandname>'"])

        if re.match(r"^d!\s*(.*)", e_content):
            the_command = re.findall(r"^d!\s*(.*)", e_content)[0]

            # I recommend putting all admin commands here
            if the_command == "quitfm":
                if has_role(the_message=message, rolename="Admin"):
                    await message.channel.send(embed=embed_field("Dangerous Command", ["You just used the quit command!", "This is a dangerous command, it will shut down the bot!\nShutting down..."]))
                    quit()
                else:
                    await message.channel.send(embed=command_error(error_type="Permission", permission_needed="Admin", bad_command="quit", the_message=message))

            # I recommend putting all moderator commands here

            # I recommend putting all global commands here
            if the_command == "myname":
                await message.channel.send(embed=embed_field("Safe Command", ["You just used the myname command!", "Name: {}\nId: {}".format(message.author, message.author.id)]))

            elif the_command.split(" ")[0] == "remind":
                the_command_args = the_command.split(" ")[1:]

                try:
                    await message.channel.send(embed=embed_field("Safe Command", ["You just used the remind command!", "The remind time has been set to %s minutes"%str(float(the_command_args[0])), "After that time has passed you will be reminded the following:", the_command_args[1]]))
                    await asyncio.sleep(float(the_command_args[0])*60)
                    await message.channel.send(embed=embed_field("Reminder!", ["This was a reminder set %s minutes ago!"%str(float(the_command_args[0])), the_command_args[1]]))
                except:
                    await message.channel.send(embed=command_error(error_type="Type", permission_needed="", bad_command="remind", the_message=message))

            elif the_command.split(" ")[0] == "stats":

                with open("DiscordUsers.json", "r") as file:
                    discord_users = json.load(file)

                update_data(message.author.id)

                the_command_args = the_command.split(" ")[1:]

                try:
                    if the_command_args[0] == "leaderboard":
                        pass
                except:
                    await message.channel.send(embed=embed_field("Your Stats!", ["You used the stats command, here are yours!", "**Level**: {}\n**Experience**: {}\n**Id**: {}".format(discord_users[str(message.author.id)]["level"], discord_users[str(message.author.id)]["level"], str(message.author.id))]))

        elif re.match(r"^wd\s*(.*)", e_content):
            pass

        else:
            print("Received Message")

async def update_data(discord_user):
    with open("DiscordUsers.json", "r") as file:
        discord_users = json.load(file)

    print(discord_users[str(discord_user.id)]["exists"] == "true", discord_user.id, discord_users)

    if not discord_users[str(discord_user.id)]["exists"] == "true":
        discord_users[str(discord_user.id)] = {}
        discord_users[str(discord_user.id)]["exists"] = "true"
        discord_users[str(discord_user.id)]["experience"] = 0
        discord_users[str(discord_user.id)]["level"] = 1

    with open("DiscordUsers.json", "w") as file:
        json.dump(discord_users, file, sort_keys=True, indent=4, separators=(',', ': '))

async def update_experience(discord_user, exp, the_message):
    with open("DiscordUsers.json", "r") as file:
        discord_users = json.load(file)

    experience = int(discord_users[str(discord_user.id)]["experience"]) + exp

    starting_level = discord_users[str(discord_user.id)]["level"]
    ending_level = int(experience ** (1/4))

    if starting_level < ending_level:
        await the_message.channel.send(":partying_face: You levelled up to level: %s!"%ending_level)
        discord_users[str(discord_user.id)]["level"] = ending_level

    discord_users[str(discord_user.id)]["experience"] = experience

    with open("DiscordUsers.json", "w") as file:
        json.dump(discord_users, file, sort_keys=True, indent=4, separators=(',', ': '))

client = MyClient()
client.run('NjkwNTAyMTgwOTQ3NjIzOTU2.XqbtOg.Qv0_rRxwQnfNWRrwtRtYSzTYJpQ')
