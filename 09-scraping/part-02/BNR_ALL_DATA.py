from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# driver = webdriver.Chrome('/Users/denesgeza/Downloads/chromedriver')
browser = webdriver.Chrome(ChromeDriverManager().install())
service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']
# driver.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')

# table = driver.find_element(By.XPATH, value='//*[@id="Datatable"]')
table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
# print(table_text)
lista = table_text.split('\n')
# print(lista)

header_len = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
# print(header)

dictionar = {i: [] for i in header}

for index in range(0, len(header)):
    for i in range(len(header) + int(index), len(lista), len(header)):
        dictionar[header[index]].append(lista[i])

# print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv('BNR_ALL_DATA.csv')