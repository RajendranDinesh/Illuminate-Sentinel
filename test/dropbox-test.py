from twilio.rest import Client
import time as t
import dropbox
from dropbox.exceptions import AuthError
import pathlib

DROPBOX_ACCESS_TOKEN = 'sl.BYK8kQ7GqZq2MQZxcOXeVLo8CizOUtWwPTIwWTzXBPa55GI8rVutVfkEDbsIl1xn1z9_SDiA5DDOmp1M8AHVTF8PK4bQl-6n2S5sC64W2onfVB5CoFepwequAGurM5mAzJFyDwI2'

account_sid = 'AC45802ac684dd136942dca66acb1ac263'
auth_token = 'a63bc145f21a3371e73937ee40896cc9'


def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx

def dropbox_upload_file(local_path, local_file, dropbox_file_path):
    """Upload a file from the local machine to a path in the Dropbox app directory.

    Args:
        local_path (str): The path to the local file.
        local_file (str): The name of the local file.
        dropbox_file_path (str): The path to the file in the Dropbox app directory.

    Example:
        dropbox_upload_file('.', 'test.csv', '/stuff/test.csv')

    Returns:
        meta: The Dropbox file metadata.
    """

    try:
        dbx = dropbox_connect()

        local_file_path = pathlib.Path(local_path) / local_file

        with local_file_path.open("rb") as f:
            meta = dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))

            return meta
    except Exception as e:
        print('Error uploading file to Dropbox: ' + str(e))

def dropbox_get_link(dropbox_file_path):
    """Get a shared link for a Dropbox file path.

    Args:
        dropbox_file_path (str): The path to the file in the Dropbox app directory.

    Returns:
        link: The shared link.
    """

    try:
        dbx = dropbox_connect()
        shared_link_metadata = dbx.sharing_create_shared_link(dropbox_file_path)
        shared_link = shared_link_metadata.url
        return shared_link.replace('?dl=0', '?dl=0')
    except dropbox.exceptions.ApiError as exception:
        if exception.error.is_shared_link_already_exists():
            shared_link_metadata = dbx.sharing_get_shared_links(dropbox_file_path)
            shared_link = shared_link_metadata.links[0].url
            return shared_link.replace('?dl=0', '?dl=0')

def send_alert(camera_number, image_path, time):

    # Send the message using the WhatsApp Business API
    client = Client(account_sid, auth_token)

    name = image_path[29:59]
    name = name + '.mp4'
    db_path = '/ForestProject/'+name


    dropbox_upload_file('E:/ForestProject/data/videos', name, db_path)
    link = dropbox_get_link('/ForestProject/'+ name)

    message = f'ALERT: Light source detected by camera {camera_number} at {time[11:19]} on {time[0:10]} {link}'

    response = client.messages.create(
        from_ = "whatsapp:+14155238886",
        to = 'whatsapp:+917010757200',
        force_delivery=True,
        body = message)
    
    t.sleep(1)

    print(response.status)

    # Check if the message was sent successfully
    if response.status != 'sent' and response.status != 'queued':
        raise ValueError(f'Failed to send message: {response.error_code}')

#sid - SKfa0a7db00162f1617ad78d435d1a5d9b
#secret - youf1Tkn7dqevioUlKUQY82XYFRv1d3B