#!/usr/bin/env python
""" Minor League E-Sports Bot
# Author: irox_rl
# Purpose: General Functions of a League Franchise summarized in bot fashion!
# Version 1.0.6
#
# v1.0.6 - integrate for slash commands
        update send_notification to include interactions if command is app_command
"""

# local imports #
from .channels import get_channel_by_id
from .commands import Commands
from .err import register_callback, InsufficientPrivilege, IllegalChannel, BotNotLoaded
from .periodic_task import PeriodicTask

# non-local imports
import asyncio
import datetime
import discord
from discord.ext import commands as disco_commands
import dotenv
import os


class Bot(discord.ext.commands.Bot):
    """ Default bot by irox
    """

    def __init__(self,
                 command_prefix: str | list,
                 bot_intents: discord.Intents | None,
                 command_cogs: [disco_commands.Cog]):
        super().__init__(command_prefix=command_prefix,
                         intents=bot_intents,
                         help_command=None,
                         case_insensitive=True)
        self._version = os.getenv('VERSION')
        if not self._version:
            raise ValueError('Version not determined from .env file. Please use a valid .env file.')
        try:
            self._server_icon = os.getenv('SERVER_ICON')
        except ValueError:
            self._server_icon = None

        self._handler: discord.User | None = None
        self._admin_channel: discord.TextChannel | None = None
        self._notification_channel: discord.TextChannel | None = None
        self._initialized = False
        self._guild: discord.Guild | None = None
        self._time = datetime.datetime.now()
        self._last_time = self._time
        self._start_time = datetime.datetime.now()
        self._cycle_time = int(os.getenv('CYCLE_TIME'))
        self._periodic_task: PeriodicTask = PeriodicTask(self.cycle_time,
                                                         self,
                                                         task_callback=self.on_task,
                                                         enable_admin=True)
        for cog in command_cogs:
            asyncio.run(self.add_cog(cog(self)))

        register_callback(self.__err__)

    @property
    def admin_channel(self) -> discord.TextChannel | None:
        """ return the admin channel
        """
        return self._admin_channel

    @property
    def cycle_time(self) -> int:
        """ return the cycle time
                """
        return self._cycle_time

    @property
    def day_of_week(self) -> str:
        """ return the day of week, formatted as yyyy-mm-dd hh:mm:ss
                """
        return self._time.strftime('%A')

    @property
    def default_embed_color(self):
        """ return the discord.color for an embed object to use
            Over-ride this property to use a different color
        """
        return discord.Color.dark_blue()

    @property
    def guild(self) -> discord.Guild:
        return self._guild

    @property
    def handler(self) -> discord.User | None:
        """ return the handler of this bot
                        """
        return self._handler

    @property
    def loaded(self) -> bool:
        """ loaded status for bot\n
        override to include external processes that need to load when initiating
        """
        return self._periodic_task.initialized and self._initialized

    @property
    def notification_channel(self) -> discord.TextChannel | None:
        return self._notification_channel

    @property
    def last_time(self):
        return self._last_time

    @property
    def server_icon(self):
        return self._server_icon

    @property
    def time(self) -> datetime.datetime:
        return self._time

    @property
    def version(self) -> str:
        """ return the version of this repo
                                """
        return self._version

    async def __begin_task__(self) -> None:
        """ Begin periodic task\n
        **returns**: None\n
        """
        self._periodic_task.change_interval(seconds=self.cycle_time)
        self._periodic_task.run.start()

    def default_embed(self,
                      title: str,
                      description: str = '',
                      color=None) -> discord.Embed:
        """ Helper function to easily and repeatedly get the same embed\n
            **param title**: title of the embed\n
            **param description**: description to create the embed with\n
            **returns**: discord.Embed with name and description supplied
         """
        # this should be updated to be a class method, along with the default color
        if not color:
            color = self.default_embed_color
        return discord.Embed(color=color,
                             title=title,
                             description=description)

    async def __err__(self,
                      message: str | Exception) -> None:
        """ Helper function to send error or notification messages to notify channel with a single parameter.\n
            **If a notification channel does not exist**, the notification is printed to console instead\n
            **param message**: message to report\n
            **returns**: None\n
            """
        if not message:
            return
        if not self._notification_channel:
            return print(message)
        await self.send_notification(ctx=self._notification_channel,
                                     text=message,
                                     as_reply=False)

    def emoji_by_name(self,
                      _name: str):
        return next((x for x in self.guild.emojis if x.name == _name), None)

    async def get_app_cmds_by_user(self,
                                   ctx: discord.ext.commands.Context) -> [disco_commands.command]:
        return self.tree.walk_commands()

    async def get_help_cmds_by_user(self,
                                    ctx: discord.ext.commands.Context) -> [disco_commands.command]:
        return self.commands

    async def get_notification_embed(self,
                                     text: str) -> discord.Embed:
        embed = (self.default_embed('**Notification**')
                 .add_field(name='Message', value=text, inline=True)
                 .set_footer(text=f'Generated: {datetime.datetime.now()}'))
        if self._server_icon:
            embed.set_thumbnail(url=self._server_icon)
        return embed

    async def send_notification(self,
                                ctx: discord.ext.commands.Context | discord.abc.GuildChannel | discord.Interaction,
                                text: str,
                                as_reply: bool = False,
                                as_followup: bool = False) -> None:
        """ Helper function to send notifications as required to a specific context, also as reply if required\n
        **param ctx**: context to send notification to\n
        **param text**: text of the notification body\n
        **as_reply**: send the notification as a discord reply to the context\n
        **returns**: None\n
        """
        embed = await self.get_notification_embed(text)
        if isinstance(ctx, discord.ext.commands.Context):
            await ctx.reply(embed=embed) if as_reply and (ctx.author is not None) else await ctx.send(embed=embed)
            return
        elif isinstance(ctx, discord.Interaction):
            await ctx.response.send_message(embed=embed) if not as_followup else await ctx.followup.send(embed=embed)
            return
        elif isinstance(ctx, discord.TextChannel):
            await ctx.send(embed=embed)
            return

    def info_embed(self) -> discord.Embed:
        """ helper to get information embed\n
            **returns**: discord.Embed with bot info attached\n
        """
        embed = discord.Embed(color=self.default_embed_color, title='**Bot Info**\n\n',
                              description='For help, type `ub.help`\n\n')
        embed.add_field(name='Version', value=f"`{self.version}`", inline=True)
        embed.add_field(name='Boot Time', value=f"`{self._start_time}`", inline=False)
        embed.add_field(name='Current Tick', value=f"`{self._periodic_task.ticks}`", inline=True)
        embed.add_field(name='Last Tick Time', value=f"`{self._last_time}`", inline=False)
        embed.add_field(name='Cycle Time', value=f"`{self.cycle_time}` seconds", inline=True)
        if self._server_icon:
            embed.set_thumbnail(url=self._server_icon)
        return embed

    async def on_command_error(self,
                               ctx: discord.ext.commands.Context,
                               error) -> None:
        """ Override of discord.Bot on_command_error
            If CommandNotFound, simply reply to the user of the error.\n
            If not, raise the error naturally\n
            ***param ctx***: context to send the error message to\n
            ***param error***: error that occurred\n
            ***returns***: None\n
            **raises**: supplied error if not **discord.ext.commands.errors.CommandNotFound**
            """
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.reply("That command wasn't found! Type 'ub.help' for a list of all available commands.")
            return
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.reply(f'You must fill in additional arguments for this command!\n{error}')
            return
        elif isinstance(error, discord.HTTPException):
            await ctx.reply('We are being rate limited... Please wait a few moments before trying that again.')
            return
        elif isinstance(error, InsufficientPrivilege):
            await ctx.reply(error.__str__())
            return
        elif isinstance(error, IllegalChannel):
            await ctx.reply(error.__str__())
            return
        elif isinstance(error, BotNotLoaded):
            await ctx.reply(error.__str__())
            return
        else:
            await self.__err__(f'We have encountered the following error:\n{error.__str__()}')
            raise error

    async def on_ready(self,
                       suppress_task=False) -> None:
        """ Method that is called by discord when the bot connects to the supplied guild\n
        **param suppress_task**: if True, do NOT run periodic task at the end of this call\n
        **returns**: None\n
        """
        if self._initialized:
            return

        guild_token = os.getenv('GUILD')
        handler_token = os.getenv('HANDLER')
        admin_channel_token = os.getenv('ADMIN_CHANNEL')
        notification_channel_token = os.getenv('NOTIFICATION_CHANNEL')

        if not guild_token:
            raise ValueError('guild token must be supplied in .env file!')
        self._guild = next((x for x in self.guilds if x.id.__str__() == guild_token), None)
        if self._guild is None:
            raise ValueError('Supplied guild is not available to this bot.\n'
                             'Please invite the bot to the rubber duck pond')

        self._handler = next((x for x in self._guild.members if x.id.__str__() == handler_token), None)
        self._admin_channel = get_channel_by_id(admin_channel_token,
                                                self._guild) if admin_channel_token else None
        self._notification_channel = get_channel_by_id(notification_channel_token,
                                                       self._guild) if notification_channel_token else None
        self._initialized = True

        print(f'POST -> {datetime.datetime.now()}')

        if not suppress_task:
            await self.__begin_task__()

    async def on_task(self) -> None:
        """ callback method for periodic task to call during it's interval\n
            override this as needed
        **returns**: None\n
        """
        pass


if __name__ == '__main__':
    """ common call for .py file.
        if this file is called, the code below is run
        if this file is imported, it will not run
        """
    """ load dotenv before generating bot
    """
    dotenv.load_dotenv()

    """ generate intents for bot
        the compiler doesn't like that it thinks these properties are read-only, but they're not.
        the following boolean assignments are required for this bot to function
        """
    intents = discord.Intents(8)
    # noinspection PyDunderSlots
    intents.guilds = True
    # noinspection PyDunderSlots
    intents.members = True
    # noinspection PyDunderSlots
    intents.message_content = True
    # noinspection PyDunderSlots
    intents.messages = True

    """ generate bot
        load bot params from .env file
        do not modify this code!
        modify the .env!
        include any task args at the end!
    """
    bot = Bot('ub.',
              intents,
              command_cogs=[Commands])
    """ Start 
    """
    bot.run(os.getenv('DISCORD_TOKEN'))
