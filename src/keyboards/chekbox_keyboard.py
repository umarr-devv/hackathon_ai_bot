from aiogram import types
from src.functions.string_values import answers


class ChekBoxKeyboard:
    url_buttons: list[types.InlineKeyboardButton] = []
    next_button: list[types.InlineKeyboardButton] = []
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
        buttons += self.url_buttons + self.next_button
        return types.InlineKeyboardMarkup(
            inline_keyboard=buttons
        )


class InformatedKeyboard(ChekBoxKeyboard):
    url_buttons = [
        [types.InlineKeyboardButton(
            text='❕ Информация про хакатон',
            url='deliver.latoken.com/hackathon'
        )
        ],
        [
            types.InlineKeyboardButton(
                text='❕ Информация про Латокен',
                url='deliver.latoken.com/about'
            )
        ],
        [
            types.InlineKeyboardButton(
                text='❕ Ссылка на #nackedmanagement',
                url='coda.io/@latoken/latoken-talent/nakedmanagement-88'
            )
        ]
    ]

    next_button = [[
        types.InlineKeyboardButton(
            text='➡️ Следующий Вопрос',
            callback_data='next-informated'
        )
    ]]

    answers_key = 'informated'


class AdvantageKeyboard(ChekBoxKeyboard):
    next_button = [[
        types.InlineKeyboardButton(
            text='➡️ Следующий Вопрос',
            callback_data='next-advantage'
        )
    ]]
    answers_key = 'advantage'


class VentureFundKeyboard(ChekBoxKeyboard):
    answers_key = 'venture_fund'

    url_buttons = [[
        types.InlineKeyboardButton(
            text='Ссылка на статью',
            url='https://coda.io/d/LATOKEN-Talent_dubFlG9FzGD/Wartime-Principles_suq47#_luMKu'
        )
    ]]
    next_button = [[
        types.InlineKeyboardButton(
            text='➡️ Следующий Вопрос',
            callback_data='next-venture-fund'
        )
    ]]

class WantKeyboard(ChekBoxKeyboard):
    class VentureFundKeyboard(ChekBoxKeyboard):
        answers_key = 'want'

        next_button = [[
            types.InlineKeyboardButton(
                text='➡️ Следующий Вопрос',
                callback_data='next-want'
            )
        ]]