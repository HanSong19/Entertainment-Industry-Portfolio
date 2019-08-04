from flask import Flask,request,render_template,redirect,jsonify
import pymysql,re,time, os, sys,json, time, urllib.request,kobis_info,kobis_graph
from bs4 import BeautifulSoup
from selenium import webdriver as wd
import pandas as pd
import numpy as np
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image

tmrvl=[]
url="https://movie.naver.com/movie/running/current.nhn"
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
table=soup.select('dt.tit a')
for result3 in table:
        mtitle=str(result3.string)
        mcode=str(result3.attrs['href'])
        i = str(re.findall('\d+', mcode)[0])
        tmcode=tuple([i])
        tmtitle=tuple([mtitle])
        tmrvl.append(tmtitle+tmcode)
conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
c=conn.cursor()
#마리아 db에 넣을댸는 ??가아니고 %s로 써야됨
sql="INSERT IGNORE INTO test(title,codem) VALUES(%s,%s)"
c.executemany(sql, tmrvl)
conn.commit()
conn.close()

#다음의 웹사이트 드라이버와 연결한다

app = Flask(__name__)

@app.route('/moviemain')#주소임
def mainmovie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="select * from current_movie" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('Movie_bootstrap.html',movieList=result)

@app.route('/')
def formresult():
    driver = wd.Chrome(executable_path='portfolio/data/chromedriver')

    url = "https://movie.daum.net/premovie/released"
    driver.get(url)
    time.sleep(3)
    response = driver.page_source
    soup = BeautifulSoup(response,'lxml')
    results = soup.select('.num_page')

    if len(results) == 1:
        page = 1
    else:
        page = int(results[-1].text)

    movie_title = [] #영화제목
    movie_genre = [] #영화연령
    movie_img = []  #영화포스터
    movie_img_Processing =[] #영화포스터주소(가공후)
    #movie_score = [] #영화평점
    movie_open = [] #영화오픈날짜
    movie_story = [] #영화줄거리
    
    for movie_page in range(1,page+1):
        print(movie_page)
        url = "https://movie.daum.net/premovie/released?opt=reserve&page={}".format(movie_page)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')
        

        #영화 타이틀 추출.
        movietitles = soup.find_all('a',class_='name_movie #title')
        
        for movietitle in movietitles:
            movie_title.append(movietitle.text)
        
        #영화 연령 추출
        movieGenres = soup.find_all('em',class_='ico_movie')
        
        for movieGenre in movieGenres:
            if movieGenre.text == "독점":
                continue
            else:
                movie_genre.append(movieGenre.text)
        #영화 이미지 추출
        movieImgs = soup.select("div span img.img_g")
        
        for movieImg in movieImgs:
            movie_img.append(movieImg['src'])

        #영화개봉 날짜 추출
        movieOpens = soup.find_all('span',class_='info_state')

        #영화개봉날짜 정규표현씩 활용하여 추출.
        for movieOpen in movieOpens:
            movieOpen_cleand = re.sub('[a-zA-Z]' , '', movieOpen.text)
            movieOpen_cleand = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                            '', movieOpen.text)              
            movieOpen_cleand_final = movieOpen_cleand.split()
            movie_open.append(movieOpen_cleand_final[0])
            movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        
        for movieStory in movieStorys:
            movieStory_cleand = movieStory.text.strip()
            movieStroy_cleand_final = movieStory_cleand.replace("\n","")
            movie_story.append(movieStroy_cleand_final)  
    driver.close()      
        #영화이미지주소 가공
    for moviesoso in range(len(movie_img)):
        movie_img_Processing.append(movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 
        
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    print(movie_img_Processing)
    try:
        with conn.cursor() as cursor:
            sql="delete from current_movie"
            cursor.execute(sql)
            conn.commit()    
            for insert in range(len(movie_title)):        
                sql='''
                insert into current_movie
                (current_movie_title, current_movie_img, current_movie_genre, current_movie_open, current_movie_story)
                values(%s,%s,%s,%s,%s);
                '''
                cursor.execute(sql,(movie_title[insert],movie_img_Processing[insert],movie_genre[insert],movie_open[insert],movie_story[insert]))
                conn.commit()
    finally:
        conn.close()   
    return redirect('/moviemain')


#영화상세
@app.route('/movie_detail/<m_no>/<current_movie_title>')#주소임
def detail(m_no,current_movie_title):
    
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from current_movie c inner join test t on c.current_movie_title = t.title where current_movie_title = %s;'
            cursor.execute(sql,(current_movie_title))
            result=cursor.fetchone() #하나만 가져올떄

            sql='select * from current_movie where current_movie_title = %s;'
            cursor.execute(sql,(current_movie_title))
            result1=cursor.fetchone() #하나만 가져올떄

            sql='select * from board where m_no= %s;'
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()
    if result is not None:    
        tmrvl=[]
        movieName = result['codem']

        for page in range(1,200):
            url="https://movie.naver.com/movie/bi/mi/review.nhn?code="+str(movieName)+"&page="+str(page)
            response = urllib.request.urlopen(url)

            soup=BeautifulSoup(response,'html.parser')
            table=soup.select('ul.rvw_list_area li a')
            for result3 in table:
                mrv=str(result3.string)
                tmrv=tuple([mrv])
                tmrvl.append(tmrv)
                #tmrv1=str(tmrv)
                #f.write(tmrv1)
        df=pd.DataFrame(tmrvl)

        def preprocessing(text):
            # 개행문자 제거
            text = re.sub('\\\\n', ' ', text)
            return text
        
        tokenizer = RegexTokenizer()
        stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가',
                        '그럼', '이런', '저런', '합니다',
                        '많은', '많이', '정말', '너무','[',']','것으로','했습니다','했다'] 

        sentences = df[0].apply(preprocessing)

        # soynlp로 명사 추출하기
        noun_extractor = LRNounExtractor(verbose=True)
        noun_extractor.train(sentences)
        nouns = noun_extractor.extract()
    
        # 이미지 파일위에 출력하기
        img = Image.open('portfolio/static/img/cloud.png')
        img_array=np.array(img)

        wordcloud = WordCloud( font_path = '/Library/Fonts/NanumBarunGothic.ttf', 
                            stopwords = stopwords_kr,
                            background_color = 'white', 
                            mask=img_array,
                            width = 800, height = 600).generate(' '.join(nouns))
        plt.figure(figsize = (15 , 10))
        plt.imshow(wordcloud)
        plt.axis("off")
        #plt.show()  
        url1="portfolio/static/img/wordcloud/" + current_movie_title + ".png"
        wordcloud.to_file(url1)
    '''
    kobis_info.info()
    
    #graph그리는것
    df = pd.read_csv(r'portfolio/data/cine.csv',engine='python',encoding='utf-8')
    temp = df[df['movieNm'] == current_movie_title]
    #print(temp[['salesAmt','targetDt','movieNm']])
    #print(temp.dtypes)
    mpl.rc('font', family='/Library/Fonts/NanumBarunGothic.ttf') #한글 폰트 설정
    plt.bar(temp['targetDt'].astype(str),temp['salesAmt']) 
    plt.title('일별 매출액 막대 그래프')
    plt.xlabel('날짜')
    plt.ylabel('총매출액')
    plt.xticks(fontsize=13, rotation=90)
    url1="portfolio/static/img/chart/" + current_movie_title + ".png"
    plt.savefig(url1) 
    '''
    return render_template('movie_detail.html', wordInfo=result, board=board, movieInfo=result1)



if __name__ == "__main__":
    app.run(debug = True)


'''
print(movie_title)
print(movie_genre) 
print(movie_img_Processing) 
print(movie_open) 
print(movie_story)
'''