from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import github

app = Flask(__name__)
api = Api(app)

g = github.Github("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")
repo = g.get_repo("herokutests/provideip")


class Ip(Resource):
    def get(self):
        with open("ip.txt", "r") as text:
            return text.read()


class Update(Resource):
    def put(self, newip):
        with open("ip.txt", "w") as text:
            text.write(newip)
        contents = repo.get_contents("/ip.txt")
        repo.update_file("ip.txt", "file_updated_automatically", newip, contents.sha)
        return "Updated", 201


api.add_resource(Ip, "/ip")
api.add_resource(Update, "/updateip/<string:newip>")

if __name__ == '__main__':
    app.run()
