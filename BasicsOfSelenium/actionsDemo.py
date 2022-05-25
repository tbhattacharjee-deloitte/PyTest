
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")

# driver.get("https://www.familysearch.org/en/")
# ActionChains

# action.move_to_element(driver.find_element_by_id("search")).perform()

# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
# right click
action.context_click(driver.find_element(By.ID, "double-click")).perform()
# double click
action.double_click(driver.find_element(By.ID, "double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
