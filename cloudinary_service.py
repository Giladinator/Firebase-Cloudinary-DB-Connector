from dotenv import load_dotenv
load_dotenv()

import cloudinary.api
import cloudinary.uploader
import cloudinary

config = cloudinary.config(secure=True)

# Get all images from Cloudinary 
def getData():
    # Get image details and save it in the variable 'image_url'.
    image_url = cloudinary.Search()\
        .expression("resource_type:image")\
        .sort_by("public_id", "desc")\
        .execute()

    # Create array of images objects containing folder, url, filename 
    url_to_upload = []
    for url in image_url['resources']:
        url_to_upload.append(
            {"folder": url["folder"], "image_url": url["url"], "filename": url["filename"]})
    return url_to_upload
    # print(json.dumps(url_list, indent=4))
    # print(url_list)