import pymongo
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(f"{os.environ['MONGODB_CONN_STRING']}")
                
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
        