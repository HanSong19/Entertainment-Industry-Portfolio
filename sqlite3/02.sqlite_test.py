import sqlite3

conn = sqlite3.connect("sqlite3/example.db")
c= conn.cursor()
#방법 1
symbol = "AAA"
c.execute("SELECT * from stocks WHERE symbol = '%s'"%symbol)
# *은 전부다 라는 뜻인데, 원래는 필드 명을 다 써주는게 에러가 덜나긴 한다
# WHERE은 조건을 나열할 때 쓴다
items = c. fetchall() #fetch는 한 행(가로열) 씩 가져와서 쓸수 있게 한다

for item in items:
    print(item)

#방법 2

t = ('RHAT',)
sql = 'SELECT *FROM stocks WHERE symbol = ?'
c.execute(sql, t) 
print(c.fetchall())

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
            ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
            ('2006-04-06', 'SELL', 'IBM', 500, 53.00),]

c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)', purchases)
conn.commit() #데이터를 더하거나 변화가 있거나 하는것은 무조건 commit해야지 들어간다

c.execute('select * from stocks ORDER BY price')
rows = c.fetchall()

for row in rows:
    print(row)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
c.close()

