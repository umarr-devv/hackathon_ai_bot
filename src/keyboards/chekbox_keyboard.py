from aiogram import types
from src.functions.string_values import answers


class ChekBoxKeyboard:
    url_buttons: list[types.InlineKeyboardButton]
    next_button: types.InlineKeyboardButton
    prefix: str
    answers_key: str

    def __init__(self, prefix: str):
        self.prefix = prefix

    def as_keyboard(self, values: dict):
        buttons = [
            [
                types.InlineKeyboardButton(
                    text=f'{"✅" if values[index] else "☑️"} {answers[self.answers_key][index]}',
                    callback_data=f'{self.prefix}_{index}'
                )
            ]
            for index in range(1, len(answers[self.answers_key]) + 1)
        ]
        return types.InlineKeyboardMarkup(
            inline_keyboard=buttons
        )
