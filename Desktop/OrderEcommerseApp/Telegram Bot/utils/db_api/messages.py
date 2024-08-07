# from loader import dp
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
# from data.config import API_URL

# delivery_cost = 12000


# def get_cart_keyboard(cart_data):
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     for item in cart_data[0]['items']:
#         keyboard.add(InlineKeyboardButton(
#             f"❌ {item['product']['title']} x{item['quantity']}",
#             callback_data=f'remove_item_{item["id"]}'
#         ))

#     keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))
#     keyboard.add(InlineKeyboardButton("Очистить корзину", callback_data="clear_cart"))
#     keyboard.add(InlineKeyboardButton("Оформить заказ", callback_data="place_order"))

#     return keyboard


# @dp.message_handler(commands=['start', 'cart'])
# async def send_cart(message: types.Message):
#     cart = cart_data[0]
#     items_text = "\n".join(
#         [f"{item['quantity']}x {item['product']['title']} - {item['total_price']} сум" for item in cart['items']]
#     )
#     total_cost = cart['total_price'] + delivery_cost

#     text = (
#         f"В корзине:\n"
#         f"{items_text}\n\n"
#         f"Товары: {cart['total_price']} сум\n"
#         f"Доставка: {delivery_cost} сум\n"
#         f"Итого: {total_cost} сум"
#     )

#     await message.answer(text, reply_markup=get_cart_keyboard())


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('remove_item_'))
# async def remove_item(callback_query: CallbackQuery):
#     item_id = int(callback_query.data.split('_')[-1])
#     cart = cart_data[0]
#     cart['items'] = [item for item in cart['items'] if item['id'] != item_id]
#     cart['total_price'] = sum(item['total_price'] for item in cart['items'])

#     await callback_query.answer("Item removed")
#     await send_cart(callback_query.message)


# @dp.callback_query_handler(lambda c: c.data == 'clear_cart')
# async def clear_cart(callback_query: CallbackQuery):
#     cart = cart_data[0]
#     cart['items'] = []
#     cart['total_price'] = 0
#     await callback_query.answer("Cart cleared")
#     await send_cart(callback_query.message)


# @dp.callback_query_handler(lambda c: c.data == 'place_order')
# async def place_order(callback_query: CallbackQuery):
#     await callback_query.answer("Order placed!")
#     # Implement order placement logic here


# @dp.callback_query_handler(lambda c: c.data == 'back')
# async def go_back(callback_query: CallbackQuery):
#     await callback_query.answer("Back")
#     # Implement going back to the previous menu here
