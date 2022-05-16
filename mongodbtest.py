from pymongo import MongoClient
from pprint import pprint

url="mongodb+srv://developer:xxxxxxx@cluster0.wzawa.mongodb.net/testdb?retryWrites=true&w=majority"
client = MongoClient(url)
db=client.admin
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
