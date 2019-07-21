import pymysql


def conn_db():
    conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password='qwer1234',
                        db='test',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
    return conn
    
def store(title,content):
    title=title.replace("'","''")
    title=title.replace('"','\"')
    content = content.replace("'","''")
    content=content.replace('"','\"')

    sql = 'insert into pages (title, content) values(%s,%s)'
    cursor.execute(sql,(title,content))
    connection.commit()



def create_table():
    conn=conn_db() #위에있는 함수를 받는다
    cursor=conn.cursor()
    #movie 테이블 생성(글번호, 평점,영화제목,140자평,글쓴이,날짜)
    #no integer, grade integer, title text, content text, writer text, date text
    cursor.execute('''
                    create table if not exists movie(
                    no int NOT NULL, 
                    grade int, 
                    title varchar(255),
                    content varchar(300),
                    writer varchar(30),
                    date varchar(20))
                    ''')
    conn.commit()
    conn.close()



def all_users():
    conn=conn_db()
    cursor = conn.cursor()
    cursor.execute("select * from movie")
    items = cursor.fetchall()
    print(len(items))
    conn.close()
    return items


#입력하는것
def insert_movie(items):
    conn=conn_db()
    cursor = conn.cursor()
    #cursor.execute("insert into books values('Song','han@gmail.com','w apartment', 123456)")
    #이 방법이 있긴 한데 거의 쓰지 않는다
    sql = "insert into movie (no, grade, title,content,writer,date) values(%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()


