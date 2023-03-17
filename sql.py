from sqlalchemy.orm import sessionmaker
from base import Ticket, engine, Ticket_info, Ticket_log

def init_session():
    make=sessionmaker(bind=engine)
    session=make()
    return session

def init_ticket(user_id):
    pass