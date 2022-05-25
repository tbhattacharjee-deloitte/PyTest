import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# Dynamic dropdown

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

print(len(countries))

for i in countries:
    if i.text == "India":
        i.click()

print(driver.find_element(By.ID, "autosuggest").get_attribute('value'))
assert driver.find_element(By.ID, "autosuggest").get_attribute('value') == "India"
