import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    return text

def displayWordCloud(data = None, backgroundcolor = 'white', width=800, height=600 ):
    wordcloud = WordCloud(
                        font_path = '/Library/Fonts/NanumBarunGothic.ttf', 
                        stopwords = stopwords_kr,
                        background_color = backgroundcolor, 
                        width = width, height = height).generate(data)
    plt.figure(figsize = (15 , 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show() 

df = pd.read_csv('pandas/foo1.csv', engine='python', encoding='utf-8')
tokenizer = RegexTokenizer()
stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가',
                '그럼', '이런', '저런', '합니다',
                '많은', '많이', '정말', '너무','[',']','것으로','했습니다','했다'] 

sentences = df['본문'].apply(preprocessing)
displayWordCloud(' '.join(sentences))

# soynlp로 명사 추출하기
noun_extractor = LRNounExtractor(verbose=True)
noun_extractor.train(sentences)
nouns = noun_extractor.extract()
displayWordCloud(' '.join(nouns))

# 이미지 파일위에 출력하기
img = Image.open('pandas/cloud.png')
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
wordcloud.to_file("pandas/simple.png")
