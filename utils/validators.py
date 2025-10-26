def validate_payload(body):
    required_fields = ["receiver_email", "subject", "body_text"]

    for field in required_fields:
        if field not in body or not body[field].strip():
            return False, f"{field} is required"

    if "@" not in body["receiver_email"]:
        return False, "Invalid email format"

    return True, None
