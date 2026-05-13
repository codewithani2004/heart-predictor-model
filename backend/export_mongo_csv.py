from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")
db_name = os.getenv("MONGO_DB")

# Connect to MongoDB
conn_str = f"mongodb+srv://{username}:{password}@{cluster}/{db_name}?retryWrites=true&w=majority"
client = MongoClient(conn_str)
db = client[db_name]

# Single export folder
export_folder = "export"
os.makedirs(export_folder, exist_ok=True)

# Export each collection to CSV in export folder
collections = db.list_collection_names()
for coll_name in collections:
    data = list(db[coll_name].find({}))
    if data:
        # Convert _id to string so CSV is readable
        for doc in data:
            doc["_id"] = str(doc["_id"])
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(export_folder, f"{coll_name}.csv"), index=False)
        print(f"Exported {coll_name}")
    else:
        print(f"No data in {coll_name}")

print("All collections exported to export/ folder!")
