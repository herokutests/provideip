from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)
ip = "192.168.1.11"


class Ipget(Resource):
    def get(self, password):
        if password == "kellazip":
            return ip
        else:
            return "incorrect password"


class Ipupdate(Resource):
    def get(self)
        return {"message": "welcome"}
    def put(self, newip):
        global ip
        ip = newip
        return "Updated", 201


api.add_resource(Ipupdate, "/")
api.add_resource(Ipget, "/getip/<string:password>")
api.add_resource(Ipupdate, "/updateip/<string:newip>")

if __name__ == '__main__':
    app.run()
