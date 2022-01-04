from flask_pymongo import pymongo
import flask
import certifi
import json
from bson import json_util
from flask import request
from bson.objectid import ObjectId
from flask_cors import CORS
from datetime import datetime

app = flask.Flask(__name__)
CORS(app)

# MongoDB Atlas Connection (UserName: flask, pwd: flask, Database: flask, Collection: memory)
CONNECTION_STRING = "mongodb+srv://flask:flask@cluster0.ijnpm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
db = client.get_database('flask')

# CRUD - GetAllPosts
@app.route("/", methods=['GET'])
def getPosts():
    posts = db.memory.find()
    res = json.loads(json_util.dumps(posts))
    return flask.jsonify(res)

# CRUD - CreatePost
@app.route("/", methods=['POST'])
def createPost():
    data = request.json
    res = db.memory.insert_one({
        'title': data['title'],
        'message': data['message'],
        'creator': data['creator'],
        'tags': data['tags'],
        'selectedFile': data['selectedFile'],
        'likeCount': 0,
        'createdAt': datetime.now()})
    # get the data after create data
    post = db.memory.find_one({'_id': res.inserted_id})
    res = json.loads(json_util.dumps(post))
    return flask.jsonify(res)


# CRUD - GetPostById
@app.route("/<obj_id>", methods=['GET'])
def getPost(obj_id):
    post = db.memory.find_one({'_id': ObjectId(obj_id)})
    res = json.loads(json_util.dumps(post))
    return flask.jsonify(res)

# CRUD - DeletePost
@app.route('/<obj_id>', methods=['DELETE'])
def deletePost(obj_id):
    res = db.memory.delete_one({'_id': ObjectId(obj_id)})
    output = {'Status': 'Successfully Deleted',
              'Deleted_Count': str(res.deleted_count)}
    return output

# CRUD - UpdatePost
@app.route('/<obj_id>', methods=['PATCH'])
def updatePost(obj_id):
    data = request.json
    db.memory.update_one({'_id': ObjectId(obj_id)}, {"$set": {
        'title': data['title'],
        'message': data['message'],
        'creator': data['creator'],
        'tags': data['tags'],
        'selectedFile': data['selectedFile']}})
    # get the data after update data
    post = db.memory.find_one({'_id': ObjectId(obj_id)})
    res = json.loads(json_util.dumps(post))
    return flask.jsonify(res)

#  CRUD - LikePost
@app.route('/<obj_id>/likePost', methods=['PATCH'])
def likePost(obj_id):
    oldPost = db.memory.find_one({'_id': ObjectId(obj_id)})
    db.memory.update_one({'_id': ObjectId(obj_id)}, {"$set": {'likeCount': oldPost['likeCount'] + 1}})
    # get the data after update data
    post = db.memory.find_one({'_id': ObjectId(obj_id)})
    res = json.loads(json_util.dumps(post))
    return flask.jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
