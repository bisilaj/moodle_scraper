#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-01 21:24:50
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $0.1

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import os

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
# browser.implicitly_wait(10)
browser.get('https://moodle.carleton.edu/auth/shibboleth/index.php')
wait1 = WebDriverWait(browser, 10)
wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))

# username = browser.find_element_by_xpath(".//*[@id='username']")
# password = browser.find_element_by_xpath(".//*[@id='password']")
username = browser.find_element_by_css_selector("#username")
password = browser.find_element_by_css_selector("#password")

username.send_keys("xiax")
password.send_keys("-Xxf19951206")
# submit = browser.find_element_by_xpath("html/body/div[1]/div/div/div/form/div[3]/button")
submit = browser.find_element_by_css_selector('.form-element.form-button')
submit.click()

wait2 = WebDriverWait(browser, 20)
wait2.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".no-overflow>p>a")))
time.sleep(3)
# needs to wait for the page fully displayed!
browser.save_screenshot('my_homepage.png')

course_1 = browser.find_element_by_xpath(".//*[@id='inst97373']/div[2]/ol/li[1]/ol/li[2]/ol/li[1]/a")
course_1.click()
browser.save_screenshot('course_1.png')
browser.back()
course_2 = browser.find_element_by_xpath(".//*[@id='inst97373']/div[2]/ol/li[1]/ol/li[2]/ol/li[2]/a")
course_2.click()
browser.save_screenshot('course_2.png')
browser.back()
course_1 = browser.find_element_by_xpath(".//*[@id='inst97373']/div[2]/ol/li[1]/ol/li[2]/ol/li[3]/a")
course_3.click()
browser.save_screenshot('course_3.png')

browser.quit()