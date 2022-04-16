import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


def main():
    options = Options()
    options.add_argument("window-size=1400,600")
    ua = UserAgent()
    a = ua.random
    user_agent = ua.random

    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome("/Users/denesgeza/Downloads/chromedriver", options=options)

    title = []
    address = []
    price = []
    surface = []
    desc = []

    for i in range(1, 6):
        url = 'https://www.immoweb.be/fr/recherche/immeuble-de-rapport/a-vendre/liege/4000?page=' + str(i)
        driver.get(url)
        scrap_data(driver, title, address, price, surface, desc)

    df = pd.DataFrame({"Title": title, "Address": address, "Price:": price, "Surface": surface, "Description": desc})
    df.to_csv("output.csv")


def scrap_data(driver, title, address, price, surface, desc):
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("div", {"class": "result-xl"})

    for result in results:
        title.append(result.find("div", {"class": "title-bar-left"}).get_text().strip())
        address.append(result.find("span", {"result-adress"}).get_text().strip())
        price.append(result.find("div", {"class": "xl-price rangePrice"}).get_text().strip())
        surface.append(result.find("div", {"class": "xl-surface-ch"}).get_text().strip())
        desc.append(result.find("div", {"class": "xl-desc"}).get_text().strip())


if __name__ == '__main__':
    main()
