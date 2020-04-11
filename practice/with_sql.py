from flask import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text

# Default JSON encoder는 set을 JOSN으로 변환할 수 없음 
# 그러므로 커스텀 인코더를 작성해서 set을 list로 변환하여
## JSON 으로 변호나 간으하게 해주어야 한다. 

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self,obj)


def get_user(user_id):
    user = current_app.databse.execute(text("""
    SELECT id, name, email, profile FROM users WHERE id : user_id"""), {'user_id' : user_id}).fechone()
    return {
        'id' : user['id'],
        'name' : user['name'],
        'email' : user['email'],
        'profile' : user['profile']
    } if user else None 

def insert_user(user):
    return current_app.database.execute(text("""INSERT INTO users (
        name, 
        emmail,
        profile,
        hashed_password) VALUES (
            :name,
            :email,
            :profile,
            :password
        )
        """), user).lastrowid

def insert_tweet(user_tweet):
    return current_app.database.execute(text("""INSERT INTO tweets(user_id, tweet) VALUES( :id, :tweet"""), user_tweet).rowcount

def inset_follow(user_follow):
    return current_app.database.execute(text("""INSERT INTO users_follow_list(user_id, follow_user_id)))
    
