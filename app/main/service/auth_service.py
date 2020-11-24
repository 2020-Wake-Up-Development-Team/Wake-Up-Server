# USERS 테이블에 접근하는 파일
from ..model.models import USERS_TB
from ...db import db_session


def user_signup(user_id, pwd, school, number, name):
    try:
        if find_id(user_id):  # 이미 있는 아이디
            print("defind")
            return "defind id"

        else:  # 회원가입 진행
            table = USERS_TB(user_id=user_id, pwd=pwd, school=school, name=name)
            db_session.add(table)
            db_session.commit()
            return "success"  # 회원가입 성공

    except Exception as err:
        print("Error Log: [{}]".format(err))
        return "fail"


def user_login(user_id, pwd):
    try:
        if not find_id(user_id):  # 없는 아이디로 로그인
            return "undefind id"
        else:
            queries = (
                db_session.query(USERS_TB)
                .filter(USERS_TB.user_id == user_id)
                .filter(USERS_TB.pwd == pwd)
            )
            entry = [dict(user_id=q.user_id, pwd=q.pwd) for q in queries]
            if len(entry) == 0:  # 로그인 실패
                return "fail"
            else:
                return "success"  # 로그인 성공

    except Exception as err:
        print("Error Log: [{}]".format(err))
        return "fail"


def find_id(user_id):  # 아이디가 있으면 return 1, 없으면 return 0
    try:
        queries = db_session.query(USERS_TB).filter(USERS_TB.user_id == user_id)
        entry = [dict(user_id=q.user_id, pwd=q.pwd) for q in queries]
        if len(entry) == 0:
            return False  # 아이디 X
        else:
            return True  # 아이디 O

    except Exception as err:
        print("Error Log: [{}]".format(err))
        return 0