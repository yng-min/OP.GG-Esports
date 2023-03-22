import opgg


print(opgg.load_schedule())
print()

print(opgg.save_schedule(league_id="99", page=0))
print()

print(opgg.update_schedule(match_info={"matchId":"20014","type":"reschedule","scheduledAt":None,"originalScheduledAt":"2022-10-03T06:00:00.000Z","title":"Tiebreaker: LLL vs TBD","league":"Worlds"}))
print()
