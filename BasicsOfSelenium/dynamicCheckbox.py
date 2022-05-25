import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkbox))
for i in checkbox:
    if i.get_attribute('value') == "option2":
        i.click()
        assert i.is_selected()
