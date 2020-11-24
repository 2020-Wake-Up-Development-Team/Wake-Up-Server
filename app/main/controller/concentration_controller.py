# CONCENTRATION 테이블에 접근하는 CONCENTRATION_SERVICE 코드를 사용하는 api입니다.
from flask import Blueprint, request, json, Response
from ..service import concentration_service

api = Blueprint("concentration", __name__, url_prefix="/concentration")


@api.route("/retrieve/<int:page_num>", methods=["GET"])
def retrieve_data(page_num):
    # page_num * 10개씩 concentration 내림차순하여 전송
    result = concentration_service.get_ten_records(page_num)
    return result


@api.route("/detail/linear-chart/<user_id>", methods=["GET"])
def detailed_concentration_data(user_id):
    # 최근 7일간의 데이터 전송
    result = concentration_service.get_detail_info(user_id, "linear")
    pass


@api.route("/detail/circle-chart/<user_id>", methods=["GET"])
def detailed_categorical_data(user_id):
    result = concentration_service.get_detail_info(user_id, "categorical")