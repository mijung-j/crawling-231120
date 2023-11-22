from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # 불필요한 에러 메시지 없애기
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 브라우저 생성
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.naver.com')