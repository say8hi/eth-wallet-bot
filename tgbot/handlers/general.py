from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from tgbot.filters.chats import IsPrivate
from tgbot.keyboards.inline import close_menu, wallet_menu
from tgbot.keyboards.reply import main_menu
from tgbot.models.db import Database

user_router = Router()
user_router.message.filter(IsPrivate())


@user_router.callback_query(F.data == "close")
async def user_start(call: CallbackQuery):
    await call.message.delete()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(f"Hi, <code>{message.from_user.full_name}</>",
                         reply_markup=main_menu)


@user_router.message(F.text == '❕Info')
async def user_start(message: Message):
    await message.answer("🤖 Welcome to @say8hi ETH Wallet Bot!\n"
                         "This bot allows you to securely store and transfer Ethereum (ETH) easily.\n\n"
                         "❗️Remember to keep your wallet information secure, "
                         "and never share your private keys with anyone.\n\n"
                         "Happy managing your ETH! 🚀💰",
                         reply_markup=close_menu)


@user_router.message(F.text == "👝My wallet")
async def user_start(message: Message):
    eth_wallet = await Database.eth_accounts.get(message.from_user.id)
    text = f"\n❕You don't have a wallet yet."
    if eth_wallet:
        eth_amount = 0
        text = f"├─Address: <code>{eth_wallet.get('address')}</>\n" \
               f"└─ETH amount: <code>{eth_amount}</>"
    await message.answer(f"Your wallet:\n{text}", reply_markup=wallet_menu(bool(eth_wallet)))
