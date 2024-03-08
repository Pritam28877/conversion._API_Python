import time
import json
import requests
import hashlib

# Define constants
API_VERSION = "v15.0"  # Update API version as needed
BASE_URL = f"https://graph.facebook.com/{API_VERSION}/"

def send_offline_event(event_name, currency, value, custom_data, order_id, item_id, contact, dataset_id=None):
    """Sends an offline event to Facebook Conversions API.

    Args:
        event_name: The name of the offline event (e.g., "Purchase").
        currency: The currency code (e.g., "INR").
        value: The value of the purchase.
        custom_data: A dictionary containing item details.
        order_id: The order ID.
        item_id: The item ID.
        dataset_id: The ID of the dataset associated with the event (optional).
    """

    # Set the endpoint URL
    url = f"{BASE_URL}{dataset_id}/events" if dataset_id else f"{BASE_URL}me/events"

    # Set headers with access token and content type
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your access token
    headers = {"Content-Type": "application/json"}

    # Capture user input for all parameters
    event_time = int(time.time())  # Current time as event time

    # Prepare data payload
    data = {
        "action_source": "physical_store",  # Set action_source as per documentation
        "event_name": event_name,
        "event_time": event_time,
        "user_data": {
            "em": [hashlib.sha256(contact['email'].encode()).hexdigest()],
            "ph": [hashlib.sha256(contact['phone'].encode()).hexdigest()]
        },
        "custom_data": {
            "currency": currency,
            "value": value,
            "custom_data": custom_data,
            "order_id": order_id,
            "item_id": item_id
        }
    }

    # Send the POST request
    try:
        response = requests.post(url, headers=headers, json={"data": [data]})
        response.raise_for_status()  # Raise an exception for non-200 status codes
        print("Event sent successfully!")
    except requests.RequestException as e:
        print(f"Error sending event: {e}")

# Example usage (uncomment if needed)
# send_offline_event("Purchase", "INR", 123.45, {"email": "user@example.com", "phone": "1234567890", "contents": [{"id": "product123", "quantity": 1}]}, "order123", "item123", "<DATASET_ID>")
