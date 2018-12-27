from selenium import  webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenuim")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()