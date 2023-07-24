import pandas as pd
from pymongo import MongoClient
import json5
from os.path import exists
from os import mkdir


def getJson():
    with open("./config.jsonc") as file:
        jsonContent = json5.load(file)
        file.close()

    return jsonContent


def main():
    jsonContent = getJson()

    connectionString = jsonContent["connectionString"]
    database = jsonContent["database"]
    collectionName = jsonContent["collection"]
    directory = jsonContent["directory"]

    client = MongoClient(connectionString)
    db = client.get_database(database)
    collection = db.get_collection(collectionName)

    df = pd.DataFrame(collection.find())

    if not exists(directory):
        print("Directory does not exist, creating...")
        mkdir(directory)

    df.to_csv(f"{directory}/{collectionName}.csv")

    client.close()

    print("Saved!")


if __name__ == "__main__":
    main()
