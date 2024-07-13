from flask import Flask, request, jsonify
import logging

from Utils import response_utils as rutils


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return 'Endpoint successful!'

@app.route("/get-name", methods=["POST"])
def get_name():
    if request.method == "POST":
        data = request.json
        params = data["body"]
        request_name = params["name"]

        if request_name:
            message = "Hi, I am Lachin"
            return jsonify(rutils.success_response({"message": message}))
    else:
        message = "Invalid HTTP method"
        error_info = {"errorCode": None, "message": message, "suggestions": None}
        return jsonify(rutils.failuer_response([error_info]))


if __name__ == "__main__":
    app.run(debug=True)
