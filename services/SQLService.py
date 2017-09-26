import pymysql, os


def execute_sql(query):
    host = os.environ.get('SQL_HOST', default=None)
    user = os.environ.get('SQL_USERNAME', default=None)
    pw = os.environ.get('SQL_PASSWORD', default=None)
    db = os.environ.get('SQL_DATABASE', default=None)
    
    ret_val = None
    
    connection = pymysql.connect(host=host, user=user,password=pw, db=db,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    try:
        with connection.cursor() as cursor:
            # Execute query.
            cursor.execute(query)

            ret_val = cursor
    finally:
        # Close connection.
        connection.close()

    return ret_val