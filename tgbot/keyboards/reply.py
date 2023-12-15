from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(text="👝My wallet")
                                    ],
                                    [
                                        KeyboardButton(text="❕Info")
                                    ]
                                ])
