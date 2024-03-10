def get_ctwa_clid(webhook_payload):
    """
    Extracts the ctwa_clid from the WhatsApp webhook notification payload.

    Args:
        webhook_payload (dict): The webhook notification payload received from WhatsApp.

    Returns:
        str or None: The ctwa_clid if found, None otherwise.
    """
    try:
        # Extract relevant data from the payload
        entries = webhook_payload.get("entry", [])
        if entries:
            for entry in entries:
                changes = entry.get("changes", [])
                if changes:
                    for change in changes:
                        value = change.get("value", {})
                        metadata = value.get("metadata", {})
                        user_data = metadata.get("user_data", {})
                        ctwa_clid = user_data.get("ctwa_clid")
                        if ctwa_clid:
                            return ctwa_clid
    except Exception as e:
        print(f"Error extracting ctwa_clid: {e}")
    return None

# Example usage:
# webhook_payload = {...}  # Replace with the actual webhook payload
# ctwa_clid = get_ctwa_clid(webhook_payload)
# print(ctwa_clid)
