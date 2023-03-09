from code_schedule.match_completed import *
from code_schedule.match_finished import *
from code_schedule.match_started import *
from code_schedule.save_schedule import *
from code_schedule.update_schedule import *

print(match_completed(match_info={"matchId": "19972","type": "complete","set": 2,"title": "Semifinal 2: GEN vs DRX","winner": "DRX","winnerName": "DRX","dpm": "GEN Ruler","dtpm": "DRX Kingen","gold": "DRX Deft","cs": "DRX Zeka","firstBlood": "GEN Ruler","mvp": "DRX Zeka","league": "Worlds"}))
print()

print(match_finished(league_id="99", page=0))
print()

print(match_started(match_id="20714", tournament_id="1018", status="not_started"))
print()

print(save_schedule(league_id="99", page=0))
print()

print(update_schedule(match_info={"matchId":"20014","type":"reschedule","scheduledAt":None,"originalScheduledAt":"2022-10-03T06:00:00.000Z","title":"Tiebreaker: LLL vs TBD","league":"Worlds"}))
print()
