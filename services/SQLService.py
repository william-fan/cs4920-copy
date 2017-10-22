import pymysql, os

sql_connection = None

def execute_sql(query):
    one_time = False
    ret_val = None
    
    global sql_connection
    
    if sql_connection is None:
        connect()
        one_time = True
    with sql_connection.cursor() as cursor:
        # Execute query.
        cursor.execute(query)

        ret_val = cursor
    
    if one_time:
        disconnect()
    
    return ret_val

def connect():
    host = os.environ.get('SQL_HOST', default=None)
    user = os.environ.get('SQL_USERNAME', default=None)
    pw = os.environ.get('SQL_PASSWORD', default=None)
    db = os.environ.get('SQL_DATABASE', default=None)
    global sql_connection
    sql_connection = pymysql.connect(host=host, user=user,password=pw, db=db,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor, autocommit=True)

def disconnect():
    global sql_connection
    sql_connection.close()
    sql_connection = None