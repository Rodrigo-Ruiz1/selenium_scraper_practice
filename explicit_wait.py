import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/selenium_drivers/chromedriver_win32/chromedriver.exe")

#specify target link
driver.get("http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

#method to force driver to wait
driver.implicitly_wait(3)

#find_element method to get target by id
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label') , #Element filtration
        'Complete!' #expected text
    )
)