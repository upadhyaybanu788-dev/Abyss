import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', help='Ask the magic 8ball a question')
    async def eight_ball(self, ctx, *, question):
        responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy, try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]
        await ctx.send(f'🎱 {random.choice(responses)}')

    @commands.command(name='dice', help='Roll a dice')
    async def roll_dice(self, ctx, sides: int = 6):
        if sides < 2:
            await ctx.send('Dice must have at least 2 sides!')
            return
        result = random.randint(1, sides)
        await ctx.send(f'🎲 You rolled a {result}!')

    @commands.command(name='coinflip', help='Flip a coin')
    async def coinflip(self, ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'🪙 {result}!')

async def setup(bot):
    await bot.add_cog(Fun(bot))