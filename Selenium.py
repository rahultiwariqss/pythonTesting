#D:\chromedriver_win32\chromedriver.exe
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com")
# # driver.maximize_window()
# # driver.minimize_window()
# # driver.maximize_window()
#
# # print(driver.title)
# # print(driver.page_source)
# # a = driver.current_url
# # print(a)
# # driver.get("https://www.amptify.com")
# # b= driver.current_url
# # print(a+b)
# driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("animals")

# service_obj = Service("D:\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com")
# driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("https://www.amptify.com")
# driver.timeouts.implicit_wait
# driver.find_element(By.CLASS_NAME, "gNO89b").click()

service_obj = Service("D:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")

