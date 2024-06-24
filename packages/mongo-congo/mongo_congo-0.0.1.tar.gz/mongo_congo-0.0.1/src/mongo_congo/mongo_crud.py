from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import Union


class mongo_connect:
    def __init__(self, url: str, database_name: str, collection_name: str):
        self.url: str = url
        self.database_name: str = database_name
        self.collection_name: str = collection_name
        self.client: MongoClient = MongoClient(self.url)  # Type annotation added here
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def insert_record(self, record: Union[dict, list]):
        if isinstance(record, list):
            for r in record:
                if not isinstance(r, dict):
                    raise TypeError("Each element in the list must be a dictionary")
            self.collection.insert_many(record)
        elif isinstance(record, dict):
            self.collection.insert_one(record)
        else:
            raise TypeError("Record must be a dictionary or a list of dictionaries")
