import requests
from bs4 import BeautifulSoup as bs


def data_first_three_pages():
    '''
    Affiche l'équipe, l'année et le % (ratio) des trois premières pages
    '''

    for i in range(3):
        url = 'https://www.scrapethissite.com/pages/forms/?page_num=' + str(i+1)
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')

        for teams in soup.find_all('tr', {'class': 'team'}):
            teams_formatted: str = teams.text.strip().split("\n")
            
            team = teams_formatted[0]
            year_temp = teams_formatted[3].split(" ")
            year = year_temp[len(year_temp)-1]
            ratio_temp = teams_formatted[14].split(" ")
            ratio = ratio_temp[len(ratio_temp)-1]

            print(team + ", " + year + ", " + ratio + "%")

        
data_first_three_pages()