from pymongo import MongoClient

uri = "mongodb+srv://cluster0.wzawa.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='/Users/ikane/Dropbox/DEV/mongo/X509-cert-7069374346259977441.pem')

db = client['business']
collection = db['reviews']
doc_count = collection.count_documents({})
print(doc_count)
