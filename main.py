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

import discord
import time
import random
import asyncio
import re 
import os
from termcolor import colored

class webdiplomacy:
   hours_left = 24

    
class console:
    class utils:
        def cyan(text):
          return colored(text, "cyan")

developers = ["685384266736992256"] # Add your DiscordID here if you want to be notified when it's up

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
        global developers

        print('_______________')
        print('Info Type:', console.utils.cyan("Runtime"))
        print('_______________')
        print("Running with name:", console.utils.cyan(self.user.name))
        print("And therefore id:", console.utils.cyan(self.user.id))
        print('And further by extension:', console.utils.cyan(os.environ['token']))
        print('_______________')
        print('Info Type:', console.utils.cyan("Status"))
        print('_______________')
        print('Ready:', console.utils.cyan("yes"))
        print('Guilds:', ", ".join([console.utils.cyan([guild for guild in client.guilds])))
        print('_______________')
        
        #print([[x for x in y.members] for y in client.guilds]))
        total = 0
        for i in client.guilds:
            for x in i.members:
                total += 1
                
        self.bg_task = self.loop.create_task(self.web_diplomacy_reminder())
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over %i kiddie winks"%total))

    async def web_diplomacy_reminder(self):
        pass
        """
        global webdiplomacy
        while not self.is_closed():
            embed = discord.Embed(title="WebDiplomacy!", colour=discord.Colour(0x006400))
            embed.add_field(name="This is an automated reminder", value="%s hours left of the current phase!"%str(webdiplomacy.hours_left))
            self.get_channel(704784702296424518).send(embed=embed)
            
            webdiplomacy.hours_left -= 0.25
            if webdiplomacy.hours_left <= 0:
                webdiplomacy.hours_left = 24
            await asyncio.sleep(15*60)
          """
            
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
            elif the_command == "invite":
                await message.channel.send(embed=embed_field("Extending an invitation!", ["You just used the invite command!", "Use this link: **https://discordapp.com/api/oauth2/authorize?client_id=689934378117234739&permissions=0&scope=bot** to invite David to **your** server!"]))
            elif re.match(r"^([1-9][0-9]*)", the_command):
                embed = discord.Embed(title="Roll that dice!", colour=discord.Colour(0x0000A0))
                value="The result of your **{}** sided dice roll is **{}**".format(re.findall(r"^[0-9]+", the_command)[0], str(random.randint(1, int(re.findall(r"^[0-9]+", the_command)[0]))))
                embed.add_field(name="You just rolled a dice!", value=value)
                await message.channel.send(embed=embed)
            # I recommend putting all moderator commands here

            # I recommend putting all global commands here
            if the_command == "myname":
                await message.channel.send(embed=embed_field("Safe Command", ["You just used the myname command!", "Name: {}\nId: {}".format(message.author, message.author.id)]))

            if the_command.split(" ")[0] == "remind":
                these_command_args = the_command.split(" ")
                if these_command_args[1] == "period":
                    the_command_args = " ".join(the_command.split(" ")[2:])

                    await message.channel.send(embed=embed_field("Safe Command", ["You just used the remind command with a period modifier!", "The remind time has been set to %s minutes"%str(float(the_command_args[1])), "After that time has passed you will be reminded the following:", the_command_args[1]]))

                for i in range(int(these_command_args[2])):
                    pass
                else:
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

        elif re.match(r"^wd!\s*(.*)", e_content):
            the_command = re.findall(r"^wd!\s*(.*)", e_content)[0]
            print(the_command.split(" "))
            if the_command.split(" ")[0] == "remind":
                try:
                    the_command_args = the_command.split(" ")
                    print("{} : {} : {}".format(the_command_args[2], the_command_args[1], " ".join(the_command_args[3:])))
                    embed = discord.Embed(title="Remind me diplomacy style!", colour=discord.Colour(0x4b5320))
                    embed.add_field(name="You've set a reminder to go off every **{}** minutes, **{}** times!".format(str(float(the_command_args[2])), the_command_args[1]), value=" ".join(the_command_args[3:]))
                    await message.channel.send(embed=embed)

                    for i in range(int(the_command_args[1])):
                        embed = discord.Embed(title="Remind me diplomacy style!", colour=discord.Colour(0x4b5320))
                        embed.add_field(name="This is a webdiplomacy reminder set by: **{}**".format(message.author), value=" ".join(the_command_args[3:]))
                        await message.channel.send(embed=embed)
                        await asyncio.sleep(float(the_command_args[2])*60)
                except Exception as e:
                    embed = discord.Embed(title="Remind me diplomacy style!", colour=discord.Colour(0x4b5320))
                    embed.add_field(name="Something went wrong! This is the correct syntax", value="wd!remind (<int>|times) (<float>|interval(minutes)) (<**string>|tobereminded)")
                    await message.channel.send(embed=embed)
                    print(e)


        else:
            print("Received Message")
      
client = MyClient()
client.run(str(os.environ['token']))
