# -*- coding: utf-8 -*-

import requests
import datetime
import pytz

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL

def save_schedule(league_id: str = "null", page: int = 0):
    """
    OP.GG Esports의 경기 일정 데이터 처리를 위해 호출되는 함수
    """
    try:
        now_year = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y")
        now_month = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("X%m").replace("X0", "X").replace("X", "")
        query = """
query {
    pagedAllMatches(status: "not_started", leagueId: %s, year: %s, month: %s, page: %d) {
        id
        tournamentId
        tournament{serie{league{shortName}}}
        name
        originalScheduledAt
        scheduledAt
        status
    }
}
""" % (league_id, now_year, now_month, page)
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        if 200 <= result.status_code < 300:
            matches = result.json()['data']['pagedAllMatches']

            if matches == []:
                return { "error": False, "code": "SUCCESS", "message": "경기 일정 데이터가 없습니다.", "data": None }

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": matches }

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}", "data": None }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
