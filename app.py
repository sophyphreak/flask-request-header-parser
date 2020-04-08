from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class RequestHeaderParser(Resource):
    def get(self):
        return {
            "ipaddress": request.remote_addr,
            "language": str(request.accept_languages),
            "software": str(request.user_agent),
        }


api.add_resource(RequestHeaderParser, "/api/whoami/")

if __name__ == "__main__":
    app.run(debug=True)
