from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin


# Set your firebase credentials
# ==============================
cred = credentials.Certificate("service-account-file.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# upload to firebase
def upload_firebase(new_photos):
    for image in new_photos:
        db.collection("photos").add(image)



def getData():
    firebase_collection = []
    docs = db.collection(u'photos').stream()
    for doc in docs:
        doc = doc.to_dict()        
        firebase_collection.append(doc)
    return firebase_collection