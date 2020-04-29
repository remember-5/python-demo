# encoding: utf-8
import time

from selenium import webdriver

# 引入 Keys 模块

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:/soft/chromedriver/chromedriver')
    driver.get("https://www.jianshu.com/u/7ec548858a10")
    for i in range(0, 10):
        driver.execute_script("window.scrollBy(0,100000)")
        time.sleep(1)

    bf = driver.page_source
    # time.sleep(5)
    #
    # for i in range(3):  # 测试三次下拉
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    #     time.sleep(3)

    # driver .close()
