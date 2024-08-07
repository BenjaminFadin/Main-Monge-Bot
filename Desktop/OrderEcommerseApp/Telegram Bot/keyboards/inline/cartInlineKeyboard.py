from loader import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

def get_cart_inline_btns(cart_data):
    clear_cart_button = InlineKeyboardButton('🗑️ Очистить корзину', callback_data='clear_cart')
    
    product_buttons = [
        InlineKeyboardButton(f"❌ {item['product']['title']}", callback_data=f"remove_item_{item['id']}")
        for item in cart_data['items']
    ]
    
    # Combine all buttons
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(clear_cart_button)
    keyboard.add(*product_buttons)
    
    return keyboard

# @dp.callback_query_handler(lambda c: c.data == 'clear_cart')
# async def clear_cart(callback_query: CallbackQuery):
#     global cart
#     cart['items'] = []
#     cart['total_price'] = 0.0
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, "Корзина очищена.")

# # Handle removing an item from the cart
# @dp.callback_query_handler(lambda c: c.data.startswith('remove_item_'))
# async def remove_item(callback_query: CallbackQuery):
#     global cart
#     item_id = int(callback_query.data.split('_')[-1])
#     cart['items'] = [item for item in cart['items'] if item['id'] != item_id]
#     cart['total_price'] = sum(item['total_price'] for item in cart['items'])
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, "Товар удален из корзины.")




