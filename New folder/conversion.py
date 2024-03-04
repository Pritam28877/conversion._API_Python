import requests
import hashlib  # For hashing user data (optional)
import time  # To get the current timestamp

# Replace with your actual values
PIXEL_ID = 3586640601600069
ACCESS_TOKEN = "EAANqH0ZAEJZA4BO15sEtn0hBdvPcLY3PO7rXFISEi0RGuZCaLDBZC91LxNJJwnh1SsErv5XsM53g5u8AWRa5X1BZC1ZBuJGeWBwheK4ZAvnwabMZB5SsxtkMrwudmII9PCcuE82gvqhMbx9T2HUrOzrUKKf8ZA1hxatU9s1VtHhYfYU5f28FWjDZCTE1harujBEQZDZD"

# Event details
EVENT_NAME = "TestEvent2"
EVENT_ID = int(time.time() * 1000)  # Unique event ID using current timestamp
USER_DATA = {
    "client_ip_address": "254.254.254.254",
    "client_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
}
TEST_DATA1 = "value1"
TEST_DATA2 = 42
TEST_DATA3 = True
TEST_EVENT_CODE = "TEST25082"

# Function to hash user data (optional)
def hash_user_data(data):
    hashed_data = {}
    for key, value in data.items():
        hashed_data[key] = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return hashed_data

# Hash user data (optional, uncomment if needed)
# USER_DATA = hash_user_data(USER_DATA)

# Construct the event payload
event_data = {
    "data": [
        {
            "action_source": "website",
            "event_id": EVENT_ID,
            "event_name": EVENT_NAME,
            "event_time": int(time.time()),  # Use current timestamp
            "user_data": USER_DATA,
            "test_data1": TEST_DATA1,
            "test_data2": TEST_DATA2,
            "test_data3": TEST_DATA3,
        }
    ],
    "test_event_code": TEST_EVENT_CODE,
}

# Set the API endpoint URL
url = f"https://graph.facebook.com/v13.0/{PIXEL_ID}/events"

# Set headers with authorization
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}

# Send the POST request
try:
    response = requests.post(url, headers=headers, json=event_data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    print("Event sent successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error sending event: {e}")
