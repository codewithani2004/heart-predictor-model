# from fastapi import FastAPI, Response
# from fastapi.middleware.cors import CORSMiddleware
# from joblib import load
# from pydantic import BaseModel
# from datetime import datetime
# import pandas as pd
# from pathlib import Path
# import os

# # ✅ MongoDB connection
# from database import collection  # your database.py must have `collection = db["patients"]`

# # -------------------- FastAPI Setup --------------------
# app = FastAPI(
#     title="Heart Disease Prediction API",
#     description="Predict heart disease and store real-time data in MongoDB"
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # change to your frontend URL in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------- Pydantic Request Model --------------------
# class HeartDiseaseRequest(BaseModel):
#     age: int
#     sex: int
#     cp: int
#     trestbps: int
#     chol: int
#     fbs: int
#     restecg: int
#     thalach: int
#     exang: int
#     oldpeak: float
#     slope: int
#     ca: int
#     thal: int

# # -------------------- Load ML Model --------------------
# MODEL_PATH = Path(__file__).parent / "models" / "heart_model.joblib"
# model = load(MODEL_PATH)

# # -------------------- Routes --------------------
# @app.get("/")
# def home():
#     return {"message": "Heart Disease Prediction API is running ✅"}

# @app.get("/mongo-status")
# async def mongo_status():
#     """Check MongoDB connection"""
#     try:
#         await collection.database.client.admin.command("ping")
#         return {"mongo": "connected ✅"}
#     except Exception as e:
#         return {"mongo": f"not connected ❌: {e}"}

# # @app.post("/predict")
# # async def predict(input_data: HeartDiseaseRequest):
# #     features = [[
# #         input_data.age,
# #         input_data.sex,
# #         input_data.cp,
# #         input_data.trestbps,
# #         input_data.chol,
# #         input_data.fbs,
# #         input_data.restecg,
# #         input_data.thalach,
# #         input_data.exang,
# #         input_data.oldpeak,
# #         input_data.slope,
# #         input_data.ca,
# #         input_data.thal
# #     ]]

# #     prediction = int(model.predict(features)[0])
# #     probability = float(model.predict_proba(features)[0][1])

# #     document = {
# #         "inputData": input_data.dict(),
# #         "prediction": prediction,
# #         "probability": probability,
# #         "createdAt": datetime.utcnow()
# #     }

# from datetime import datetime

# @app.post("/predict")
# async def predict(input_data: HeartDiseaseRequest):

#     features = [[
#         input_data.age,
#         input_data.sex,
#         input_data.cp,
#         input_data.trestbps,
#         input_data.chol,
#         input_data.fbs,
#         input_data.restecg,
#         input_data.thalach,
#         input_data.exang,
#         input_data.oldpeak,
#         input_data.slope,
#         input_data.ca,
#         input_data.thal
#     ]]

#     # 🔥 prediction
#     prediction = int(model.predict(features)[0])
#     probability = float(model.predict_proba(features)[0][1])

#     # 🔥 response return (IMPORTANT)
#     result = {
#         "prediction": prediction,
#         "probability": probability,
#         "createdAt": datetime.utcnow()
#     }

#     return result
#     # ✅ Prevent duplicate entries
#     exists = await collection.find_one({"inputData": input_data.dict()})
#     if not exists:
#         await collection.insert_one(document)

#     return {
#         "prediction": prediction,
#         "probability": probability
#     }

# @app.get("/export-csv")
# async def export_csv():
#     """Export all stored predictions as CSV"""
#     docs = await collection.find({}).to_list(length=10000)

#     if not docs:
#         return {"message": "No prediction data found"}

#     rows = []
#     for item in docs:
#         row = item["inputData"]
#         row["prediction"] = item["prediction"]
#         row["probability"] = item["probability"]
#         row["createdAt"] = item["createdAt"]
#         rows.append(row)

#     df = pd.DataFrame(rows)
#     csv_data = df.to_csv(index=False)
#     headers = {"Content-Disposition": "attachment; filename=predictions.csv"}

#     return Response(content=csv_data, media_type="text/csv", headers=headers)

# # -------------------- Startup Event --------------------
# @app.on_event("startup")
# async def startup_event():
#     try:
#         await collection.database.client.admin.command("ping")
#         print("MongoDB connected successfully ✅")
#     except Exception as e:
#         print(f"MongoDB connection failed ❌: {e}")

# # -------------------- Run Server --------------------
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



# from fastapi import FastAPI, Response
# from fastapi.middleware.cors import CORSMiddleware
# from joblib import load
# from pydantic import BaseModel
# from datetime import datetime
# import pandas as pd
# from pathlib import Path

# # MongoDB
# from database import collection

# # -------------------- FastAPI --------------------
# app = FastAPI(
#     title="Heart Disease Prediction API",
#     description="Predict heart disease and store real-time data in MongoDB"
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------- Request Model --------------------
# class HeartDiseaseRequest(BaseModel):
#     age: int
#     sex: int
#     cp: int
#     trestbps: int
#     chol: int
#     fbs: int
#     restecg: int
#     thalach: int
#     exang: int
#     oldpeak: float
#     slope: int
#     ca: int
#     thal: int

