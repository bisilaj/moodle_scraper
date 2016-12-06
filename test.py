from selenium import webdriver
import os
import time
browser = webdriver.Safari()
# chromedriver = "./chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
browser.get('http://xxf1995.github.io/')
# browser.execute_script("document.body.style.zoom=(top.window.screen.height-70)/Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
time.sleep(5)
browser.save_screenshot('test_safari.png')
browser.quit()