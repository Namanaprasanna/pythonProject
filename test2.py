from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.support.select import Select

s=Service("C:\seleniumed\msedgedriver.exe")
driver =webdriver.Edge(service = s)
driver.get('https://automationpractice.com/index.php')
sign_in = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a")
sign_in.click()
time.sleep(2)
driver.find_element_by_name("email_create").send_keys("ghj@gmail.com")
driver.find_element_by_css_selector("#SubmitCreate > span").click()
time.sleep(3)
register = driver.find_element_by_xpath("//*[@id='submitAccount']/span")
register.click()