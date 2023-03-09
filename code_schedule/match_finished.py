# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def match_finished(league_id: str = "null", page: int = 0):
    """
    OP.GG Esports의 경기 종료 데이터 처리를 위해 호출되는 함수
    """
    try:
        query = """
query {
    pagedAllMatches(status: "finished", leagueId: %s, year: null, page: %d) {
        id
        tournamentId
        tournament{serie{league{shortName}}}
        name
        numberOfGames
        awayScore
        awayTeam{id}
        awayTeam{name}
        awayTeam{acronym}
        awayTeam{nationality}
        awayTeam{imageUrl}
        homeScore
        homeTeam{id}
        homeTeam{name}
        homeTeam{acronym}
        homeTeam{nationality}
        homeTeam{imageUrl}
        status
    }
}
""" % (league_id, page)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            matches = result.json()['data']['pagedAllMatches']

            if matches == []:
                return { "error": False, "code": "SUCCESS", "message": "경기 종료 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": matches }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
