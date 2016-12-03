from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


email=raw_input("Enter Email ID/ Phone number:")
passw=raw_input("Enter Password:")

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(email)
elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)
delay = 10
try:
    elem=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,"_2s25")))
    elem.click();
    print "Successfully Logged in";
except TimeoutException:
    print "Timeout or wrong email/password";
