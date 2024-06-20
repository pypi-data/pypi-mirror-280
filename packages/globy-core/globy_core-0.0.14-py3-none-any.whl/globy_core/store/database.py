from abc import ABC, abstractmethod
from typing import Optional, Dict, List
import datetime
from pymongo import MongoClient, DESCENDING

class GlobyDatabase(ABC):
    @abstractmethod
    def add_item(self, item: Dict) -> None:
        """Add a new item to the collection."""
        pass

    @abstractmethod
    def get_latest_item(self, filter: Dict) -> Optional[Dict]:
        """Get the last item based on the index that matches the filter."""
        pass

    @abstractmethod
    def get_latest_item_bytime(self, filter: Dict) -> Optional[Dict]:
        """Get the most recently added item that matches the filter."""
        pass

    @abstractmethod
    def delete_item(self, filter: Dict) -> None:
        """Delete the first item that matches the filter."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the collection is empty."""
        pass

    @abstractmethod
    def get_all_items(self, filter: Dict) -> List[Dict]:
        """Get all items that match the filter."""
        pass

    @abstractmethod
    def delete_all_items(self, filter: Dict) -> None:
        """Delete all items that match the filter."""
        pass

class MongoDBCollection(GlobyDatabase):
    def __init__(self, database_name: str, collection_name: str, host='localhost', port=27017):
        self._client = MongoClient(host, port)
        self._db = self._client[database_name]
        self._collection = self._db[collection_name]

    def add_item(self, item: Dict) -> None:
        """Add a new item to the collection with a timestamp."""
        item['_timestamp'] = datetime.datetime.now(datetime.UTC)  # Add a timestamp to each item
        self._collection.insert_one(item)

    def get_latest_item(self, filter: Dict) -> Optional[Dict]:
        """Get the last item based on the index that matches the filter."""
        cursor = self._collection.find(filter).sort([("$natural", -1)]).limit(1)
        return cursor.next() if cursor.count() > 0 else None

    def get_latest_item_bytime(self, filter: Dict) -> Optional[Dict]:
        """Get the most recently added item that matches the filter."""
        cursor = self._collection.find(filter).sort('_timestamp', DESCENDING).limit(1)
        return cursor.next() if cursor.count() > 0 else None

    def delete_item(self, filter: Dict) -> None:
        """Delete the first item that matches the filter."""
        self._collection.delete_one(filter)

    def is_empty(self) -> bool:
        """Check if the collection is empty."""
        return self._collection.count_documents({}) == 0

    def get_all_items(self, filter: Dict) -> List[Dict]:
        """Get all items that match the filter."""
        return list(self._collection.find(filter))

    def delete_all_items(self, filter: Dict) -> None:
        """Delete all items that match the filter."""
        self._collection.delete_many(filter)

class DynamoDBDatabase(GlobyDatabase):
    pass

# Example Usage
if __name__ == "__main__":
    db_collection = MongoDBCollection(database_name='mydb', collection_name='mycollection')

    # Add an item
    db_collection.add_item({'key': 'value1'})

    # Fetch the last item based on the index for the key
    latest_item = db_collection.get_latest_item({'key': 'value1'})
    print(latest_item)

    # Fetch the most recently added item for the key
    latest_item_bytime = db_collection.get_latest_item_bytime({'key': 'value1'})
    print(latest_item_bytime)

    # Get all items for the key
    all_items = db_collection.get_all_items({'key': 'value1'})
    print(all_items)

    # Delete all items for the key
    db_collection.delete_all_items({'key': 'value1'})

    # Check if the collection is empty
    is_empty = db_collection.is_empty()
    print(is_empty)
