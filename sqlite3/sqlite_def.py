import sqlite3

def create_table():
    conn= sqlite3.connect('sqlite3/my_books.db')
    cursor=conn.cursor()
    cursor.execute('''create table if not exists books(
                    title text,
                    pulished_date text,
                    publisher text,
                    pages integer,
                    recommend integer           
                    )''')
    conn.commit()
    conn.close()


def insert_books(items):
    conn = sqlite3.connect("sqlite3/my_books.db")
    cursor = conn.cursor()
    #cursor.execute("insert into books values('Java','2019-05-20','길벗', 500, 10)")
    sql = 'insert into books values(?,?,?,?,?)'
    #cursor.execute(sql,('Python','201001','한빛',584,20))
    
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()


def all_books():
    conn=sqlite3.connect("sqlite3/my_books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books")
    print('[1]전체 데이터 출력하기')
    books=cursor.fetchall()
    print(type(books))
    print(len(books))

    for book in books:
        for i in book:
            print(i,end=" ")
        print()
    conn.close()


