import sqlite3

def create_table():
    conn= sqlite3.connect('my_books.db')
    cursor=conn.cursor()
    cursor.execute('''create table if not exists books(
                    title text,
                    pulished_date text,
                    publisher text,
                    page integer,
                    recommend integer           
                    )''')
    conn.commit()
    conn.close()

def insert_books():
    conn = sqlite3.connect("my_books.db")
    cursor = conn.cursor()
    cursor.execute("insert into books values('Java','2019-05-20'.'길 벗', 500, 10)")
    sql = 'insert into books values(?,?,?,?,?)'
    cursor.execute(sql,('Python','201001','한빛',584,20))
    items = [
        ('빅테이터','2014-07-02','삼성',296.11),
        ('안드로이드','2010-02-02','삼성',526.20),
        ('spring','2013-12-02','삼성',248.15)
    ]
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()


create_table()

