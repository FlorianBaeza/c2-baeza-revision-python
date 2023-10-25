import requests
from bs4 import BeautifulSoup as bs


def countries_list():
    '''
    Affiche la liste des pays présente à l'URL spécifiée
    '''

    url = 'https://www.scrapethissite.com/pages/simple/'
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    for country in soup.find_all('div', {'class': 'country'}):
        country_name: str = country.text
        country_name = country_name.strip().split("\n")[0]

        print(country_name)

        
countries_list()