# pip install flask_restful

from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class BasicREST(Resource):
    def get(self):
        profile={
            "name":"praffull",
            "codename":"ethan hunt",
            "city":"london",
            "language":"english",
            "qualification":"MBA(MC)",
            "mobile":"7391966656",
            "email":"praffull@outlook.com",
            "keyskills":["java","spring boot","jpa","ai"]
        }
        return profile

api.add_resource(BasicREST,"/profile")
app.run(debug=True)

# http://127.0.0.1:5000/profile

