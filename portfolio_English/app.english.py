from flask import Flask,request,render_template,redirect,jsonify
import pymysql,re,time, os
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd


#다음의 웹사이트 드라이버와 연결한다
app = Flask(__name__)

@app.route('/moviemain')#주소임
def mainmovie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movieEnglish',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="select * from current_movie" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('Movie_English_bootstrap.html',movieList=result)

@app.route('/')
def formresult():
    driver = wd.Chrome(executable_path='portfolio/chromedriver')

    url = "https://www.rottentomatoes.com/browse/in-theaters/"
    driver.get(url)
    time.sleep(3)
    response = driver.page_source
    soup = BeautifulSoup(response,'lxml')
    results = soup.select('.mb-movie')
    for i in results:
        print(i)
    

    #if len(results) == 1:
    #    page = 1
    #else:
    #    page = int(results[-1].text)

    movie_title = [] #영화제목
    movie_img = []  #영화포스터
    movie_score = [] #영화평점
    movie_open = [] #영화오픈날짜
    
      

    #영화 타이틀 추출.
    movietitles = soup.find_all("h3",class_="movieTitle" )
    
    for movietitle in movietitles:
        movie_title.append(movietitle.text)
    
    #영화 이미지 추출
    movieImgs = soup.select("div a img.poster")
    
    for movieImg in movieImgs:
        movie_img.append(movieImg['src'])

    #영화개봉 날짜 추출
    movieOpens = soup.find_all('p',class_='release-date')

    #영화개봉날짜 정규표현씩 활용하여 추출.
    for movieOpen in movieOpens:
        movie_open.append(movieOpen.text)

    #영화 평점 추출
    moviescores = soup.find_all('span',class_='tMeterScore')
    #영화평점 정규표현씩 활용하여 추출.
    for moviescore in moviescores:
        movie_score.append(moviescore.text)
        
    
    driver.close()      
    #영화이미지주소 가공
    #for moviesoso in range(len(movie_img)):
    #    movie_img_Processing.append(movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 
    print(movie_title)
    print(movie_score) 
    print(movie_img) 
    print(movie_open) 
    
     
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movieEnglish',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    print(movie_img)
    try:
        with conn.cursor() as cursor:
            sql="delete from current_movie"
            cursor.execute(sql)
            conn.commit()    
            for insert in range(len(movie_title)):        
                sql='''
                insert into current_movie
                (current_movie_title, current_movie_open, current_movie_img, current_movie_score)
                values(%s,%s,%s,%s);
                '''
                cursor.execute(sql,(movie_title[insert], movie_open[insert], movie_img[insert], movie_score[insert], ))
                conn.commit()
    finally:
        conn.close()   
    return redirect('/moviemain')


if __name__ == "__main__":
    app.run(debug = True)


