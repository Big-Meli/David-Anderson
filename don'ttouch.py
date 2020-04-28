    async def on_message_delete(self, message):
        embed = discord.Embed(title="Message alert!", colour=discord.Colour(0x0000A0))
        embed.add_field(name="A Message was **Deleted**!", value="Guild: {}\nChannel: {}\nUser: {}\nContent: {}".format(message.guild, message.channel, message.author, message.content))
        await message.channel.send("704773875900088402", embed=embed)
        
        print("A Message was Deleted!", value="Guild: {}\nChannel: {}\nUser: {}\nContent: {}".format(message.guild, message.channel, message.author, message.content))

    async def on_message(self, message):
        embed = discord.Embed(title="Message alert!", colour=discord.Colour(0x0000A0))
        embed.add_field(name="A Message was **Sent**!", value="Guild: {}\nChannel: {}\nUser: {}\nContent: {}".format(message.guild, message.channel, message.author, message.content))
        await message.channel.send("704773875900088402", embed=embed)

        print("A Message was Sent!", value="Guild: {}\nChannel: {}\nUser: {}\nContent: {}".format(message.guild, message.channel, message.author, message.content))

    async def on_message_edit(self, before, after):
        embed = discord.Embed(title="Message alert!", colour=discord.Colour(0x0000A0))
        embed.add_field(name="A Message was **Edited**!", value="Guild: {}\nChannel: {}\nUser: {}\nContent Before: {}\nContent After: {}".format(before.guild, before.channel, before.author, before.content, after.content))
        await message.channel.send("704773875900088402", embed=embed)

        print(name="A Message was Edited!", value="Guild: {}\nChannel: {}\nUser: {}\nContent Before: {}\nContent After: {}".format(before.guild, before.channel, before.author, before.content, after.content))
        
