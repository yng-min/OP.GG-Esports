import opgg


print(opgg.season_info(tournamentId="99"))
print()

print(opgg.ban_rank_info(serieId="511", limit=10, page=0))
print()

print(opgg.pick_rank_info(serieId="511", limit=10, page=0))
print()
