import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# iframe, frameset, frame
driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

# frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='tinymce']").clear()
driver.find_element(By.XPATH, "//*[@id='tinymce']").send_keys("I am able to automate")

driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME, "h3").text)
