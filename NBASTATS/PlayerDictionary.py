# NBA API
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# Player Dictionary
def shotChartdet(player_name, season_id):
    nba_players= players.get_players()
    player_dict=[player for player in nba_players if player['full_name']==player_name][0]
    print(player_dict)
    player_info=commonplayerinfo.CommonPlayerInfo(player_id= 1628369)
    JT= player_info.get_normalized_dict()
    print(JT)

# Print Jayson Tatum's dictionary
if __name__ == "__main__":
    shotChartdet("Jayson Tatum", "2019-20")
