from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://shikhar-admin:admin-12@my-cluster.yv07f.mongodb.net/?retryWrites=true&w=majority&appName=my-cluster")
client = MongoClient(MONGO_URI)
db = client["vercelApp"]
collection = db["data"]

# API route
@app.route("/api/data", methods=["GET"])
def get_data():
    data = collection.find({}, {"_id": 0, "name": 1})
    return jsonify(list(data))

if __name__ == "__main__":
    app.run(debug=True)

