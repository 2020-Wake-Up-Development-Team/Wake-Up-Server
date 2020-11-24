from flask import Blueprint, request, json, Response

api = Blueprint("video_analysis", __name__, url_prefix="/video_analysis")