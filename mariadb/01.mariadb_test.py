import pymysql

#python으로 만들어진 library라서 
conn=pymysql.connect(host = 'localhost',
                    user = 'root',
                    password="qwer1234",
                    db = 'test',
                    charset = 'utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

c=conn.cursor()


c.execute(''' CREATE TABLE if not exists stocks
            (date text, trans text, symbol text, qty real, price real)
         ''')

c.execute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()





