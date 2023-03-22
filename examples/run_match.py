import opgg


print(opgg.match_completed(match_info={"matchId": "19972","type": "complete","set": 2,"title": "Semifinal 2: GEN vs DRX","winner": "DRX","winnerName": "DRX","dpm": "GEN Ruler","dtpm": "DRX Kingen","gold": "DRX Deft","cs": "DRX Zeka","firstBlood": "GEN Ruler","mvp": "DRX Zeka","league": "Worlds"}))
print()

print(opgg.match_finished(league_id="99", page=0))
print()

print(opgg.match_started(match_id="20714", tournament_id="1018", status="not_started"))
print()
