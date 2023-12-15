from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📬Broadcast", callback_data="broadcast")
        ],
        [
            InlineKeyboardButton(text="✖Close", callback_data="close")
        ]
    ]
)

back_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙Back", callback_data='back_admin')
        ]
    ]
)

close_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✖️Close", callback_data='close')
        ]
    ]
)

choose_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔Yes", callback_data='yes'),
        ],
        [
            InlineKeyboardButton(text="🔙Back", callback_data='back_admin')
        ]
    ]
)


def wallet_menu(has_wallet=False):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💠Add wallet", callback_data='add_wallet:main'),
            ] if not has_wallet else [],
            [
                InlineKeyboardButton(text="✖️Close", callback_data='close')
            ]
        ]
    )
