import requests

url = "https://qwer.gg/matches/graphql"
query = """
query {
    playersByIds(playerIds: ["1939"]) {
        id
        nickName
        firstName
        lastName
        position
        nationality
        imageUrl
        birthday
        stream
        youtube
        twitter
        instagram
        facebook
        discord
    }
}
"""
headers = {
    "Content-Type": "application/json",
}

result = requests.post(url, json={"query": query}, headers=headers)

if 200 <= result.status_code < 300:

    player = result.json()['data']['playersByIds'][0]
    print(player)
    # print(f"Webhook sent {result.status_code} ${result.json()}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result}")

"fragment CorePlayer on Player {\n  id\n  nickName\n  firstName\n  lastName\n  imageUrl\n  birthday\n  nationality\n  position\n  stream\n  youtube\n  twitter\n  facebook\n  instagram\n  discord\n  __typename\n}\n\nfragment CoreTeam on Team {\n  id\n  name\n  acronym\n  imageUrl\n  nationality\n  foundedAt\n  imageUrlDarkMode\n  imageUrlLightMode\n  youtube\n  twitter\n  facebook\n  instagram\n  discord\n  website\n  __typename\n}\n\nquery ListPlayersByIds($playerIds: [ID]!) {\n  playersByIds(playerIds: $playerIds) {\n    ...CorePlayer\n    currentTeam {\n      ...CoreTeam\n      __typename\n    }\n    __typename\n  }\n}"
