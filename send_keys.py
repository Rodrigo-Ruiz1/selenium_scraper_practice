from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/selenium_drivers/chromedriver_win32/chromedriver.exe")


driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD9, Keys.NUMPAD5)
sum2.send_keys(3)

#try except in case element does not appear
try:

    noThanks = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    noThanks.click()
except:
    print('No element with this class name.')

#CSS_SELECTOR to find target through onclick. google "CSS Selectors Reference" to see how to reference attributes
total = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')

total.click()