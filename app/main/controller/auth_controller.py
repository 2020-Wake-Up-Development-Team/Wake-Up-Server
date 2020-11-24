from flask import Blueprint, request, json, Response

api = Blueprint("auth", __name__, url_prefix="/auth")