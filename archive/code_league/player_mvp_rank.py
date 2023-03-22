# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def player_mvp_rank(tournamentId: str, limit: int = 10, page: int = 0):
    """
    OP.GG Esports의 선수 랭킹 데이터 처리를 위해 호출되는 함수
    """
    try:
        query = """
query {
    pagedMvpRankByTournament(tournamentId: "%s", limit: %d, page: %d) {
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
""" % (tournamentId, limit, page)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            mvps = result.json()['data']['pagedMvpRankByTournament']

            if mvps == []:
                return { "error": False, "code": "SUCCESS", "message": "밴 순위 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": mvps }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
