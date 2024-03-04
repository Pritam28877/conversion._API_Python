import time
import requests

# Define the event data
event_data = {
    "data": [
        {
            "action_source": "website",
            "event_id": 123458,
            "event_name": "TestEvent",
            "event_time": 1709302732,
            "user_data": {
                "client_ip_address": "254.254.254.254",
                "client_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
                "em": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
            }
        }
    ],
    "test_event_code": "TEST96290"
}

# Set the API endpoint URL
PIXEL_ID = 3586640601600069
url = f"https://graph.facebook.com/v13.0/{PIXEL_ID}/events?test_event_code={event_data['test_event_code']}"

# Set headers with authorization
ACCESS_TOKEN = "EAANqH0ZAEJZA4BO15sEtn0hBdvPcLY3PO7rXFISEi0RGuZCaLDBZC91LxNJJwnh1SsErv5XsM53g5u8AWRa5X1BZC1ZBuJGeWBwheK4ZAvnwabMZB5SsxtkMrwudmII9PCcuE82gvqhMbx9T2HUrOzrUKKf8ZA1hxatU9s1VtHhYfYU5f28FWjDZCTE1harujBEQZDZD"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}

# Send the POST request
try:
    response = requests.post(url, headers=headers, json=event_data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    print("Event sent successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error sending event: {e}")