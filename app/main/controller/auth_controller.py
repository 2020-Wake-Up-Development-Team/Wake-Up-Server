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
        data["class"].replace("-", ""),
        data["name"],
    )  # 회원가입 함수

    if state == "success":
        return jsonify({"code": 200, "message": "signup success"})  # 회원가입 성공

    elif state == "defind id":
        return jsonify({"code": 400, "message": "signup defind id"})  # 이미 있는 아이디

    elif state == "fail":
        return jsonify({"code": 400, "message": "signup fail"})  # 회원가입 실패


@api.route("/login", methods=["POST"])  # 로그인
def login():
    data = request.get_json()  # 데이터 받기

    state = auth_service.user_login(data["id"], data["pwd"])  # 로그인 함수

    if state == "success":
        return jsonify({"code": 200, "message": "login success"})  # 로그인 성공

    elif state == "fail":
        return jsonify({"code": 400, "message": "login fail"})  # 로그인 실패

    elif state == "undefind id":
        return jsonify({"code": 400, "message": "login undefined id"})  # 없는 아이디
