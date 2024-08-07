import requests

# Replace with your actual API URL
url = "http://127.0.0.1:8000/carts/"

# Replace with the actual telegram_id you want to filter by
telegram_id = "959991268"

# Send a GET request to the API with the telegram_id filter
response = requests.get(url, params={'user__telegram_id': telegram_id})

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response
    cart_data = response.json()
    print(cart_data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

