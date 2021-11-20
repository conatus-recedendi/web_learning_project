from pymongo import MongoClient

client = MongoClient('mongodb://myUserAdmin:pwd@localhost:27017')

db = client['baedalgeek_test']

collection = db['Users']

def create(name, age):
	json = {
		"name": name,
		"age": age,
	}
	collection.insert_one(json)

if __name__ == '__main__':
	create("kylee", 42)
