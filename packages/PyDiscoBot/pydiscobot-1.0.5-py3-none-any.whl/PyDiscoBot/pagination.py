#!/usr/bin/env python
""" Pagination handling for discord API
# Author: irox_rl
# Purpose: Handle pagination efforts for embeds
# Version 1.0.5
#
# v1.0.5 - initial release, developed on ub.help command
"""

# local imports #
from typing import Callable, Optional

# non-local imports
import discord
from discord.ext import commands


class Pagination(discord.ui.View):
    def __init__(self,
                 ctx: discord.ext.commands.Context,
                 get_page: Callable):
        self.ctx = ctx
        self.msg: discord.Message | None = None
        self.get_page = get_page
        self.total_pages: Optional[int] = None
        self.index = 1
        super().__init__(timeout=100)

    async def interaction_check(self,
                                interaction: discord.Interaction) -> bool:
        return True

    async def navigate(self):
        embed, self.total_pages = await self.get_page(self.index)
        if self.total_pages == 1:
            if not self.msg:
                self.msg = await self.ctx.send(embed=embed)
            else:
                await self.msg.edit(embed=embed)
        elif self.total_pages > 1:
            self.update_buttons()
            if not self.msg:
                self.msg = await self.ctx.send(embed=embed, view=self)
            else:
                await self.msg.edit(embed=embed, view=self)

    async def edit_page(self,
                        interaction: discord.Interaction):
        embed, self.total_pages = await self.get_page(self.index)
        self.update_buttons()
        if not self.msg:
            self.msg = await self.ctx.send(embed=embed, view=self)
        else:
            await self.msg.edit(embed=embed, view=self)

        # this WILL throw. but it's fine. we just need it for the interaction complete
        # but we don't want to be bombarded by messages
        try:
            await interaction.response.send_message('', ephemeral=True)
        except discord.HTTPException:
            return

    def update_buttons(self):
        self.children[0].disabled = self.index == 1
        self.children[1].disabled = self.index == self.total_pages

    @discord.ui.button(emoji="◀️", style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.Button):
        self.index -= 1
        await self.edit_page(interaction)

    @discord.ui.button(emoji="▶️", style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.Button):
        self.index += 1
        await self.edit_page(interaction)

    async def on_timeout(self) -> None:
        embed, self.total_pages = await self.get_page(0,
                                                      as_timout=True)
        if not self.msg:
            self.msg = await self.ctx.send(embed=embed)
        else:
            await self.msg.edit(embed=embed, view=None)

    @staticmethod
    def compute_total_pages(total_results: int, results_per_page: int) -> int:
        return ((total_results - 1) // results_per_page) + 1
