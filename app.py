from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    messageCount = 0

    def get(self):
        self.messageCount += 1
        return {"you got message": self.messageCount}


api.add_resource(Message, "/message")


@app.route("/")
def hello():
    return "hello world"
