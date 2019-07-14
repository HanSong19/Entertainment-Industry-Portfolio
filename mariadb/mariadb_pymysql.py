import pymysql

def conn_db():
    conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password='qwer1234',
                        db='test',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
    return conn


def create_table():
    conn=conn_db() #위에있는 함수를 받는다
    cursor=conn.cursor()
    cursor.execute('''
                    create table if not exists books(
                    title varchar(50),
                    published_data date,
                    publisher varchar(50),
                    pages int,
                    recommended int)
                    ''')
    conn.commit()
    conn.close()

def insert_books(items):
    conn=conn_db()
    cursor = conn.cursor()
    #cursor.execute("insert into books values('Java','2019-05-20','길벗, 500,10)")
    #이 방법이 있긴 한데 거의 쓰지 않는다
    sql = "insert into books values(%s,%s,%s,%s,%s)"
    cursor.execute(sql,('Python','201001','한빛', 584,20))
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()
