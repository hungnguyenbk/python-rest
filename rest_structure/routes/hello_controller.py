from flask import Blueprint, jsonify
from services.hello_service import get_hello_message

hello_blueprint = Blueprint("hello", __name__)

@hello_blueprint.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": get_hello_message()})
