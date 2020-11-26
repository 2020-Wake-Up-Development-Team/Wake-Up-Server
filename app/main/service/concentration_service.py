# CONCENTRATION 테이블에 접근하는 코드
from datetime import date
from ..model.models import CONCENTRATION_TB, USERS_TB
from ...db import db_session
from sqlalchemy.sql import func
from sqlalchemy import text


def get_detail_info(user_id, opt):
    if opt == "categorical":
        pass
    elif opt == "linear":
        pass


def get_base_info():
    # 전체
    pass


def get_ten_records(page_num):
    sql_query = """
        SELECT
            sum(CONCENTRATION_TB.concentration) / COUNT(USERS_TB.id),
            USERS_TB.id,
            USERS_TB.number,
            USERS_TB.name,
            CONCENTRATION_TB.full_frame
        FROM
            USERS_TB,
            CONCENTRATION_TB
        GROUP BY
            USERS_TB.id
        ORDER BY
            sum(CONCENTRATION_TB.concentration) DESC
    """
    queries = db_session.execute(sql_query)
    # queries = queries[page_num * 10 : page_num * 10 + 11]  # page_num
    return queries
