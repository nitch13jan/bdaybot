import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()

elem.send_keys("bdaybottest@gmail.com")
elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys("12345679")
elem.send_keys(Keys.RETURN)
delay = 100
  
try:
    elem=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,"_2s25")))
    time.sleep(5);
    elem.click();
    print("Successfully Logged in");
except TimeoutException:
    print("Timeout or wrong email/password");
    driver.close();
  
posts=[]
try:
    posts=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,'userContentWrapper')))
    posts=driver.find_elements_by_class_name('userContentWrapper')
    for post in posts:
        post_text=post.find_element_by_class_name('userContent').text
        post.find_element_by_xpath(".//a[@class='UFILikeLink']").click()
    print("Successfully liked relevant posts");
except TimeoutException:
    print("Timeout");