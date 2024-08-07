import requests


def get_cart_items_by_tg_id(url, telegram_id):
    carts_url = f"{url}/carts/"
    # print(url)
    # print(carts_url)
    # print("^" * 100)
    response = requests.get(carts_url, params={'user__telegram_id': telegram_id})

    if response.status_code == 200:
        cart_data = response.json()
        return cart_data
    else:
        return f"Failed to retrieve data: {response.status_code}"


# telegram_id = "959991268"
# get_cart_items_by_tg_id(telegram_id)


# cart_data = [{'id': '349ad751-2475-4be2-9a61-de6ccd097972', 'items': [{'id': 1, 'product': {'id': 2, 'title': 'test2', 'unit_price': 40000.0}, 'quantity': 1, 'total_price': 40000.0}, {'id': 2, 'product': {'id': 1, 'title': 'test2', 'unit_price': 50000.0}, 'quantity': 2, 'total_price': 100000.0}], 'total_price': 140000.0, 'user': {'telegram_id': 995991268, 'username': 'Benjamin Dusse', 'first_name': 'Benjamin', 'last_name': 'Dusse', 'phone_number': '880378151'}}]

# print(cart_data[0]['total_price'])
