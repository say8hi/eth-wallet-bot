import asyncio

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.inline import choose_menu, admin_menu, back_admin
from tgbot.misc.states import BroadcastState
from tgbot.models.db import Database
from tgbot.services.broadcaster import broadcast

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.callback_query(F.data == 'back_admin')
@admin_router.message(Command("admin"))
async def admin_start(update: Message | CallbackQuery, state: FSMContext):
    await state.clear()
    if isinstance(update, Message):
        await update.answer("Admin-menu", reply_markup=admin_menu)
        return
    await update.message.edit_text("Admin-menu", reply_markup=admin_menu)


# ======================================================================================================================
# Broadcast
@admin_router.callback_query(F.data == 'broadcast')
async def broadcast_main(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>Send me photo with caption for broadcast.\n"
                                               "└─You can send only text.</b>", reply_markup=back_admin)
    await state.set_state(BroadcastState.BS1)
    await state.update_data(msg_to_edit_id=msg_to_edit.message_id)


@admin_router.message(BroadcastState.BS1, F.content_type.in_({'text', 'photo'}))
async def receive_broadcast_data(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit_id = data.get('msg_to_edit_id')
    await message.delete()
    if message.photo:
        file_id = message.photo[-1].file_id
        await state.update_data(photo=file_id, text=message.caption)
        await asyncio.sleep(2)
        await message.bot.delete_message(message.from_user.id, msg_to_edit_id)
        await message.answer_photo(photo=file_id, caption=f"{message.caption}\n\n"
                                                          f"<b>Broadcast message example.\n"
                                                          f"Start broadcast?</b>",
                                   reply_markup=choose_menu)
    else:
        await state.update_data(text=message.text)
        await message.bot.edit_message_text(f"{message.text}\n\n"
                                            f"<b>Broadcast message example.\n"
                                            f"Start broadcast?</b>",
                                            message.from_user.id, msg_to_edit_id, reply_markup=choose_menu)
    await state.set_state(BroadcastState.BS2)


@admin_router.callback_query(BroadcastState.BS2, F.data == 'yes')
async def agree_and_start(call: CallbackQuery, state: FSMContext, bot):
    data = await state.get_data()
    text, photo_name, silent_mode = data.get("text"), data.get('photo'), data.get("silent_mode")
    await state.clear()
    await call.message.delete()
    users = await Database.users.get(get_all=True)
    to_delete = await call.message.answer("<b>Broadcast started</b>")
    done = await broadcast(bot, users, text, photo_name, disable_notification=silent_mode)
    await to_delete.delete()
    await call.message.answer(f"<b>Broadcast finished</b>\n"
                              f"Have received message: <code>{done[0]}</>\n"
                              f"Haven't received message: <code>{done[1]}</>",
                              reply_markup=back_admin)
