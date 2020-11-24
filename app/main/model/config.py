db = {
    "user": "root",  # 1)
    "password": "woungsub",  # 2)
    "host": "127.0.0.1",  # 3)
    "port": 3306,  # 4)
    "database": "wakeupdb",  # 5)
}

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
    db["user"], db["password"], db["host"], db["port"], db["database"]
)