# # -------------------- Load Model --------------------
# MODEL_PATH = Path(__file__).parent / "models" / "heart_model.joblib"
# model = load(MODEL_PATH)

# # -------------------- Home --------------------
# @app.get("/")
# def home():
#     return {"message": "Heart Disease Prediction API is running ✅"}

# # -------------------- Mongo Status --------------------
# @app.get("/mongo-status")
# async def mongo_status():
#     try:
#         await collection.database.client.admin.command("ping")
#         return {"mongo": "connected ✅"}
#     except Exception as e:
#         return {"mongo": f"not connected ❌: {e}"}

# # -------------------- PREDICT (MAIN FIXED) --------------------
# @app.post("/predict")
# async def predict(input_data: HeartDiseaseRequest):

#     features = [[
#         input_data.age,
#         input_data.sex,
#         input_data.cp,
#         input_data.trestbps,
#         input_data.chol,
#         input_data.fbs,
#         input_data.restecg,
#         input_data.thalach,
#         input_data.exang,
#         input_data.oldpeak,
#         input_data.slope,
#         input_data.ca,
#         input_data.thal
#     ]]

#     # ML Prediction
#     prediction = int(model.predict(features)[0])
#     probability = float(model.predict_proba(features)[0][1])

#     # Document for MongoDB
#     document = {
#         "inputData": input_data.dict(),
#         "prediction": prediction,
#         "probability": probability,
#         "createdAt": datetime.utcnow()
#     }

#     # Save to MongoDB
#     await collection.insert_one(document)

#     return {
#         "prediction": prediction,
#         "probability": probability,
#         "createdAt": datetime.utcnow()
#     }

# # -------------------- EXPORT CSV --------------------
# @app.get("/export-csv")
# async def export_csv():

#     docs = await collection.find({}).to_list(length=10000)

#     if not docs:
#         return {"message": "No data found"}

#     rows = []
#     for item in docs:
#         row = item["inputData"]
#         row["prediction"] = item["prediction"]
#         row["probability"] = item["probability"]
#         row["createdAt"] = item["createdAt"]
#         rows.append(row)

#     df = pd.DataFrame(rows)
#     csv_data = df.to_csv(index=False)

#     return Response(
#         content=csv_data,
#         media_type="text/csv",
#         headers={"Content-Disposition": "attachment; filename=predictions.csv"}
#     )

# # -------------------- Startup --------------------
# @app.on_event("startup")
# async def startup_event():
#     try:
#         await collection.database.client.admin.command("ping")
#         print("MongoDB connected successfully ✅")
#     except Exception as e:
#         print(f"MongoDB connection failed ❌: {e}")




from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
from pathlib import Path

from database import collection

# -------------------- APP --------------------
app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predict heart disease and store data"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- MODEL --------------------
MODEL_PATH = Path(__file__).parent / "models" / "heart_model.joblib"
model = load(MODEL_PATH)

# -------------------- REQUEST --------------------
class HeartDiseaseRequest(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# -------------------- HOME --------------------
@app.get("/")
def home():
    return {"message": "API Running ✅"}

# -------------------- PREDICT (FIXED) --------------------
@app.post("/predict")
async def predict(input_data: HeartDiseaseRequest):

    # FIX: proper dataframe (VERY IMPORTANT)
    features = pd.DataFrame([{
        "age": input_data.age,
        "sex": input_data.sex,
        "cp": input_data.cp,
        "trestbps": input_data.trestbps,
        "chol": input_data.chol,
        "fbs": input_data.fbs,
        "restecg": input_data.restecg,
        "thalach": input_data.thalach,
        "exang": input_data.exang,
        "oldpeak": input_data.oldpeak,
        "slope": input_data.slope,
        "ca": input_data.ca,
        "thal": input_data.thal
    }])

    # prediction
    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    # store in mongo
    document = {
        "inputData": input_data.dict(),
        "prediction": prediction,
        "probability": probability,
        "createdAt": datetime.utcnow()
    }

    await collection.insert_one(document)

    return {
        "prediction": prediction,
        "probability": probability,
        "createdAt": datetime.utcnow()
    }

# -------------------- EXPORT CSV --------------------
@app.get("/export-csv")
async def export_csv():

    docs = await collection.find({}).to_list(length=10000)

    rows = []
    for item in docs:
        row = item["inputData"]
        row["prediction"] = item["prediction"]
        row["probability"] = item["probability"]
        row["createdAt"] = item["createdAt"]
        rows.append(row)

    df = pd.DataFrame(rows)
    csv_data = df.to_csv(index=False)

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"}
    )

# -------------------- STARTUP --------------------
@app.on_event("startup")
async def startup():
    try:
        await collection.database.client.admin.command("ping")
        print("MongoDB connected ✅")
    except Exception as e:
        print("MongoDB error ❌:", e)