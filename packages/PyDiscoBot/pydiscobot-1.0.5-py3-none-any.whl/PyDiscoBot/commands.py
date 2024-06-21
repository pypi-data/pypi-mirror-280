#!/usr/bin/env python
""" Minor League E-Sports Bot Commands
# Author: irox_rl
# Purpose: General Functions and Commands
# Version 1.0.5
#
# v1.0.5 - remove err string (unused anyways)
#           hide a few commands
#           update help function for pagination
#           add get_admin_channel and get_public_channel for command predicates
"""

# local imports #
from .pagination import Pagination

# non-local imports
import datetime
import discord
from discord.ext import commands
import time


class Commands(commands.Cog):
    def __init__(self,
                 master_bot):
        self.bot = master_bot

    async def get_admin_cmds_channel(self):
        return self.bot.admin_commands_channel

    async def get_public_cmds_channel(self):
        return self.bot.public_commands_channel

    def bot_loaded(self) -> bool:
        return self.bot.loaded

    @commands.command(name='echo',
                      description='echo',
                      hidden=True)
    async def echo(self,
                   ctx: discord.ext.commands.Context,
                   *message: str):
        await ctx.send(' '.join(message))

    @commands.command(name='datetounix',
                      description='convert date to unix code for discord purposes.\n'
                                  'You must give a date in the following format: y/m/d H:M:S')
    async def datetounix(self,
                         ctx: discord.ext.commands.Context,
                         *date_string: str):
        try:
            _date = ' '.join(date_string)
            d = datetime.datetime.strptime(_date, '%y/%m/%d %H:%M:%S')
            unix_time = time.mktime(d.timetuple())
            await ctx.send(f'template: <`t:{str(int(unix_time))}:F`>  (remember to add < and > around the template!)')
            await ctx.send(f'<t:{int(unix_time)}:F>')
        except ValueError:
            await ctx.reply('You must give a date in the following format:\n'
                            '%y/%m/%d %H:%M:%S\n'
                            'do not include am/pm. use 24 hour clock.')

    @commands.command(name='help',
                      description="Show all available commands for this bot.")
    async def help(self,
                   ctx: discord.ext.commands.Context):
        cmds = await self.bot.get_help_cmds_by_user(ctx)
        sorted_commands = sorted([command for command in cmds if not command.hidden], key=lambda x: x.name)

        async def get_page(page: int,
                           as_timout: bool=False):
            emb: discord.Embed = self.bot.default_embed(f'**Commands List**\n\n',
                                                        f'Available commands for {ctx.author.mention}')
            if self.bot.server_icon:
                emb.set_thumbnail(url=self.bot.get_emoji(self.bot.server_icon).url)

            if as_timout:
                emb.add_field(name=f'**`Timeout`**',
                              value='This command has timed out. Type `[ub.help]` for help.')
                emb.set_footer(text=f'Page 1 of 1')
                return emb, 0

            elements_per_page = 5
            offset = (page - 1) * elements_per_page
            for cmd in sorted_commands[offset:offset + elements_per_page]:
                emb.add_field(name=f'**`ub.{cmd} {"  ".join([f"[{param}]" for param in cmd.clean_params])}`**',
                              value=f'{cmd.description}',
                              inline=False)
            total_pages = Pagination.compute_total_pages(len(sorted_commands),
                                                         elements_per_page)

            emb.set_footer(text=f'Page {page} of {total_pages}')
            return emb, total_pages

        await Pagination(ctx, get_page).navigate()

    @commands.command(name="info",
                      description="Get build info.")
    async def info(self,
                   ctx: discord.ext.commands.Context):
        return await ctx.reply(embed=self.bot.info_embed())

    @commands.command(name='test',
                      description='developer test function',
                      hidden=True)
    async def test(self,
                   ctx: discord.ext.commands.Context):
        await ctx.send('guh? huh? who what? where am i?')

    @commands.Cog.listener()
    async def on_message(self,
                         message: discord.Message):
        if message.author == self.bot.user:
            return

        if 'nice' == message.content.lower():
            await message.reply('nice')
