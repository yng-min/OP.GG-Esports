import requests
import json
import datetime

url = "https://qwer.gg/matches/graphql"
query = """
query {
    standings(tournamentId: "1018") {
        team{id}
        team{name}
        team{acronym}
        team{nationality}
        team{foundedAt}
        team{imageUrl}
        position
        previously
        setWin
        setLose
        team{youtube}
        team{twitter}
        team{instagram}
        team{facebook}
        team{website}
        recentMatches{id}
        recentMatches{tournamentId}
    }
}
"""
headers = {
    "Content-Type": "application/json",
}

result = requests.post(url, json={"query": query}, headers=headers)

if 200 <= result.status_code < 300:

    matches = result.json()['data']['standings']
    print(matches)
    # print(f"Webhook sent {result.status_code} ${result.json()}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result}")
