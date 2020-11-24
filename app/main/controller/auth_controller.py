import re
from flask import Flask, request, Blueprint, jsonify
from ..service import auth_service


api = Blueprint("auth", __name__, url_prefix="/auth")


@api.route("/signup", methods=["POST"])  # 회원가입
def signup():
    data = request.get_json()  # 데이터 받기
    if not "-" in data["class"]:
        return jsonify({"message": "class format isn't right"})

    state = auth_service.user_signup(
        data["id"],
        data["pwd"],
        data["school"],
        data["class"].replace("-", ""),  # "-" => "" 변경
        data["name"],
    )  # 회원가입 함수
    return state


@api.route("/login", methods=["POST"])  # 로그인
def login():
    data = request.get_json()  # 데이터 받기

    state = auth_service.user_login(data["id"], data["pwd"])  # 로그인 함수
    return state