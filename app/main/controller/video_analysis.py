from flask import Blueprint, request, jsonify, Response
import wget
import urllib.request

api = Blueprint("video_analysis", __name__, url_prefix="/video_analysis")


@api.route("/<id>", methods=["POST"])
def get_videofile(id):
    data = request.get_json()
    try:
        if not urllib.request.urlopen(data["url"]).status == 200:
            return jsonify({"message": "invalid url", "status": 400})

        video_file = wget.download(data["url"])
        # video_file 처리
        return jsonify({"status": 200})

    except Exception as err:
        return jsonify({"status": 400, "message": "Fail"})
