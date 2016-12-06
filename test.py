from selenium import webdriver
import os
import time
# chromedriver = "./chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
browser = webdriver.PhantomJS()
# browser.implicitly_wait(10)
browser.get('http://xxf1995.github.io/')
time.sleep(5)
browser.save_screenshot('test.png')
browser.quit()