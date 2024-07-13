from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from src.keyboards import AdvantageKeyboard, InformatedKeyboard, ListKeyboard, VentureFundKeyboard, WantKeyboard
from src.keyboards.chekbox_keyboard import ChekBoxKeyboard, InformatedKeyboard
from src.functions.string_values import questions


class QuestionsState(StatesGroup):
    default = State()
    salary = State()
    opinion = State()


router = Router()


@router.message(F.text == '/test', StateFilter(None))
@router.callback_query(F.data.startswith('test-informated'), QuestionsState.default)
async def on_start_test(message: types.Message | types.CallbackQuery,
                        state: FSMContext):
    text = f'Вопрос: {questions["informated"]}'
    keybaord = InformatedKeyboard('test-informated')

    if isinstance(message, types.Message):
        await state.set_state(QuestionsState.default)
        default_value = {number: False for number in range(1, 4)}
        await state.update_data(
            {'informated': default_value}
        )

        await message.answer(text, reply_markup=keybaord.as_keyboard(default_value))

    elif isinstance(message, types.CallbackQuery):
        await message.answer()

        prefix, value = message.data.split('_')
        value = int(value)
        data = await state.get_data()
        data['informated'][value] = not data['informated'][value]
        await state.update_data(data)

        await message.message.edit_reply_markup(reply_markup=keybaord.as_keyboard(data['informated']))


@router.callback_query(F.data == 'next-informated', QuestionsState.default)
async def on_prize_fund(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup()

    text = f'Вопрос: {questions["prize_fund"]}'
    keyboard = ListKeyboard(prefix='test-prize-fund', answers_key='prize_fund')

    await callback.message.answer(text, reply_markup=keyboard.as_keyboard())


@router.callback_query(F.data.startswith('test-prize-fund'), QuestionsState.default)
async def on_expectation(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup()

    prefix, value = callback.data.split('_')
    await state.update_data({'prize_fund': int(value)})

    text = f'Вопрос: {questions["expectation"]}'
    keyboard = ListKeyboard(prefix='test-expectation', answers_key='expectation')

    await callback.message.answer(text, reply_markup=keyboard.as_keyboard())


@router.callback_query(F.data.startswith('test-expectation'), QuestionsState.default)
@router.callback_query(F.data.startswith('test-advantage'), QuestionsState.default)
async def on_advantage(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    text = f'Вопрос: {questions["advantage"]}'
    keyboard = AdvantageKeyboard('test-advantage')

    if callback.data.startswith('test-expectation'):
        await callback.message.edit_reply_markup()

        prefix, value = callback.data.split('_')
        await state.update_data({'expectation': int(value)})

        default_value = {number: False for number in range(1, 10)}
        await state.update_data(
            {'advantage': default_value}
        )

        await callback.message.answer(text, reply_markup=keyboard.as_keyboard(default_value))

    elif callback.data.startswith('test-advantage'):
        prefix, value = callback.data.split('_')
        value = int(value)
        data = await state.get_data()
        data['advantage'][value] = not data['advantage'][value]
        await state.update_data(data)

        await callback.message.edit_reply_markup(reply_markup=keyboard.as_keyboard(data['advantage']))


@router.callback_query(F.data == 'next-advantage', QuestionsState.default)
async def on_salary(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup()

    await state.set_state(QuestionsState.salary)
    text = f'Вопрос: {questions["salary"]}'

    await callback.message.answer(text)


@router.message(QuestionsState.salary)
async def on_schedule(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:
        text = f'Вопрос: {questions["schedule"]}'
        keyboard = ListKeyboard('test-schedule', 'schedule').as_keyboard()
        await state.set_state(QuestionsState.default)
        await state.update_data({'salary': message.text})
    else:
        text = 'Некорректные данные'
        keyboard = None

    await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data.startswith('test-schedule'), QuestionsState.default)
@router.callback_query(F.data.startswith('test-venture-fund'), QuestionsState.default)
async def on_venture_fund(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    text = f'Вопрос: {questions["venture_fund"]}'
    keyboard = VentureFundKeyboard('test-venture-fund')

    if callback.data.startswith('test-schedule'):
        await callback.message.edit_reply_markup()

        prefix, value = callback.data.split('_')
        await state.update_data({'schedule': int(value)})

        default_value = {number: False for number in range(1, 7)}
        await state.update_data(
            {'venture-fund': default_value}
        )

        await callback.message.answer(text, reply_markup=keyboard.as_keyboard(default_value))

    elif callback.data.startswith('test-venture-fund'):
        prefix, value = callback.data.split('_')
        value = int(value)
        data = await state.get_data()
        data['venture-fund'][value] = not data['venture-fund'][value]
        await state.update_data(data)

        await callback.message.edit_reply_markup(reply_markup=keyboard.as_keyboard(data['venture-fund']))


@router.callback_query(F.data.startswith('next-venture-fund'), QuestionsState.default)
@router.callback_query(F.data.startswith('test-want'), QuestionsState.default)
async def on_want(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    text = f'Вопрос: {questions["want"]}'
    keyboard = WantKeyboard('test-want')

    if callback.data == 'next-venture-fund':
        await callback.message.edit_reply_markup()

        default_value = {number: False for number in range(1, 8)}
        await state.update_data(
            {'want': default_value}
        )

        await callback.message.answer(text, reply_markup=keyboard.as_keyboard(default_value))

    elif callback.data.startswith('test-want'):
        prefix, value = callback.data.split('_')
        value = int(value)
        data = await state.get_data()
        data['want'][value] = not data['want'][value]
        await state.update_data(data)

        await callback.message.edit_reply_markup(reply_markup=keyboard.as_keyboard(data['want']))


@router.callback_query(F.data == 'next-want', QuestionsState.default)
async def on_exam(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_reply_markup()

    text = f'Вопрос: {questions["exam"]}'
    keyboard = ListKeyboard(prefix='test-exam', answers_key='exam')
    await callback.message.answer(text, reply_markup=keyboard.as_keyboard())


@router.callback_query(F.data.startswith('test-exam'), QuestionsState.default)
async def on_task(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup()
    
    prefix, value = callback.data.split('_')
    await state.update_data({'exam': int(value)})

    text = f'Вопрос: {questions["task"]}'
    keyboard = ListKeyboard(prefix='test-task', answers_key='task')
    await callback.message.answer(text, reply_markup=keyboard.as_keyboard())


@router.callback_query(F.data.startswith('test-task'), QuestionsState.default)
async def on_opinion(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_reply_markup()
    
    prefix, value = callback.data.split('_')
    await state.update_data({'task': int(value)})

    text = f'Вопрос: {questions["opinion"]}'
    await callback.message.answer(text)
    
    await state.set_state(QuestionsState.opinion)


@router.message(QuestionsState.opinion)
async def on_finish_test(message: types.Message, state: FSMContext):
    await state.update_data({'opinion': message.text})
    data = await state.get_data()
    await state.clear()