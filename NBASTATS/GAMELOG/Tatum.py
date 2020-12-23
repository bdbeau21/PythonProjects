import pandas as pd 
import numpy as np
from nba_api.stats.static import players
player_dict = players.get_players()

# Find Jayson Tatum ID
tatum = [player for player in player_dict if player['full_name'] == 'Jayson Tatum'][0]
tatum_id = tatum['id']

# Find Chicago Bulls ID
from nba_api.stats.static import teams 
teams = teams.get_teams()
CHI = [x for x in teams if x['full_name'] == 'Chicago Bulls'][0]
CHI_id = CHI['id']


# Load data for all Tatum seasons
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
gamelog_tatum_all = playergamelog.PlayerGameLog(player_id=tatum_id, season = SeasonAll.all)
df_tatum_games_all = gamelog_tatum_all.get_data_frames()[0]

#for i in gamelog_tatum_all:
new=df_tatum_games_all['MATCHUP']
