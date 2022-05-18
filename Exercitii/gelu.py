from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


class Scraper:

    def __init__(self, cod_produs):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.cod_produs = cod_produs
        self.pret_emag = self.scraper_emag()
        self.pret_altex = self.scraper_altex()

        self.descriere_emag = None
        self.pret_emag = None
        self.pret_altex = None
        self.descriere_altex = None
        self.pret_produs_emag = None
        self.cod_produs = None


    def scraper_emag(self):
        self.browser.get('https://www.emag.ro/#opensearch')
        get_element = self.browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(f'{self.cod_produs}')
        get_element.submit()
        descriere_produs_emag = self.browser.find_element(by=By.ID, value="card_grid")
        self.descriere_emag = descriere_produs_emag.text.split('\n')
        self.pret_produs_emag = self.browser.find_element(by=By.XPATH,
                                                          value=f'//*[@id="card_grid"]/div/div/div/div[4]/div[1]/p[2]')
        self.pret_emag = self.pret_produs_emag.text.removesuffix(' Lei')
        self.browser.close()
        return self.descriere_emag, self.pret_emag

    def scraper_altex(self):
        self.browser.get(f'https://altex.ro/cauta/?q={self.cod_produs}')
        pret_produs_altex = self.browser.find_element(by=By.XPATH,
                                                      value=f'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                            f'2]/div/ul[2]/li/a/div[5]/div/div[2]/span[1]')
        descriere_produs_altex = self.browser.find_element(by=By.XPATH,
                                                           value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                                 '2]/div/ul[2]/li/a')
        self.descriere_altex = descriere_produs_altex.text.split('\n')
        self.pret_altex = pret_produs_altex.text
        self.browser.close()
        return self.descriere_altex, self.pret_altex


    def __str__(self):
        return f'{self.cod_produs} - ', f'Pret Altex: {self.pret_altex} RON, ', f'Pret Emag = {self.pret_emag} RON'


if __name__ == '__main__':
    plita = Scraper('EIS62449')


























    def scraper_emag(self):
        self.browser.get('https://www.emag.ro/#opensearch')
        get_element = self.browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(f'{self.cod_produs}')
        get_element.submit()
        descriere_produs_emag = self.browser.find_element(by=By.ID, value="card_grid")
        self.descriere_emag = descriere_produs_emag.text.split('\n')
        self.pret_produs_emag = self.browser.find_element(by=By.XPATH,
                                                          value=f'//*[@id="card_grid"]/div/div/div/div[4]/div[1]/p[2]')
        self.pret_emag = self.pret_produs_emag.text.removesuffix(' Lei')
        return self.descriere_emag, self.pret_emag

    def scraper_altex(self):
        self.browser.get(f'https://altex.ro/cauta/?q={self.cod_produs}')
        pret_produs_altex = self.browser.find_element(by=By.XPATH,
                                                      value=f'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                            f'2]/div/ul[2]/li/a/div[5]/div/div[2]/span[1]')
        descriere_produs_altex = self.browser.find_element(by=By.XPATH,
                                                           value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div['
                                                                 '2]/div/ul[2]/li/a')
        self.descriere_altex = descriere_produs_altex.text.split('\n')
        self.pret_altex = pret_produs_altex.text
        return self.descriere_altex, self.pret_altex

    # afisare in DATAFRAME

    def __str__(self):
        dictionar = {'cod produs': f'{self.cod_produs}',
                     'descriere': f'{self.descriere_altex[0]}',
                     'pret': f'{self.pret_altex}',
                     'magazin': 'altex'
                     }, {'cod produs': f'{self.cod_produs}',
                         'descriere': f'{self.descriere_emag[0]}',
                         'pret': f'{self.pret_emag}',
                         'magazin': 'emag'}
        df = pd.DataFrame(dictionar, columns=('cod produs', 'pret', 'magazin'))
        self.df_sortat_pret = df.sort_values(by=['pret'], ascending=True)
        pd.options.display.max_columns = 4
        print(self.df_sortat_pret)

cautare = Scraper()
cautare.cod_produs = 'EIS62449'
cautare.scraper_emag()
# cautare.scarper_altex()
# cautare.__str__()
print(cautare.scraper_emag())