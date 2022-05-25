from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com")
print(driver.title)
print(driver.current_url)

# going to another url and going back

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
driver.quit()
