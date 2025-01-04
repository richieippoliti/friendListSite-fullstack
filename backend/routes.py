from app import app, db
from flask import request, jsonify
from models import Friend

# get all friends
@app.route("/api/friends",methods=["GET"])

def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    # [ {...}, {...}]  
    # Stores the friends and all their individual metadata
    return jsonify(result)
