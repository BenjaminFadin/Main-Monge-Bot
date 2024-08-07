from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db, bot
from data.config import API_URL
from utils import get_cart_items_by_tg_id
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from keyboards.default.settingsKeyboard import get_settings_keyboard
from keyboards.inline.cartInlineKeyboard import get_cart_inline_btns


@dp.message_handler(state=PersonalData.main_menu)
async def mainMenuHandler(message: types.Message):
    print('mainMenuHandler')
    user = await db.select_user(telegram_id=message.from_user.id)
    user_lang = user['language']
    telegram_id = user['telegram_id']
    cart_data = get_cart_items_by_tg_id(API_URL, telegram_id)[0]

    msg = message.text

    if msg == naming.CART[user_lang]:
        # Sending message from cart_data
        # await message.answer(cart_data)    

        # products = cart_data['items']
        # delivery_price = 24000
        # total_price_with_delivery = float(cart_data['total_price']) + delivery_price

        # # Create the message
        # text = f"ID korzina: \n"
        # for item in products:
        #     product = item['product']
        #     text += f"Product: {product['title']}\n"

        # text += f"\nTotal Price: {cart_data['total_price']} so'm\n"
        # text += f"Delivery: {delivery_price} so'm\n"
        # text += f"Total Price with Delivery: {total_price_with_delivery} so'm"
        # await message.answer(text)
        await message.answer(cart_data['total_price'], reply_markup=get_cart_inline_btns(cart_data))

        await PersonalData.cart.set()
    elif msg == naming.COMMENT[user_lang]:
        await message.answer("Comment")
    elif msg == naming.SETTINGS[user_lang]:
        await message.answer(naming.SETTINGS_MSG[user_lang], reply_markup=get_settings_keyboard(user_lang))
        await PersonalData.settings.set()
    elif msg == naming.CURR_ORDERS[user_lang]:
        await message.answer("Current orders")
    else:
        await message.answer(naming.error_msg[user_lang])


@dp.callback_query_handler(state='*')
async def callback_handler(callback_query: CallbackQuery):
    data = callback_query.data
    if data == 'clear_cart':
        print('clear_cart')
        user_id = callback_query.from_user.id
        await db.clean_cart(user_id)
        print(user_id)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Корзина очищена.")
        await PersonalData.cart.set()
    elif data.startswith('remove_item'):
        print('remove_item')
        item_id = int(callback_query.data.split('_')[-1])
        await db.remove_cart_item(item_id)
        print(item_id)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Товар удален из корзины.")
