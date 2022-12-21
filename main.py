import json
import firebase_service
import cloudinary_service
import dict_operations

# ==============================

def main():
    cloudinary_data = cloudinary_service.getData()
    firebase_data = firebase_service.getData()
    results = dict_operations.DictListUpdate(cloudinary_data,firebase_data)
    print(json.dumps(results,indent=2))
    firebase_service.upload_firebase(results)
main()
