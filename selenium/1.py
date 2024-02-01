from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import parsel
driver = webdriver.Edge()

driver.get('https://www.gequbao.com/')
#  driver.save_screenshot('歌曲.png') 对屏幕进行截屏

# htmldata = driver.page_source 获取页面源代码
# selector = parsel.Selector(htmldata)
# print(selector)
# print(driver.get_cookies())
sleep(5)
driver.quit()