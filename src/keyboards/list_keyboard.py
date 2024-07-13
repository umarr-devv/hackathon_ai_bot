from aiogram import types

from src.functions.string_values import answers


class ListKeyboard:
    prefix: str
    answers_key: str

    def __init__(self, prefix: str, answers_key: str):
        self.prefix = prefix
        self.answers_key = answers_key

    def as_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(
                    text=f'{answers[self.answers_key][index]}',
                    callback_data=f'{self.prefix}_{index}'
                )
            ]
            for index in range(1, len(answers[self.answers_key]) + 1)
        ]
        return types.InlineKeyboardMarkup(
            inline_keyboard=buttons
        )
