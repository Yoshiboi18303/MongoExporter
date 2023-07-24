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
    client = MongoClient(jsonContent.connectionString)
    db = client.get_database(jsonContent.database)
    collection = db.get_collection(jsonContent.collection)

    df = pd.DataFrame(collection.find())

    if not exists(jsonContent.directory):
        print("Directory does not exist, creating...")
        mkdir(jsonContent.directory)

    df.to_csv(f"{jsonContent.directory}/{jsonContent.collection}.csv")

    client.close()

    print("Saved!")


if __name__ == "__main__":
    main()
