from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
API_TOKEN = os.getenv('DB_ADDRESS')

# MongoDB connection setup
client = MongoClient()
db = client["esim_db"]
esims_collection = db["esims"]


class Esim(BaseModel):
    country: str
    provider: str
    price: float
    days: int
    gb: float


def serialize_esim(esim):
    return {
        "id": str(esim["_id"]),
        "country": esim["country"],
        "provider": esim["provider"],
        "price": esim["price"],
        "days": esim["days"],
        "gb": esim["gb"]
    }


@app.get("/esim/{country}")
async def get_esim_by_country(country: str, min_days: int, min_gb: float):
    # Construct the MongoDB query
    query = {
        "country": country,
        "days": {"$gte": min_days},
        "gb": {"$gte": min_gb}
    }

    esims = esims_collection.find(query)
    esims_list = [serialize_esim(esim) for esim in esims]

    if not esims_list:
        raise HTTPException(status_code=404, detail="No eSIMs found for this country with the given criteria")

    return esims_list


@app.post("/esim")
async def add_esim(esim: Esim):
    esim_id = esims_collection.insert_one(esim.dict()).inserted_id
    return {"id": str(esim_id)}


@app.put("/esim/{id}")
async def update_esim(id: str, esim: Esim):
    result = esims_collection.update_one({"_id": ObjectId(id)}, {"$set": esim.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="eSIM not found")
    return {"message": "eSIM updated"}


@app.delete("/esim/{id}")
async def delete_esim(id: str):
    result = esims_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="eSIM not found")
    return {"message": "eSIM deleted"}
