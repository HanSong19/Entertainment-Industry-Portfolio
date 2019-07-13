import sqlite3

print(sqlite3.version)

conn = sqlite3.connect('sqlite3/example.db') #this connects this file to example.db. 
#if example.db does not exsit, it automatically make the file. 
#sqlite, maria db are 관계형 bd, some (mongo something) is not automatic
c= conn.cursor()
#cursor를 통해서 실행하기 때문에 꼭 cursor가 필요하다 위에는 그냥 연결 하는것
c.execute('''
            CREATE TABLE if not exists stocks(
                date text, 
                trans text,
                symbol text,
                qty real,
                price real
                )
        ''')

c.execute('''
            insert into stocks(date, trans, symbol, qty, price) 
                        values('2019-0109','BUY','AAA',100, 35.14)
            ''')

conn.commit()
conn.close()
