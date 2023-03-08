import requests
import json
import datetime

url = "https://qwer.gg/matches/graphql"
query = """
query {
    playersByTournamentAndTeam(tournamentId: "1018", teamId: "385") {
        player{id}
        player{nickName}
        player{firstName}
        player{lastName}
        player{position}
        player{nationality}
        player{imageUrl}
        player{birthday}
        player{stream}
        player{youtube}
        player{twitter}
        player{instagram}
        player{facebook}
        player{discord}
        playerStat{games}
        playerStat{winRate}
        playerStat{wins}
        playerStat{loses}
        playerStat{kills}
        playerStat{deaths}
        playerStat{assists}
        playerStat{kda}
        playerStat{dpm}
        playerStat{dtpm}
        playerStat{gpm}
        playerStat{cspm}
        playerStat{dpgr}
        playerStat{firstBlood}
        playerStat{firstTower}
        playerStat{wardsPlaced}
        playerStat{wardsKilled}
    }
}
"""
headers = {
    "Content-Type": "application/json",
}

result = requests.post(url, json={"query": query}, headers=headers)

if 200 <= result.status_code < 300:

    matches = result.json()['data']['playersByTournamentAndTeam']
    print(matches)
    # print(f"Webhook sent {result.status_code} ${result.json()}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result}")
