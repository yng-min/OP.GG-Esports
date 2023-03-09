from code_league.league_standing import *
from code_league.player_info_by_team import *
from code_league.player_mvp_rank import *

print(league_standing(tournamentId="1018"))
print()

print(player_info_by_team(tournamentId="1018", teamId="385"))
print()

print(player_mvp_rank(tournamentId="1018", limit=10, page=0))
print()


# for i in range(5):
#     data = player_info_by_team(tournamentId="1018", teamId="385") # LCK, T1
#     player_nickName = data['data'][i]['player']['nickName']
#     player_position = data['data'][i]['player']['position']
#     player_games = data['data'][i]['playerStat']['games']
#     player_winRate = (data['data'][i]['playerStat']['winRate'] * 100).__round__(1)
#     player_wins = data['data'][i]['playerStat']['wins']
#     player_loses = data['data'][i]['playerStat']['loses']
#     player_kda = data['data'][i]['playerStat']['kda'].__round__(2)
#     player_kills = data['data'][i]['playerStat']['kills'].__round__(2)
#     player_deaths = data['data'][i]['playerStat']['deaths'].__round__(2)
#     player_assists = data['data'][i]['playerStat']['assists'].__round__(2)

#     print(f"Player: {player_nickName}")
#     print(f"Position: {player_position}")
#     print(f"Total Games: {player_games}")
#     print(f"Win Rate: {player_winRate}%")
#     print(f"Win: {player_wins}")
#     print(f"Lose: {player_loses}")
#     print(f"KDA: {player_kda}")
#     print(f"Kill: {player_kills}")
#     print(f"Death: {player_deaths}")
#     print(f"Assist: {player_assists}")
#     print()
