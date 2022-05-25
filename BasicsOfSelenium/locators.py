from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# accessing locators

driver.find_element(by=By.NAME, value="name").send_keys("tam")
driver.find_element(by=By.XPATH, value="//input[@name='email']").send_keys("hello@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH, "//*[contains(@value, 'Submit')]").click()
message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text
print(message)
assert "Success" in message
