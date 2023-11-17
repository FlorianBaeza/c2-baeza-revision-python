import requests
from bs4 import BeautifulSoup as bs
import csv


def data_ten_pages_csv():
    '''
    Enregistre dans un csv les lignes des 10 premières pages si leur ratio est positif
    '''

    file = open("result.csv", "w", encoding="utf-8")
    csv_writter = csv.writer(file)

    for i in range(10):
        url = 'https://www.scrapethissite.com/pages/forms/?page_num=' + str(i+1)
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')

        for team in soup.find_all('tr', {'class': 'team'}):
            team_formatted: str = team.text.strip().split("\n")

            team_formatted = [item.strip() for item in team_formatted if item.strip()]

            if len(team_formatted) == 8:
                team_formatted.insert(4, "")

            if int(team_formatted[8]) > 0:
                csv_writter.writerow(team_formatted)

    file.close()
        
data_ten_pages_csv()