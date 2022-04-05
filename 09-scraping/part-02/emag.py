from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://www.emag.ro/#opensearch")



driver.get("https://www.emag.ro/#opensearch")
#  Find by ID
get_element = driver.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

time.sleep(5)

# Find by CSS Selector
# search_element = driver.find_element(by=By.CLASS_NAME, value='card-item')
search_element = driver.find_element(by=By.ID, value='card_grid')
# find_element = driver.find_element(by=By.XPATH, value='//*......'
print(search_element.text)