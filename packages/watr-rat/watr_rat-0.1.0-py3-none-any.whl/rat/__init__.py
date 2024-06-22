import asyncio
import os
import random

import discord


class Rat(discord.Client):
    def __init__(self, id_: int):
        super().__init__()
        self.id_ = id_

    def start(self) -> None:
        return super().start(os.getenv(f"RAT_{self.id_}_TOKEN"))

    async def on_ready(self):
        # Ready
        channel = await self.fetch_channel(os.getenv(f"RAT_{self.id_}_CHANNEL"))
        application_commands = await channel.application_commands()

        for application_command in application_commands:
            if application_command.name == "fish":
                fish_application_command = application_command

        # Fishing
        await fish_application_command(channel)

    async def on_message(self, message: discord.Message):
        # On cooldown
        await asyncio.sleep(3.5 + sum([random.random() for _ in range(2)]))

        if message.author.id != 574652751745777665:
            return

        if message.channel.category_id != 1253328745918500874:
            return

        access = None

        for embed in message.embeds:
            if embed.title is None:
                continue

            if "You caught:" not in embed.title:
                continue

            if self.user.display_name not in embed.author.name:
                return

            access = embed

        if access is None:
            return

        component = message.components[0]
        child = component.children[0]

        if "Fish Again" not in child.label:
            return

        # Fishing
        await child.click()
