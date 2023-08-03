from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from itertools import permutations
import math

driver = webdriver.Chrome(executable_path='/home/benatt/sys_programs/chromedriver')

value_set = ['0', '3', '5', '7', '8']
perms = permutations(value_set)

for val in list(perms)[::-1]:
  v = ''.join(val)
  
  driver.get('https://old-lock-web.2021.ctfcompetition.com/')
  
  input_field = driver.find_element(By.XPATH, '//input[1]')
  input_field.send_keys(v)
  
  submit_button = driver.find_element(By.XPATH, '//input[2]')
  submit_button.click()

  element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//p[2]')))
  if 'Got' in element.text:
    print(element.text)
    break