import mariadb_pymysql as db

db.conn_db()

items=[
        ('빅데이터','2014-07-02','삼성',296,11),
        ('안드로이드','2010-02-02','삼성',526,20),
        ('spring','2013-12-02','삼성',248,15)
        ]

db.create_table()
db.insert_books(items)