import requests

url = "https://qwer.gg/matches/graphql"
query = """
query {
    pagedMvpRankByTournament(tournamentId: "1018", limit: 10, page: 0) {
        mvps{player{id}}
        mvps{player{nickName}}
        mvps{player{nationality}}
        mvps{player{imageUrl}}
        mvps{team{id}}
        mvps{team{name}}
        mvps{team{acronym}}
        mvps{team{nationality}}
        mvps{position}
        mvps{currently}
        mvps{previously}
        mvps{mvpPoint}
        mvps{games}
        mvps{kda}
        mvps{kills}
        mvps{deaths}
        mvps{assists}
    }
}
"""
headers = {
    "Content-Type": "application/json",
}

result = requests.post(url, json={"query": query}, headers=headers)

if 200 <= result.status_code < 300:

    mvps = result.json()['data']['pagedMvpRankByTournament']
    print(mvps)
    # print(f"Webhook sent {result.status_code} ${result.json()}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result}")
