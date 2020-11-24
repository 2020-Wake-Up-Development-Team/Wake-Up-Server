from flask import Blueprint, request, json, Response
from ..service import access_app_service

api = Blueprint("deniedapp", __name__, url_prefix="/deniedapp")


@api.route("/", methods=["GET"])
def get_denied_app():
    result = access_app_service.get_data()

    if len(result) == 0:
        return Response(status=404)
    return Response({"data": json.dumps(result)}, status=200)


@api.route("/", methods=["POST"])
def add_denied_app():
    data = request.get_json()
    result = access_app_service.insert_data(data["app_name"])

    if not result:
        return Response(status=400)
    return Response(status=200)


@api.route("/<str:app_name>", methods=["DELETE"])
def delete_denied_app(app_name):
    result = access_app_service.delete_data(app_name)

    if not result:
        return Response(status=400)
    return Response({"data": json.dumps(result)}, status=200)
