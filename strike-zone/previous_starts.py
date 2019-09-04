import pandas as pd
import requests
from bs4 import BeautifulSoup

class PrevStarts:
    
    def __init__(self, player_id):
        self.url = f"http://www.espn.com/mlb/player/gamelog/_/id/{player_id}/year/2019"

    def get_previous_starts(self):
        dates = {}

        res = requests.get(self.url)
        #print(res.status_code)
        soup = BeautifulSoup(res.text,'lxml')
        table = soup.find_all(lambda tag: tag.name == 'tr' and 
            tag.get('class') == ['oddrow'] or tag.get('class') == ['evenrow'])

        for row in table:
            date = row.find_all('td')
            dates[date[0].text] = date[1].text

        return dates
