# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def player_info(playerId: list):
    """
    OP.GG Esports의 선수 정보 데이터 처리를 위해 호출되는 함수
    """
    try:
        playerIds = ""
        for i in playerId: playerIds += f"{i}, "
        playerIds = playerIds[:-2]
        query = """
query {
    playersByIds(playerIds: [%s]) {
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
""" % (playerIds)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            player = result.json()['data']['playersByIds']

            if player == []:
                return { "error": False, "code": "SUCCESS", "message": "선수 정보 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": player }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
