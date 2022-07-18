import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('maciej')
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('2241')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/a[1]').click()
    driver.find_element(By.XPATH, '/html/body/nav/div/a/span').click()


element_is_clickable()

#response test:
'''
def response_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)

response_check(900, 'test900.png')
response_check(1200, 'test1200.png')
response_check(1800, 'test1800.png')
response_check(600, 'test600.png')
'''