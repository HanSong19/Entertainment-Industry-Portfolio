import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

def graph_m(title):
    df = pd.read_csv(r'portfolio/data/cine.csv',engine='python',encoding='utf-8')
    print(title)
    print(df)
    temp = df[df['movieNm'] == title]
    #print(temp[['salesAmt','targetDt','movieNm']])
    #print(temp.dtypes)
    mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
    plt.bar(temp['targetDt'].astype(str),temp['salesAmt']) 
    plt.title('일별 매출액 막대 그래프')
    plt.xlabel('날짜')
    plt.ylabel('총매출액')
    plt.xticks(fontsize=10, rotation=90)
    url1="portfolio/static/img/chart/" + title + ".png"
    plt.savefig(url1)


if __name__ == "__main__":
    graph_m("알라딘")
    
