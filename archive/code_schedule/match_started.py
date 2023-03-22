# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def match_started(match_id: str, tournament_id: str, status: str):
    """
    OP.GG Esports API에서 경기가 시작되었을 때 데이터 처리를 위해 호출되는 함수
    """
    try:
        if status != "not_started":
            return { "error": False, "code": "SUCCESS", "message": "조건에 맞지 않는 경기입니다.", "data": None }

        query = """
query {
    matchPreviewByTournament(id: "%s", tournamentId: "%s") {
        teamStats{team{id}}
        teamStats{team{acronym}}
        teamStats{kills}
        teamStats{deaths}
        teamStats{assists}
        teamStats{winRate}
        teamStats{firstTower}
        teamStats{firstBaron}
        teamStats{firstBlood}
        teamStats{firstDragon}
        teamStats{goldEarned}
    }
}
""" % (match_id, tournament_id)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            matches = result.json()['data']['matchPreviewByTournament']

            if matches == []:
                return {"error": False, "code": "SUCCESS", "message": "경기 정보 데이터가 없습니다.", "data": None}

            return {"error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": matches}

        else:
            return {"error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None}

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
