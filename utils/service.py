import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from dotenv import load_dotenv

load_dotenv()

def send_email(receiver_email, subject, body_text):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ["BREVO_API_KEY"]

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": receiver_email}],
        subject=subject,
        text_content=body_text,
        sender={"name": "Serverless API", "email": "youremail@domain.com"}
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        raise Exception(f"Failed to send email: {e}")
