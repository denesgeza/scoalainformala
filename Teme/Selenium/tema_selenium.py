
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    counter = 0
    header = ['Nr. crt.', 'Judet']
    for zi in range(20, 27):
        URL = f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zi}-ianuarie-ora-13-00/'
        browser.get(URL)

        table = browser.find_element(by=By.CLASS_NAME, value="entry-content").text
        lista = table.split('\n')
        # header: list[str] = [i for i in lista if i.startswith('Nr. crt.')]
        # header = re.findall('[A-Z][^A-Z]*', header[0])
        start_index = [lista.index(l) for l in lista if l.startswith('Nr. crt.')]
        end_index = [lista.index(l) for l in lista if l.startswith('43.')]
        try:
            daily_content: list[str] = lista[start_index[0] + 1:end_index[0]]
            splitted_daily_content = [i.split(' ') for i in daily_content]
            for i in splitted_daily_content:
                for j in i:
                    if j == 'Mare' or j == 'Mun.':
                        i.remove(j)
        except IndexError:
            pass
        date = f'{zi}-01'

        if counter == 0:
            header.append(f'{date}')
            counter += 1
            df = pd.DataFrame(splitted_daily_content)
            df = df.iloc[:, [0, 1, 3]]
            df.columns = header
        else:
            header.append(f'{date}')
            df[f'{date}'] = pd.Series(dtype='float64')
            data = [i[3] for i in splitted_daily_content]
            df[f'{date}'] = data
    df.set_index('Nr. crt.', drop=True, inplace=True)
    df.to_csv('covid.csv')

    browser.close()
    print(df)


if __name__ == '__main__':
    main()
