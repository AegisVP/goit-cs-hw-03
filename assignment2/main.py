import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

def create_connection():
    uri = "mongodb+srv://" + config['MONGODB_USER'] + ":" + config['MONGODB_PASS'] + "@cluster0.aesnroa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    print(f"Connecting to: {uri}")

    client = pymongo.MongoClient(uri)

    try:
        client.admin.command('ping')
    except Exception as e:
        print(f"Error connecting to database server: {e}")
        raise e
    
    return client

def read_all_data(db, collection):
    return list(db[collection].find())

def read_data(db, collection, query):
    return list(db[collection].find(query))

def insert_data(db, collection, data):
    db[collection].insert_one(data)

def update_age(db, collection, query, new_age):
    db[collection].update_one(query, {'$set': {'age': new_age}})

def add_feature(db, collection, query, new_feature):
    features = db[collection].find_one(query)['features']
    if (new_feature not in features):
        features.append(new_feature)
    db[collection].update_one(query, {'$set': {'features': features}})

def delete_entry(db, collection, query):
    db[collection].delete_one(query)

def purge_collection(db, collection):
    db[collection].delete_many({})

def print_data(db, collection):
    data_list = read_all_data(db, collection)
    print(data_list)

if __name__ == "__main__":
    client = create_connection()
    db = client[config['MONGODB_NAME']]
    collection = config['MONGODB_COLLECTION']
    print('\nInitial DB state:')
    print_data(db, collection)

    barsik = {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }

    murchik = {
        "name": "murchik",
        "age": 2,
        "features": ["ходить в лоток", "муркотить", "сірий"]
    }

    print('\nInserting "barsik" and "murchik":')
    insert_data(db, collection, barsik)
    insert_data(db, collection, murchik)
    print_data(db, collection)

    search_term = {"name": "barsik"}
    print('\nSearching for "barsik":')
    print(read_data(db, collection, search_term))

    print('\nUpdating "barsik"\'s age to 5:')
    update_age(db, collection, search_term, 5)
    print_data(db, collection)

    print('\nAdding "муркотить" to "barsik":')
    add_feature(db, collection, search_term, 'муркотить')
    print_data(db, collection)

    print('\nDeleting "barsik":')
    delete_entry(db, collection, search_term)
    print_data(db, collection)

    print('\nPurging collection:')
    purge_collection(db, collection)
    print_data(db, collection)