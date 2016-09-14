from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("8768884446")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys("pnc12102015")
elem.send_keys(Keys.RETURN)
elem.clear()

elem=driver.find_element_by_class_name('_s0 _7ql _ry img')
elem.click()

assert "No results found." not in driver.page_source
driver.close()
