from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys("bdaybottest@gmail.com")

elem = driver.find_element_by_id("pass")
elem.clear()
elem.send_keys("12345679")

elem=driver.find_element_by_id('u_0_l')
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()
