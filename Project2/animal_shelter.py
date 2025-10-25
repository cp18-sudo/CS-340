# animal_shelter.py
from typing import Any, Dict, List, Optional
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db: str = "aac",
        collection: str = "animals",
        authSource: str = "admin",
        tls: Optional[bool] = None
    ) -> None:
        try:
            uri = os.getenv("MONGO_URI")
            if uri:
                self.client = MongoClient(uri, serverSelectionTimeoutMS=3000)
            else:
                kwargs = dict(
                    host=host, port=port, username=username, password=password,
                    authSource=authSource, serverSelectionTimeoutMS=3000
                )
                if tls is not None:
                    kwargs["tls"] = tls
                self.client = MongoClient(**kwargs)
            self.client.admin.command("ping")
            self.database = self.client[db]
            self.collection = self.database[collection]
        except Exception as e:
            raise ConnectionError(f"Mongo connection failed: {e}")

    def create(self, data: Dict[str, Any]) -> bool:
        if not isinstance(data, dict) or not data:
            raise ValueError("data must be a non-empty dict")
        try:
            r = self.collection.insert_one(data)
            return bool(r.acknowledged and r.inserted_id)
        except PyMongoError as e:
            print("Create error:", e)
            return False

    def read(
        self,
        query: Optional[Dict[str, Any]] = None,
        projection: Optional[Dict[str, int]] = None,
        sort: Optional[List] = None,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        q = query or {}
        if not isinstance(q, dict):
            raise ValueError("query must be a dict")
        try:
            cur = self.collection.find(q, projection)
            if sort:   cur = cur.sort(sort)
            if limit:  cur = cur.limit(int(limit))
            return list(cur)
        except PyMongoError as e:
            print("Read error:", e)
            return []

    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        if not isinstance(query, dict) or not isinstance(new_values, dict):
            raise ValueError("query and new_values must be dicts")
        if not new_values:
            raise ValueError("new_values must not be empty")
        try:
            r = self.collection.update_many(query, {"$set": new_values})
            return int(r.modified_count)
        except PyMongoError as e:
            print("Update error:", e)
            return 0

    def delete(self, query: Dict[str, Any]) -> int:
        if not isinstance(query, dict) or not query:
            raise ValueError("query must be a non-empty dict")
        try:
            r = self.collection.delete_many(query)
            return int(r.deleted_count)
        except PyMongoError as e:
            print("Delete error:", e)
            return 0

    def aggregate(self, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        try:
            return list(self.collection.aggregate(pipeline))
        except PyMongoError as e:
            print("Aggregate error:", e)
            return []