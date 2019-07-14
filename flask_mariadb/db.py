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
                    create table if not exists users(
                    userid varchar(50) NOT NULL, 
                    email varchar(255) NOT NULL, 
                    useraddress varchar(255),
                    password varchar(255) NOT NULL,
                    PRIMARY KEY(userid))
                    ''')
    conn.commit()
    conn.close()

def insert_info(user):
    conn=conn_db()
    cursor = conn.cursor()
    #cursor.execute("insert into books values('Song','han@gmail.com','w apartment', 123456)")
    #이 방법이 있긴 한데 거의 쓰지 않는다
    sql = "insert into users(userid, email, useraddress,password) values(%s,%s,%s,%s)"
    cursor.execute(sql,user)
    conn.commit()
    conn.close()

def all_users():
    conn=conn_db()
    cursor = conn.cursor()
    cursor.execute("select * from users")
    users = cursor.fetchall()
    print(len(users))
    print(users)
    conn.close()
    return users

def one_user(userid):
    conn=conn_db()
    cursor = conn.cursor()
    sql = 'select * from users where userid = %s'
    cursor.execute(sql,userid)
    user= cursor.fetchone()
    conn.commit()
    conn.close()
    return user

def delete_user(userid):
    conn=conn_db()
    cursor = conn.cursor()
    sql = 'delete from users where userid = %s'
    cursor.execute(sql,userid)
    conn.commit()
    conn.close()

def update_user(user):
    conn=conn_db()
    cursor = conn.cursor()
    print(user)
    sql = ''' update users
        set email = %s,
            useraddress=%s,
            password=%s
        where userid = %s
        '''  
    
    cursor.execute(sql,(user['email'],user['useraddress'],user['password'],user['userid']))
    conn.commit()
    conn.close()