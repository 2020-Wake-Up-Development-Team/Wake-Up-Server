# CONCENTRATION 테이블에 접근하는 CONCENTRATION_SERVICE 코드를 사용하는 api입니다.
from flask import Blueprint, request, json, Response

api = Blueprint("concentration", __name__, url_prefix="/concentration")