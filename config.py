import configparser

def config_init():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def config_change_host(host, port):
    config_init()['Site']['host']=host
    config_init()['Site']['port']=port
    return "create"

def config_change_token(token):
    config_init()['Telegram']['token']=token
    return "create"

def config_change_chat(new_id):
    config_init()['Telegram']['id']=new_id
    return "create"

def config_change_sql_host(sql_host, sql_user, sql_pass, sql_tabl):
    config_init()['Mysql']['ip']=sql_host
    config_init()['Mysql']['user']=sql_user
    config_init()['Mysql']['pass']=sql_pass
    config_init()['Mysql']['tabl']=sql_tabl
    return "create"

def config_change_users(users):
    pass

site_host=config_init()['Site']['host']
site_port=config_init()['Site']['port']
token_key=config_init()['Telegram']['token']
chat_id=config_init()['Telegram']['id']
mysql_ip=config_init()['Mysql']['ip']
mysql_user=config_init()['Mysql']['user']
mysql_pass=config_init()['Mysql']['pass']
mysql_tabl=config_init()['Mysql']['tabl']
users=config_init()['Users']