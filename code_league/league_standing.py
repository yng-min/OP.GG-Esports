# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def league_standings(tournamentId: str):
    """
    OP.GG Esports에서 리그 순위 데이터 처리를 위해 호출되는 함수
    """
    try:
        query = """
query {
    standings(tournamentId: "%s") {
        position
        previously
        setWin
        setLose
        team{id}
        team{name}
        team{acronym}
        team{nationality}
        team{foundedAt}
        team{imageUrl}
        team{youtube}
        team{twitter}
        team{instagram}
        team{facebook}
        team{website}
        recentMatches{id}
        recentMatches{tournamentId}
    }
}
""" % tournamentId
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            matches = result.json()['data']['standings']

            if matches == []:
                return { "error": False, "code": "SUCCESS", "data": "리그 순위 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": matches }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
