from twilio.rest import Client
import time as t
import cloudinary
import cloudinary.uploader


account_sid = 'AC45802ac684dd136942dca66acb1ac263'
auth_token = 'a63bc145f21a3371e73937ee40896cc9'

def send_alert(camera_number, image_path, time):

    # Send the message using the WhatsApp Business API
    client = Client(account_sid, auth_token)

    cloudinary.config(
        cloud_name = "dx8tcppmo",
        api_key = "645359463232894",
        api_secret = "Cfo0v_3uCbBW9oz2rWA2vRxhEIU"
        )
    
    name = image_path[28:57]
    up = cloudinary.uploader.upload_large(f'{image_path}', resource_type = "video", public_id=f"Detected/{name}", )
    link = up['secure_url'][0:49] + '/vc_auto' + up['secure_url'][61:]

    # Format the message
    message = f'ALERT: Light source detected by camera {camera_number} at {time[11:19]} on {time[0:10]}\n\n{link}'

    response = client.messages.create(
        from_ = "whatsapp:+14155238886",
        to = 'whatsapp:+917010757200',
        force_delivery=True,
        body = message)
    
    t.sleep(1)

    # Check if the message was sent successfully
    if response.status != 'sent' and response.status != 'queued':
        raise ValueError(f'Failed to send message: {response.error_code}')

#sid - SKfa0a7db00162f1617ad78d435d1a5d9b
#secret - youf1Tkn7dqevioUlKUQY82XYFRv1d3B