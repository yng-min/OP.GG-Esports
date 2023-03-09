# -*- coding: utf-8 -*-

import requests

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def player_info_by_team(tournamentId: str, teamId: str):
    """
    OP.GG Esports의 선수 정보 데이터 처리를 위해 호출되는 함수
    """
    try:
        query = """
query {
    playersByTournamentAndTeam(tournamentId: "%s", teamId: "%s") {
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
""" % (tournamentId, teamId)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            players = result.json()['data']['playersByTournamentAndTeam']

            if players == []:
                return { "error": False, "code": "SUCCESS", "message": "선수 정보 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": players }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
