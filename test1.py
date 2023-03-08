from code_schedule.match_completed import *
from code_schedule.match_started import *
from code_schedule.save_schedule import *
from code_schedule.update_schedule import *

print(match_completed(match_info={"matchId": "19972","type": "complete","set": 2,"title": "Semifinal 2: GEN vs DRX","winner": "DRX","winnerName": "DRX","dpm": "GEN Ruler","dtpm": "DRX Kingen","gold": "DRX Deft","cs": "DRX Zeka","firstBlood": "GEN Ruler","mvp": "DRX Zeka","league": "Worlds"}))
print() # 칸 띄우기
print(match_started(match_info={'id': '21000', 'tournamentId': '1021', 'tournament': {'serie': {'league': {'shortName': 'LLA'}}}, 'name': '6K vs EST', 'originalScheduledAt': '2023-03-08T22:00:00.000Z', 'scheduledAt': '2023-03-08T22:00:00.000Z', 'status': 'not_started'}))
print() # 칸 띄우기
print(save_schedule())
print() # 칸 띄우기
print(update_schedule(match_info={"matchId":"20014","type":"reschedule","scheduledAt":None,"originalScheduledAt":"2022-10-03T06:00:00.000Z","title":"Tiebreaker: LLL vs TBD","league":"Worlds"}))
print() # 칸 띄우기

# match = match_completed(match_info={"matchId":"19925","type":"complete","set":3,"title":"Elimination match 1: MAD vs SGB","winner":"MAD","winnerName":"MAD Lions","dpm":"SGB Shogun","dtpm":"SGB Shogun","gold":"SGB Shogun","cs":"MAD Nisqy","firstBlood":"SGB Shogun","mvp":"MAD Elyoya","league":"Worlds"})
# print(match['data']['match_id'])
# print() # 칸 띄우기
# match = match_started(match_info={'id': '21000', 'tournamentId': '1021', 'tournament': {'serie': {'league': {'shortName': 'LLA'}}}, 'name': '6K vs EST', 'originalScheduledAt': '2023-03-08T22:00:00.000Z', 'scheduledAt': '2023-03-08T22:00:00.000Z', 'status': 'not_started'})
# print(match['data']['match_id'])
# print() # 칸 띄우기
# match = save_schedule()
# print(match['data'][0]['id'])
# print() # 칸 띄우기
# match = update_schedule(match_info={"matchId":"20014","type":"reschedule","scheduledAt":None,"originalScheduledAt":"2022-10-03T06:00:00.000Z","title":"Tiebreaker: LLL vs TBD","league":"Worlds"})
# print(match['data']['match_id'])
# print() # 칸 띄우기
