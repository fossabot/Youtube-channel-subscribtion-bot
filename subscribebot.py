import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
channel=input("Enter the link of the Youtube channel you want to subscribe to: ")
gmail =input("Enter your Gmail: ")
password =input("Enter your password: ")


browser = webdriver.Chrome(r"C:\Users\David\Downloads\chromedriver_win32\chromedriver.exe")
browser.get(channel)
browser.find_element_by_id("subscribe-button").click()
browser.find_element_by_id("text").click()
browser.find_element_by_id("identifierId").send_keys(gmail)
browser.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
browser.implicitly_wait(4)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
browser.find_element_by_id("subscribe-button").click()


