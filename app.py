from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
messageCount = 0


class Message(Resource):
    def get(self, name):
        messageCount += 1
        return {"you got message": messageCount}


api.add_resource(Message, "/message")


@app.route("/")
def hello():
    return "hello world"
