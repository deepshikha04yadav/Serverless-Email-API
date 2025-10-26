import json
from utils.validators import validate_payload
from utils.service import send_email

def send_mail(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        is_valid, error = validate_payload(body)

        if not is_valid:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": error})
            }

        send_email(
            body["receiver_email"],
            body["subject"],
            body["body_text"]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
