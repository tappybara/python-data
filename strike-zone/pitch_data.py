import requests

from bs4 import BeautifulSoup
from datetime import datetime

class PitchData:

    def __init__(self, player_id, date, player_team, vs_team):
        self.player_id = player_id
        self.date = date
        self.vs_team = vs_team
        self.player_team = player_team

    def format_date(self):
        # Format will be eg. Sep 1 2019
        # Resulting format should be 2019_09_01
        date = datetime.strptime(self.date, "%b %d %Y")
        date = date.strftime('%Y_%m_%d')
        return date

    def format_teams(self):
        split = self.vs_team.split(' ')
        isHome = (split[0] == 'vs')

        if isHome:
            return f"{split[1].lower()}mlb_{self.player_team.lower()}mlb_1"
        else:
            return f"{self.player_team.lower()}mlb_{split[1].lower()}mlb_1"

    def format_url(self):
        date = self.format_date()
        teams = self.format_teams()

        return f"http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel={self.player_id}&game=gid_{date}_{teams}/&s_type=&h_size=700&v_size=500"
        

    def get_pitch_data(self):
        url = self.format_url()

        res = requests.get(url)
        #print(res.status_code)
        soup = BeautifulSoup(res.content,'lxml')
        table = soup.find_all('tr')[1:]
        
        x_values, y_values = [], []

        for row in table:
            data = row.find_all('td')
            px = data[-6].text
            pz = data[-5].text

            x_values.append(px)
            y_values.append(pz)
        
        return x_values, y_values
            

        


        