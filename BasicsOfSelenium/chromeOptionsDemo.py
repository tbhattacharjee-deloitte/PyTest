from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

chromeDriverLoc = "C:/Users/tbhattacharjee/Desktop/jars and drivers/drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriverLoc, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)