#!/usr/bin/env ruby

require 'selenium-webdriver'

wd = Selenium::WebDriver.for :remote, url: 'http://10.3.1.7:4444/wd/hub', desired_capabilities: :chrome
wd.navigate.to 'https://snipt.net/restrada/python-selenium-workaround-for-full-page-screenshot-using-chromedriver-2x/'

# Get the actual page dimensions using javascript
#
width  = wd.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
height = wd.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

# Add some pixels on top of the calculated dimensions for good
# measure to make the scroll bars disappear
#
wd.manage.window.resize_to(width+100, height+100)

img = wd.screenshot_as(:png)

File.open('full-page.png', 'w+') do |fh|
  fh.write img
end

wd.quit