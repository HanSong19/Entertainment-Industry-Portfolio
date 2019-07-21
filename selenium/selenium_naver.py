from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(5)

id = 'shbshb12'   
pw = 'gj91slqpdj'

'''
driver.find_element_by_name('id').send_keys(id)
driver.find_element_by_name('pw').send_keys(pw)
bt=driver.find_element_by_class_name('btn_global')
bt.click()
''' #이 방법으로도 되는데 네이버에서 이 방법을 막아놈

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

#xpath 값찾기-> 해당소스 오른쪽 클릭 xpath복사