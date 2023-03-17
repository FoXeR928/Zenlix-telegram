import fastapi
from bot import send_ticket_bot
import config

app = fastapi.FastAPI()

@app.get("/get_ticket", status_code=fastapi.status.HTTP_201_CREATED)
def get_ticket(user: str, subj: str, msg: str):
    send_ticket_bot(user,subj,msg)
    return send_ticket_bot

@app.get("/config_change_host", status_code=fastapi.status.HTTP_201_CREATED)
def config_change_host(host: str, port: str):
    config.config_change_host(host, port)

@app.get("/config_change_token", status_code=fastapi.status.HTTP_201_CREATED)
def config_change_token(token: str):
    config.config_change_token(token)

@app.get("/config_change_chat", status_code=fastapi.status.HTTP_201_CREATED)
def config_change_chat(new_id: str):
    config.config_change_chat(new_id)

@app.get("/config_change_sql", status_code=fastapi.status.HTTP_201_CREATED)
def config_change_sql_host(sql_host: str, sql_user: str, sql_pass: str, sql_tabl: str):
    config.config_change_sql_host(sql_host, sql_user, sql_pass, sql_tabl)

@app.get("/config_change_users", status_code=fastapi.status.HTTP_201_CREATED)
def config_change_users(users: str):
    config.config_change_users(users)