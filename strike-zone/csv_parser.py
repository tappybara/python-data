import csv

class CSVParser:
    def __init__(self, filename):
        self.filename = filename

    def csv_to_dict(self):
        player_db = {}
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                player_id_mlb = str(row[0])
                player_id_espn = str(row[14])
                player_name = str(row[1])
                player_team = str(row[3])
                player_db[player_name] = [player_id_mlb, player_id_espn, player_team]

        return player_db


