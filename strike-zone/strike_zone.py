import sys
from PyInquirer import prompt
from datetime import datetime
from plotly.graph_objs import Layout
from plotly import offline

from csv_parser import CSVParser
from previous_starts import PrevStarts
from pitch_data import PitchData


class StrikeZone:

    def __init__(self):
        self.player_id_mlb = None
        self.player_id_espn = None
        self.player_name = None
        self.player_team = None
        self.player_dict = {}
        self.year = 2019
        self.filename = 'data/player_ids.csv'

    def main(self):

        parser = CSVParser(self.filename)
        self.player_dict = parser.csv_to_dict()
        
        while self.player_name == None:
            player_name = input("Please enter the pitcher's first and last name or enter q to quit.\n")
            player_name.strip()

            if player_name.lower() == 'q':
                sys.exit()

            if player_name not in self.player_dict.keys():
                print("Sorry, the pitcher does not exist in our database.\n")
            else:
                self.player_name = player_name
                self.player_id_mlb = self.player_dict[player_name][0]
                self.player_id_espn = self.player_dict[player_name][1]
                self.player_team = self.player_dict[player_name][2]

        prev_starts = PrevStarts(self.player_id_espn)
        dates = prev_starts.get_previous_starts()

        questions = [
            {
                'type': 'list',
                'name': 'starting_date',
                'message': 'Please select a starting date.',
                'choices': dates.keys()
            }
        ]

        answer = prompt(questions)
        
        selected_start = answer['starting_date'] + f" {self.year}"
        vs_team = dates[answer['starting_date']]

        pd = PitchData(self.player_id_mlb, selected_start, self.player_team, vs_team)
        
        x_values, y_values = pd.get_pitch_data()

        data = [{
            'type': 'scatter',
            'x': x_values,
            'y': y_values,
            'mode': 'markers',
        }]

        my_layout = Layout(
            title = 'Strike Zone',
            xaxis = {
                'range': [-3, 3],
                'dtick': 0.5
            },
            yaxis = {
                'range': [0, 5],
                'dtick': 0.5
            },
            shapes = [{
                'type': 'rect',
                'x0': -0.708335,
                'y0': 1.5,
                'x1': 0.7,
                'y1': 3.5,
                'line': {
                    'color': 'RoyalBlue',
                },
            }],
            width = 775,
            height = 700,
        )

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename=f'{selected_start}_{self.player_name}.html')

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sz = StrikeZone()
    sz.main()
            




