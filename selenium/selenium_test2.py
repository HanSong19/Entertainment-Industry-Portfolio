from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(5)
loca = driver.find_element_by_class_name('loca_search') #element 는 tag가 기본 단위인데 그걸 class name으로 찾는다는 이야기
loca.click()
time.sleep(5)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li') #li 에 리스트로 쭉 도시 이름들이 나옴 (시도가 많아서 elements)
li[5].click() #부산이 다섯번째
time.sleep(5)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li = gugun.find_elements_by_tag_name('li')
li[16].click()
time.sleep(5)

source = driver.page_source
bs=BeautifulSoup(source,'lxml')
entire = bs.find('ul',class_='quickSearchResultBoxSidoGugun')
li_list=entire.find_all('li')

for li in li_list:
    print(li.find('p').text)



