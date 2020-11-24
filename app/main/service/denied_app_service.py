from ...db import db_session
from ..model.models import APPACCESS_TB


def get_data():
    try:
        queries = db_session.query(APPACCESS_TB)
        entry = [
            dict(app_name=q.app_name, app_logo=q.app_logo.decode()) for q in queries
        ]
        if len(entry) == 0:
            return None
        return entry
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return False


def insert_data(app_name, app_logo):
    try:
        if find_data(app_name):
            return "already exist"
        table = APPACCESS_TB(app_name=app_name, app_logo=app_logo)
        db_session.add(table)
        db_session.commit()
        return True
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return False


def find_data(app_name):
    try:
        queries = db_session.query(APPACCESS_TB).filter(
            APPACCESS_TB.app_name == app_name
        )
        entry = [dict(app_name=q.app_name) for q in queries]
        if len(entry) == 0:
            return False
        return True
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return False


def delete_data(app_name):
    try:
        if not find_data(app_name):
            return "app not exist"
        db_session.query(APPACCESS_TB).filter(
            APPACCESS_TB.app_name == app_name
        ).delete()
        db_session.commit()
        return get_data()
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return False