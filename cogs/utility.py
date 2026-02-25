import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(f'User: {member.name}, ID: {member.id}')

    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.guild
        await ctx.send(f'Server Name: {server.name}, ID: {server.id}, Total Members: {server.member_count}')

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(member.avatar.url)


def setup(bot):
    bot.add_cog(Utility(bot))
