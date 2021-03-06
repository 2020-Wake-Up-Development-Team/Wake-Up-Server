from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.orm import relationship
from ...db import Base


class USERS_TB(Base):
    __tablename__ = "USERS_TB"

    id = Column(String(30), primary_key=True)
    pwd = Column(String(100), primary_key=True)
    school = Column(String(30), nullable=False)
    number = Column(Integer, nullable=True)
    name = Column(String(10), nullable=False)

    def __init__(self, id, pwd, school, number, name):
        self.id = id
        self.pwd = pwd
        self.school = school
        self.number = number
        self.name = name


class CONCENTRATION_TB(Base):
    __tablename__ = "CONCENTRATION_TB"

    idx = Column(Integer, autoincrement=True, primary_key=True)
    id = Column(String(30), ForeignKey("USERS_TB.id"), nullable=False)
    full_frame = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    sleep = Column(Integer, nullable=False)
    concentration = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)

    def __init__(self, id, phone, full_frame, sleep, concentration, created_at):
        self.id = id
        self.full_frame = full_frame
        self.phone = phone
        self.sleep = sleep
        self.concentration = concentration
        self.created_at = created_at


class APPACCESS_TB(Base):
    __tablename__ = "APPACCESS_TB"

    app_name = Column(String(100), primary_key=True)
    app_logo = Column(LONGBLOB, nullable=False)

    def __init__(self, app_name, app_logo):
        self.app_name = app_name
        self.app_logo = app_logo