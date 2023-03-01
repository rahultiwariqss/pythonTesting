from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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

    #Radio button selection using specific name and check if radion button is enabled/selected
    allRadioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    print(len(allRadioButtons))

    for radio in allRadioButtons:
        if radio.get_attribute("value") == "radio2":
            radio.click()
            if radio.is_selected():
                print("Radio is select")
            else:
                print("Radio button is not selected")
            break

# Suggestion Class Example(Dynamic dropdown example

    driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Ind")
    allCountries = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")
    print(len(allCountries))


    for country in allCountries:

        if country.text == "India":
            country.click()
            break

    result= []
    for country in allCountries:
        result.append()

    print(result)


