from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

#MongoDB connection
CLIENT=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.vzrlbsf.mongodb.net/?appName=sharayucluster")
DB=CLIENT["jobprojectdb"]
COLL=DB["profiles"]

#convert object id into string
def to_json(doc):
    doc["_id"]=str(doc["_id"])
    return doc

#Retrieve all documents
@app.route("/profiles",methods=['GET'])
def getprofiles():
    allprofiles=list(COLL.find())
    return jsonify([to_json(p) for p in allprofiles])

@app.route("/addprofile",methods=["POST"])
def addprofile():
    data=request.json
    result=COLL.insert_one(data)
    return jsonify({"message":"new profile added","id":str(result.inserted_id)})

@app.route("/change/<uid>",methods=["PUT"])
def changeprofile(uid):
    data=request.json
    result=COLL.update_one({"userid":uid},{"$set":data})
    if result.modified_count>0:
        return jsonify({"status":"profile updated"})
    
    return jsonify({"status":"UserID not found"})

if __name__=="__main__":
    app.run(debug=True)