import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestingSite1:
    #Invoke Webdriver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service_obj = Service("D:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    print(driver.title)
    driver.implicitly_wait(4)

#     #Radio button selection using specific name and check if radion button is enabled/selected
#     allRadioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
#     print(len(allRadioButtons))
#
#     for radio in allRadioButtons:
#         if radio.get_attribute("value") == "radio2":
#             radio.click()
#             if radio.is_selected():
#                 print("Radio is select")
#             else:
#                 print("Radio button is not selected")
#             break
#
# # Suggestion Class Example(Dynamic dropdown example
#
#     driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Ind")
#     allCountries = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")
#     print(len(allCountries))
#
#
#     for country in allCountries:
#
#         if country.text == "India":
#             country.click()
#             break
#
#
#
# # Select drop down
#     dropdown = Select (driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
#     dropdown.select_by_index(1)
#
# # Switch Window Example
#     driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
#     print(driver.title)
#     windows= driver.window_handles
#     driver.switch_to.window(windows[1])
#     print(driver.title)
#     driver.switch_to.window(windows[0])
#     print(driver.title)


# # Switch Window Example
#     driver.find_element(By.XPATH, "//a[contains(text(),'Open Tab')]").click()
#     print(driver.title)
#     win = driver.window_handles
#     driver.switch_to.window(win[1])
#     print(driver.title)

# #Alert Handle
#     driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Rahul")
#     driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
#     print(driver.switch_to.alert.text)
#     driver.switch_to.alert.accept()

#Scroll page
    driver.execute_script("window.scrollBy(0,1200)")
    time.sleep(2)
# ActionsChain

    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()

    driver.execute_script("window.scrollBy(0,100)")
    driver.switch_to.frame("courses-iframe")
    driver.find_element(By.LINK_TEXT, "Blog").click()




