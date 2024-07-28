
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("https://python.org")
# print(driver.title)
# driver.close()

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from markdownify import markdownify
import os

options = Options()

webdriver_path = '../lib/chromedriver'
print(f'WebDriver Path: {webdriver_path}')

options.binary_location = webdriver_path
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# driver = Chrome(options=options, service=ChromeService(executable_path=f'{os.getcwd()}/lib/chromedriver'))
# driver = Chrome(options=options, service=Service(ChromeDriverManager().install()))
companies = []
rejected = []
with open(f'{os.path.dirname(os.path.realpath(__file__))}/companies.txt', 'r') as f:
  companies = f.readlines()

company_list = []
for company in companies:
  driver = Chrome(options)
  
  l = company.split('.')
  index = l[0].strip()
  l = company.split('-')[0].split(' ')
  name = l[1].strip()
  
  driver.get(f'https://www.google.com/search?q={name}+company+date+founded')
  
  web_element = WebDriverWait(driver, 3).until(lambda x : x.find_element(By.XPATH, '//*[@id="Rzn5id"]/div/a[2]'))
  web_element.click()
  
  try:
    web_element = WebDriverWait(driver, 3).until(lambda x : x.find_element(By.XPATH, '//*/div[@data-attrid="kc:/business/business_operation:founded"]'))
    year = markdownify(web_element.get_attribute('innerHTML')).strip()
    
    l = company.split('-')
    link = l[1].strip()
    
    co = {
      'index': index,
      'name': name,
      'link': link,
      'year': year
    }
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/companies_found.txt', 'a') as appF:
      appF.write(f'\n{co["year"]} {co["index"]}. {co["name"]} - {co["link"]}')
      
    company_list.append(co)
  except TimeoutException as e:
    try:
      web_element = WebDriverWait(driver, 3).until(lambda x : x.find_element(By.XPATH, '//*/div[@data-attrid="wa:/description"]//b[1]'))
      year = markdownify(web_element.get_attribute('innerHTML')).strip()
      
      l = company.split('-')
      link = l[1].strip()
      
      co = {
        'index': index,
        'name': name,
        'link': link,
        'year': year
      }
    except TimeoutException as e:
      with open(f'{os.path.dirname(os.path.realpath(__file__))}/rejects.txt', 'a') as appF:
        appF.write(f'\n{company}')
        
      rejected.append(company)
  except:
    print('Error retrieving element', e)
    rejected.append(company)
  finally:
    driver.close()

company_list = sorted(company_list, 'year', reverse=True)

with open(f'{os.path.dirname(os.path.realpath(__file__))}/companies_found_sorted.txt', 'a') as appF:
  appF.write('\n'.join([f'{co["year"]} {co["index"]}. {co["name"]} - {co["link"]}' for co in company_list]))