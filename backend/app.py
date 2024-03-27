from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client.user_db
users = db.users

@app.route('/submit', methods=['POST'])
def submit():
    user_info = request.json
    users.insert_one(user_info)
    return jsonify({"message": "User info stored."}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
