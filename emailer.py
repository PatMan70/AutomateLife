import requests

# Specify the Mailgun API endpoint and credentials
MAILGUN_API_ENDPOINT = "YOUR_MAILGUN_API_ENDPOINT"
MAILGUN_API_KEY = 'YOUR_MAILGUN_API_KEY'

def send_email(to_email, email_subject, email_body):
    # Create a dictionary with the email data
    email_data = {
        'from': 'SENDER_EMAIL_ADDRESS',
        'to': to_email,
        'subject': email_subject,
        'text': email_body
    }

    # Send a POST request to the Mailgun API endpoint
    response = requests.post(
        MAILGUN_API_ENDPOINT,
        auth=('api', MAILGUN_API_KEY),
        data=email_data
    )

    # Check if the request was successful
    if response.status_code == 200:
        print('Email sent successfully!')
    else:
        print('An error occurred while sending the email.')

# Example usage
recipient_email = "RECIPIENT_EMAIL_ADDRESS"
email_subject = 'Hello'
email_body = 'Click the link button'
send_email(recipient_email, email_subject, email_body)
