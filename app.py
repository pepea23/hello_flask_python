from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
messageCount = 0


class Message(Resource):
    def get(self, name):
        return {"you got message":messageCount += 1}


api.add_resource(Message, "/message")

app.run(port=5000)