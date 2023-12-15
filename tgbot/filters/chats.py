from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config


class IsPrivate(BaseFilter):
    async def __call__(self, obj: Message, config: Config) -> bool:
        return obj.chat.type == "private"
