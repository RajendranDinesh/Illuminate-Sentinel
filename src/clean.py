import cloudinary
import cloudinary.api
import datetime

cloudinary.config(
  cloud_name = "dx8tcppmo",
  api_key = "645359463232894",
  api_secret = "Cfo0v_3uCbBW9oz2rWA2vRxhEIU"
)

def delete_old_files():
    # Get a list of all resources stored in Cloudinary
    result = cloudinary.api.resources(resource_type = 'video', max_results = 50)
    tbd = []
    for resource in result['resources']:
        # Get the timestamp of the file creation
        created_at = resource['created_at']
        created_at = created_at.replace('T', ' ')
        created_at = created_at.replace('Z', '')
        # Convert the timestamp to a datetime object
        created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        # Calculate the difference between now and the file creation time
        delta = datetime.datetime.now() - created_at
        # If the file was created more than 7 days ago, delete it
        if delta.days >= 2:
            tbd.append(resource['public_id'])

    print(cloudinary.api.delete_resources(tbd, resource_type='video'))

delete_old_files()