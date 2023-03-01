import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("D:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.maximize_window()
# driver.find_element(By.ID, "autosuggest").send_keys("Ind")
# time.sleep(4)
# countries = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/a")
#
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
#
# #driver.find_element(By.XPATH, "//select[@name='ctl00$mainContent$DropDownListCurrency']").click()
# dropDown= Select(driver.find_element(By.XPATH, "//select[@name='ctl00$mainContent$DropDownListCurrency']"))
# dropDown.select_by_index(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
cb = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(cb)

for checkbox in cb:
    if checkbox.get_attribute("Value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
    break

radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
for r in radio:
    if r.get_attribute("Value") == "radio1":
        r.click()
    break

