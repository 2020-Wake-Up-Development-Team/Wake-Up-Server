from flask import Blueprint, request, json, Response, jsonify
from ..service import denied_app_service

api = Blueprint("deniedapp", __name__, url_prefix="/deniedapp")


@api.route("", methods=["GET"])
def get_denied_app():
    result = denied_app_service.get_data()
    if result == None:
        return "Table is Empty"
    return jsonify(result)


@api.route("", methods=["POST"])
def add_denied_app():
    data = request.get_json()
    result = denied_app_service.insert_data(data["app_name"])
    if result == "already exist":
        return jsonify({"message": "{} is already existed".format(data["app_name"])})
    elif not result:
        return jsonify({"status": 404})
    return jsonify({"status": 200})


@api.route("/<app_name>", methods=["DELETE"])
def delete_denied_app(app_name):
    result = denied_app_service.delete_data(app_name)
    if result == "app not exist":
        return jsonify("{} is not existed".format(app_name), {"status": 400})
    elif not result:
        return jsonify({"status": 400})
    return jsonify({"status": 200})
