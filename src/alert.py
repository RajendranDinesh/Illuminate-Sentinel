from twilio.rest import Client

account_sid = 'AC45802ac684dd136942dca66acb1ac263'
auth_token = 'a63bc145f21a3371e73937ee40896cc9'

def send_alert(camera_number, image_path, video_id):
    # Format the message
    message = f'ALERT: Light source detected by camera {camera_number} at {video_id}'

    # Send the message using the WhatsApp Business API
    client = Client(account_sid, auth_token)

    response = client.messages.create(
        from_ = "whatsapp:+14155238886",
        to = 'whatsapp:+917010757200',
        media_url=[f'{image_path}'],
        body = message)

    # Check if the message was sent successfully
    if response.status != 'sent' and response.status != 'queued':
        raise ValueError(f'Failed to send message: {response.error_code}')

#sid - SKfa0a7db00162f1617ad78d435d1a5d9b
#secret - youf1Tkn7dqevioUlKUQY82XYFRv1d3B