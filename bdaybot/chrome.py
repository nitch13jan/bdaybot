import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()

elem.send_keys("bdaybottest@gmail.com")
elem = driver.find_element_by_name("pass")
elem.clear()

elem.send_keys("12345679")
elem.send_keys(Keys.RETURN)

delay = 30


def post_checker(post):
    happy_word_list = ['happy', 'hapy', 'hapi', 'appy', 'hpy']
    birthday_word_list = ['birthday', 'bday', 'budday', 'b\'day', 'bdy']
    return any(word in post for word in happy_word_list) and (any(word in post for word in birthday_word_list) or
                                                              ('return' in post and 'day' in post))

try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "_2s25")))
    time.sleep(5)
    elem.click()
    print("Successfully Logged in")

except TimeoutException:
    print("Timeout or wrong email/password")
    driver.close()

posts = []

try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "_44b2")))
    time.sleep(5)
    elem.click()
    posts = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'userContentWrapper')))
    time.sleep(8)
    posts = driver.find_elements_by_class_name('userContentWrapper')

    for post in posts:

        post_text = post.find_element_by_xpath(".//div[@class='_5pbx userContent']").text.lower()

        time.sleep(3)

        if post_checker(post_text):

            try:
                post.find_element_by_xpath(".//a[@class='UFILikeLink _4x9- _4x9_ _48-k']").click()

            except:
                pass

    print("Successfully liked relevant posts")

except TimeoutException:
    print("Timeout")

app_secret = 'a508a47755cb78460fde5c52c9b9230f'
app_id = '1178068725594212'
