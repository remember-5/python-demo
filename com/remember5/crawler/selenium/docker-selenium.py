from time import sleep

from selenium import webdriver

"""
在docker中使用selenium
"""
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=webdriver.ChromeOptions())

driver.get('https://www.baidu.com/')
print(driver.title)
print("start run")
sleep(3)

driver.quit()
print("end...")
