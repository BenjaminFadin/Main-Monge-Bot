from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming, validators
from loader import dp
from keyboards.default.menuKeyboard import language_choices, remove_kb


@dp.message_handler(state=PersonalData.cart)
async def CartHandler(message: types.Message, state: FSMContext):
    print(f"message: {message}")
    msg = message.text
