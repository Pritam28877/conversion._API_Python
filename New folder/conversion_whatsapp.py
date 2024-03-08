import time
import json
import requests

# Define constants
API_VERSION = "v15.0"  # Update API version as needed
BASE_URL = f"https://graph.facebook.com/{API_VERSION}/"

def send_whatsapp_purchase_event(event_name,page_id, ctwa_clid, currency, value, dataset_id=None):
    """Sends a WhatsApp purchase event to Facebook Conversions API.

    Args:
        page_id: The Facebook Page ID.
        ctwa_clid: The click-to-whatsapp click ID.
        currency: The currency code (e.g., "USD").
        value: The value of the purchase.
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
        "data": [
            {
                "event_name": event_name,
                "event_time": event_time,
                "action_source": "business_messaging",
                "messaging_channel": "whatsapp",
                "user_data": {
                    "page_id": page_id,
                    "ctwa_clid": ctwa_clid
                },
                "custom_data": {
                    "currency": currency,
                    "value": value
                }
            }
        ]
    }

    # Send the POST request
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        print("Event sent successfully!")
    except requests.RequestException as e:
        print(f"Error sending event: {e}")

# Example usage (uncomment if needed)
# send_whatsapp_purchase_event("<PAGE_ID>", "ARAkLkA8rmlFeiCktEJQ-QTwRiyYHAFDLMNDBH0CD3qpjd0HR4irJ6LEkR7JwFF4XvnO2E4Nx0-eM-GABDLOPaOdRMv-_zfUQ2a", "USD", 123)
