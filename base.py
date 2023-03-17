import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from config import mysql_user,mysql_pass,mysql_ip,mysql_tabl


engine = sqlalchemy.create_engine(f'mariadb://{mysql_user}:{mysql_pass}@{mysql_ip}:3306/{mysql_tabl}')

base = declarative_base()
class Ticket(base):
    __tablename__ = 'tickets'

    id= Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_init_id=Column(Integer)
    user_to_id=Column(VARCHAR)
    date_create=Column(DateTime)
    subj=Column(VARCHAR)
    msg=Column(LONGTEXT)
    client_id=Column(Integer)
    unit_id=Column(Integer)
    status=Column(Integer)
    hash_name=Column(VARCHAR)
    comment=Column(VARCHAR)
    arch=Column(Integer)
    is_read=Column(Integer)
    lock_by=Column(Integer)
    last_edit=Column(DateTime)
    ok_by=Column(Integer)
    prio=Column(Integer)
    ok_date=Column(DateTime)
    last_update=Column(DateTime)
    deadline_time=Column(DateTime)
    sla_plan_id=Column(Integer)

class Ticket_info(base):
    __tablename__ = 'ticket_info'

    id= Column(Integer, unique=True, autoincrement=True, primary_key=True)
    ticket_id=Column(Integer, ForeignKey(Ticket.id))
    ticket_source=Column(VARCHAR)
    ip=Column(VARCHAR)
    os=Column(VARCHAR)
    browser=Column(VARCHAR)

class Ticket_log(base):
    __tablename__ = 'ticket_log'

    id= Column(Integer, unique=True, autoincrement=True, primary_key=True)
    date_op=Column(DateTime)
    msg=Column(VARCHAR)
    init_user_id=Column(Integer)
    to_user_id=Column(VARCHAR)
    ticket_id=Column(Integer)
    to_unit_id=Column(Integer)