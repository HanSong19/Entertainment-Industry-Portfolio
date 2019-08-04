import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl


df = pd.read_csv(r'pandas/cine.csv',engine='python',encoding='utf-8')
temp = df.groupby('movieNm').sum()
print(df.head(20))


temp1 = df[df['movieNm'] == '보헤미안 랩소디']
print(temp1)

mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
plt.bar(temp.index, temp1['salesAmt']) 
plt.title('영화명(movieNm)별 총 매출액 막대 그래프')
plt.xlabel('영화명')
plt.ylabel('총매출액')
plt.xticks(fontsize=6, rotation=90)
plt.show()