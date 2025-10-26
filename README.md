# Serverless-Email-API

A simple Serverless (AWS Lambda) REST API that sends transactional emails using Brevo (Sendinblue).
Built in Python, with local development support via serverless-offline.

Function: `POST /send-mail`

## What this does

This project exposes a serverless endpoint that accepts a JSON payload with `receiver_email`, `subject`, and `body_text`, then sends an email using Brevo’s transactional email API. It includes basic input validation and maps API errors to appropriate HTTP status codes.

## Prerequisites
Make sure you have these installed on your machine:

* Node.js (v16+ recommended) and npm
* Python 3.9+
* serverless CLI (installed globally)
* pip (Python package installer)
* (Optional) Postman or Thunder Client for testing

You will also need a Brevo (Sendinblue) account and an API (v3) key.

## Setup — step by step
### 1. Clone the repo
```
git clone https://github.com/deepshikha04yadav/Serverless-Email-API.git
cd Serverless-Email-API
```
### 2. Install Serverless CLI (global)

If you haven't installed the Serverless Framework CLI:
```
npm install -g serverless
# or
npm i -g @serverless/cli
```

Confirm:
```
sls --version
```

### 3. Install project Node plugins (serverless-offline)

Inside the repo:
```
npm init -y      
npm install --save-dev serverless-offline
```

Important: `serverless-offline` must be listed under `plugins:` in `serverless.yml`:
```
plugins:
  - serverless-offline
```
### 4. Create & activate Python virtualenv + install deps

Create a virtual environment and install the Python dependencies:
```
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

### 5. Configure environment variables (.env)

Create a .env file in repo root:
```
BREVO_API_KEY=your_brevo_api_key_here
```

### 6. Run locally with serverless-offline

Start the local server:
```
sls offline
# or
serverless offline
```

You should see output indicating the local endpoints, for example:
```
POST http://localhost:3000/dev/send-mail
```
### 7. Test with curl / Postman / Thunder Client
#### Postman / Thunder Client

* Method: POST

* URL: http://localhost:3000/dev/send-mail

* Body → raw → JSON:
```
{
  "receiver_email": "recipient@example.com",
  "subject": "Hello",
  "body_text": "This is a test email"
}
```

## Error handling & expected responses

The API implements basic validation and maps results:

* 200 OK — Email sent successfully
  ```
  { "message": "Email sent successfully" }
  ```

* 400 Bad Request — Missing/invalid fields
  ```
  { "error": "receiver_email is required" }
  ```

* 500 Internal Server Error — Unexpected failure or provider error
  ```
  { "error": "Failed to send email: <provider error text>" }
  ```

Brevo-specific errors (quota, invalid API key, unverified sender) will appear in the 4xx/5xx responses from the Brevo SDK and are passed back (or wrapped) by the handler.
