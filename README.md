# Tutorials
The tutorials folder contain project tutorials that I have followed from the book 'Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming' written by Eric Matthes.

# Strike-Zone
Strike-Zone is a personal project that I have created after learning more about data mining and graphical visualizations from the aforementioned book.

It is a script written in Python that utilizes web-scraping to retrieve information about a pitcher's previous appearances in the 2019 season MLB season. The information is parsed and ultimately will be displayed as a graphical plot, detailing the pitches they threw and their end results.

It works by first inputting the first and last name of the pitcher. They could be a starter or a reliever. The script will then retrieve the dates of all of the pitcher's appearances. Once a date is selected, the corresponding graph will be generated.

-----------------------------------------------------------------------------------------------------------------------------------------

For this project, information from third parties have been gathered to make everything work. Below is a list of all sources.

MLB Player IDs (file: player_ids.csv): http://crunchtimebaseball.com/baseball_map.html

MLB Team Map (file: SFBB MLB Team Map - SFBB Team Map.csv): https://www.smartfantasybaseball.com/2015/09/new-tool-mlb-team-id-map/

Pitcher's Previous Starts (ESPN MLB Website):  
example url: http://www.espn.com/mlb/player/gamelog/_/id/39251/

Game Information (Brooks Baseball (http://www.brooksbaseball.net/pfxVB/pfx.php)):  
example url: http://www.brooksbaseball.net/pfxVB/pfx.php?month=10&day=18&year=2019&game=gid_2019_10_18_houmlb_nyamlb_1%2F&pitchSel=434378&prevGame=gid_2019_10_18_houmlb_nyamlb_1%2F&prevDate=1018&league=mlb
