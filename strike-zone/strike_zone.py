import sys
from itertools import chain
from PyInquirer import prompt
from datetime import datetime
import plotly.graph_objects as go
from plotly import offline

from csv_parser import CSVParser
from previous_starts import PrevStarts
from pitch_data import PitchData
import pitch_glossary as pg


class StrikeZone:

    def __init__(self):
        self.player_id_mlb = None
        self.player_id_espn = None
        self.player_name = None
        self.player_team = None
        self.player_dict = {}
        self.team_dict = {}
        self.year = 2019
        self.filename = 'data/player_ids.csv'
        

    def main(self):

        playerParser = CSVParser(self.filename)
        self.player_dict = playerParser.csv_to_playerDict()
        
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
        
        pitches, ptypes, results = pd.get_pitch_data()
        pGlossary = pg.PitchGlossary()
        rGlossary = pg.ResultGlossary()

        fig = go.Figure()

        for ptype in ptypes:
            # All pitches
            pitchList = [p for pitch in list(pitches.values()) for p in pitch if p['pt'] == ptype]
            color = pGlossary.colourMap(ptype)
            name = pGlossary.get_pitch(ptype)
            fig.add_trace(
                go.Scatter(
                    x = [p['px'] for p in pitchList],
                    y = [p['pz'] for p in pitchList],
                    marker_color=color,
                    name=name,
                    visible=True,
                    mode="markers",
                    hovertemplate= '%{text}<extra></extra>',
                    text = [f"Pitch Type: {name} <br>Velocity: {p['pv']}"
                        for p in pitchList],
                )
            )

        for result in results:
            pitchList = [p[-1] for p in list(pitches.values()) if p[-1]['result'] == result]
            fig.add_trace(
                go.Scatter(
                    x = [p['px'] for p in pitchList],
                    y = [p['pz'] for p in pitchList],
                    marker_color=[rGlossary.colourMap(p['result']) for p in pitchList],
                    name=result,
                    visible=False,
                    mode="markers",
                    hovertemplate= '%{text}<extra></extra>',
                    text = [f"Pitch Type: {pGlossary.get_pitch(p['pt'])}<br>{p['result']} <br>Velocity: {p['pv']}" 
                        for p in pitchList],
                )
            )

        boolArray = [True for i in range(len(ptypes))]
        boolArray.extend([False for j in range(len(results))])
        notBoolArray = [not b for b in boolArray]

        fig.update_layout(
            updatemenus=[
                go.layout.Updatemenu(
                    type="buttons",
                    direction="right",
                    active=0,
                    x=0.57,
                    y=1.2,
                    buttons=list([
                        dict(
                            label="All Pitches",
                            method="update",
                            args=
                            [
                                {"visible": boolArray}
                            ]
                        ),
                        dict(
                            label="Final Pitches",
                            method="update",
                            args=
                            [
                                {"visible": notBoolArray}
                            ]
                        )
                    ])
                )
            ],
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
            width = 800,
            height = 700
        )

        offline.plot(fig, filename=f'{selected_start}_{self.player_name}.html')

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sz = StrikeZone()
    sz.main()
            




