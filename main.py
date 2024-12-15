import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
wait = WebDriverWait(driver, 10)
reject_all_element = wait.until(
    expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='QS5gu sy4vM' and @role='none' and text()='Reject all']"))
)

# Click the "Reject all" div
reject_all_element.click()
# reject_element.send_keys(Keys.ENTER)
input_element.send_keys("Hello World" + Keys.ENTER)

time.sleep(10)

driver.quit()
