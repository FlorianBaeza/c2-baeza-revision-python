import requests
from bs4 import BeautifulSoup as bs


def countries_capitals_list():
    '''
    Affiche la liste des pays présente à l'URL spécifiée, ainsi que leurs capitales
    '''

    url = 'https://www.scrapethissite.com/pages/simple/'
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    for country in soup.find_all('div', {'class': 'country'}):
        country_formatted: str = country.text.strip()
        
        country_name = country_formatted.split("\n")[0]
        country_capital = country_formatted.split("\n")[3].split("Capital: ")[1]

        print(country_name + " " + country_capital)

        
countries_capitals_list()