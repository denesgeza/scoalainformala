from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


browser = webdriver.Chrome(ChromeDriverManager().install())
service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1']
browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')

xpath_header = '//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]'
header = browser.find_element(by=By.XPATH, value=xpath_header)

xpath_content = '//*[@id="post-25121"]/div/div/table[1]/tbody/'
content = browser.find_element(by=By.XPATH, value=xpath_content)

my_string = "blah, lots  ,  of ,  spaces, here "
result = [x.strip() for x in my_string.split(',')]

print(header.text)
print(content.text)

# table_text = table.text
# # print(table_text)
# lista = table_text.split('\n')
# # print(lista)
#
# header_len = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
# header = header_len.text.split('\n')
# # print(header)
#
# dictionar = {i: [] for i in header}
#
# for index in range(0, len(header)):
#     for i in range(len(header) + int(index), len(lista), len(header)):
#         dictionar[header[index]].append(lista[i])
#
# # print(dictionar)
# df = pd.DataFrame(dictionar)
# df.to_csv('BNR_ALL_DATA.csv')