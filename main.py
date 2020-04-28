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

import discord, time, random, asyncio, re

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

    async def on_message(self, message):
        e_content = message.content

        def command_error(error_type, permission_needed, bad_command, the_message):
            if error_type == "Permission":
                return embed_field("Bad Command", ["You just used the %s command!"%bad_command, "You are lacking the *minimum* permission of <@&%s>\nThis means that the command was not completed!"%get_role(the_message, permission_needed)])
            elif error_type == "Useage":
                return embed_field("Bad Command", ["You just used the %s command!"%bad_command, "You are using this command incorrectly, please check the useage by checking the bot docs or doing '?help <commandname>'"])

        if re.match(r"^d!\s*(.*)", e_content):
            the_command = re.findall(r"^d!\s*(.*)", e_content)[0]

            # I recommend putting all admin commands here
            if the_command == "quit":
                if has_role(the_message=message, rolename="Admin"):
                    await message.channel.send(embed=embed_field("Dangerous Command", ["You just used the quit command!", "This is a dangerous command, it will shut down the bot!\nShutting down..."]))
                    quit()
                else:
                    await message.channel.send(embed=command_error(error_type="Permission", permission_needed="Admin", bad_command="quit", the_message=message))
            if the_command == "invite":
                await message.channel.send(embed=embed_field("Extending an invitation!", ["You just used the invite command!", "Use this link: **https://discordapp.com/api/oauth2/authorize?client_id=689934378117234739&permissions=0&scope=bot** to invite David to **your** server!"]))
            # I recommend putting all moderator commands here

            # I recommend putting all global commands here
            if the_command == "myname":
                await message.channel.send(embed=embed_field("Safe Command", ["You just used the myname command!", "Name: {}\nId: {}".format(message.author, message.author.id)]))

            if the_command.split(" ")[0] == "remind":
                these_command_args = " ".join(the_command.split(" ")[1:])
                if re.match(r"^{([0-9\*\-\+\(\)\/\.]+)}\s*([\s\S]+)", these_command_args):
                    the_command_args = " ".join(the_command.split(" ")[1:])
                    
                    this_command_args = re.findall(r"^{([0-9\*\-\+\(\)\/\.]+)}\s*([\s\S]+)", these_command_args)
                    the_command_args = [None, None]
                    the_command_args[0] = eval(str(this_command_args[0][0]))
                    the_command_args[1] = this_command_args[0][1]
                    
                await message.channel.send(embed=embed_field("Safe Command", ["You just used the remind command!", "The remind time has been set to %s minutes"%str(float(the_command_args[0])), "After that time has passed you will be reminded the following:", the_command_args[1]]))
                await asyncio.sleep(float(the_command_args[0])*60)
                await message.channel.send(embed=embed_field("Reminder!", ["This was a reminder set %s minutes ago!"%str(float(the_command_args[0])), the_command_args[1]]))
                    #await message.channel.send(embed=command_error(error_type="Type", permission_needed="", bad_command="remind", the_message=message))

        elif re.match(r"^wd\s*(.*)", e_content):
            pass

        else:
            print("Received Message")



client = MyClient()
client.run('Njg5OTM0Mzc4MTE3MjM0NzM5.XqbjWw.aYFxJ_nYOhWpKmYouaW5lr4IZrQ')
