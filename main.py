import discord, time, random, asyncio

def has_role(message, rolename):
  if discord.utils.get(message.guild.roles, name=rolename) in message.author.roles:
    return True
  else:
    return False

def get_role(message, rolename):
  return discord.utils.get(message.guild.roles , name=rolename)

def embed_field(title, *fields):
  embed = discord.Embed(title=title, colour=discord.Colour(0x0000A0))
  for i in fields:
    embed.add_field(name=i[0], value=i[1])
  
  return embed


class discord_player:
  def __init__(this, username, password, inventory, money, friends, enemies):
    this.username = username
    this.password = password
    this.inventory = inventory
    this.money = money
    this.friends = friends
    this.enemies = enemies

  def load(this):
    pass

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(member):
      member.add_roles(get_role(member, 'Unidentified'))

    async def on_message(self, message):

      if has_role(message, 'mute'):
        await message.delete()
      
      else:
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!'):

          command = message.content.split(" ")[0][1:]

          try:
            commandsub1 = message.content.split(" ")[1]
            commandargs = message.content.split(" ")[2]
          except:
            pass

          commandless = message.content.replace(command, '').replace('! ', '')
          
          if has_role(message, 'Admin') or has_role(message, 'Senpai') or has_role(message, 'Teacher'): # Admin commands
            if command == 'mute': # Mute command

              if commandsub1 == "-t": # Time args
                await message.mentions[0].add_roles(get_role(message, 'mute'))
                await message.channel.send(embed=embed_field('', ['Someone was muted!','Person: {}\nTime: {} minutes'.format(message.mentions[0].mention,str(commandargs))]))

                await asyncio.sleep(float(commandargs) * 60)

                await message.mentions[0].remove_roles(get_role(message, 'mute'))
              
              else: # No time args

                await message.mentions[0].add_roles(get_role(message, 'mute'))

            elif command == 'unmute': # Unmute command

              await message.mentions[0].remove_roles(get_role(message, 'mute'))

            elif command == 'immitate':
              
              await message.channel.send(commandless)
              await message.delete()

          if has_role(message, 'Mod'):
            pass

          if command == 'commands':

            embed = embed_field('Command List',  ['Admin: Mute', 'Syntax: !mute {@person}\nSyntax: !mute -t {minutes} {@person}'],['Admin: Unmute', 'Syntax: !unmute {@person}'],['Admin: Immitate', 'Syntax: !immitate {args}'],['U: Ratemypp', 'Syntax: !ratemypp'],['U: Commands', 'Syntax: !commands'],['U: Remindme [W.I.P]', 'Syntax: !remindme -t {minutes} {args}'],['U: Setip','Syntax: !setip {ip}'])
            await message.channel.send(embed=embed)



          if command == 'ratemypp': # pp command
            responses = """Pretty cool chief, Not very long so 3/10, You got a rocking dong bro, You call that a pp?, Hard as a rock like Nock, Even Stan has a bigger penis than that.. 3/4, Would smash ngl, Mine's bigger ;), Damn bro that's pretty good.. maybe we should team up :eggplant:""".split(', ')

            await message.channel.send(responses[random.randint(0,len(responses)-1)])
          
          #Make notification command 
          

client = MyClient()
client.run('Njg5OTM0Mzc4MTE3MjM0NzM5.XnKFiA.8Dg2KgzgUi4zNNTq773AU6zMW-c')
