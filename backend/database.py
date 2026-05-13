# from dotenv import load_dotenv
# import os
# from urllib.parse import quote_plus
# from motor.motor_asyncio import AsyncIOMotorClient

# # Load environment variables
# env_path = os.path.join(os.path.dirname(__file__), ".env")
# load_dotenv(dotenv_path=env_path)

# mongo_user = os.getenv("MONGO_USERNAME")
# mongo_pass = os.getenv("MONGO_PASSWORD")
# mongo_db = os.getenv("MONGO_DB")
# mongo_cluster = os.getenv("MONGO_CLUSTER")

# if not all([mongo_user, mongo_pass, mongo_db, mongo_cluster]):
#     raise RuntimeError("❌ MongoDB env vars not loaded (.env missing or wrong)")

# # Encode special characters
# username = quote_plus(str(mongo_user))
# password = quote_plus(str(mongo_pass))

# MONGO_URL = (
#     f"mongodb+srv://{username}:{password}"
#     f"@{mongo_cluster}/{mongo_db}"
#     "?retryWrites=true&w=majority"
# )

# # Connect with a short timeout to detect connection issues fast
# client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
# db = client[mongo_db]
# collection = db["patients"]



from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient

# Load .env file (backend folder)
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

# Support BOTH old and new env styles
mongo_user = os.getenv("MONGO_USERNAME")
mongo_pass = os.getenv("MONGO_PASSWORD")
mongo_db = os.getenv("MONGO_DB")

# fallback support (optional safety)
mongo_uri = os.getenv("MONGO_URI")

# If URI exists → use simple connection
if mongo_uri:
    client = AsyncIOMotorClient(mongo_uri, serverSelectionTimeoutMS=5000)
    db = client.get_default_database() if mongo_db is None else client[mongo_db]
    collection = db["patients"]

else:
    # If using split credentials
    mongo_cluster = os.getenv("MONGO_CLUSTER")

    if not all([mongo_user, mongo_pass, mongo_db, mongo_cluster]):
        raise RuntimeError("❌ MongoDB env vars not loaded (.env missing or wrong)")

    username = quote_plus(str(mongo_user))
    password = quote_plus(str(mongo_pass))

    MONGO_URL = (
        f"mongodb+srv://{username}:{password}"
        f"@{mongo_cluster}/{mongo_db}"
        "?retryWrites=true&w=majority"
    )

    client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    db = client[mongo_db]
    collection = db["patients"]