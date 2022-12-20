# -*- coding: utf-8 -*-

import requests
import datetime
import pytz

url = "https://esports.op.gg/matches/graphql" # OP.GG Esports API URL
time_delta = 9 # 한국에서의 협정세계시 시차

def save_schedule():
    """
    OP.GG Esports 경기 일정 데이터 처리를 위해 호출되는 함수
    """
    try:
        now_time = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d")
        query = """
query {
    upcomingMatchesByDate(date: "%s") {
        id
        tournamentId
        tournament{serie{league{shortName}}}
        name
        originalScheduledAt
        scheduledAt
        status
    }
}
""" % now_time
        headers = {
            "Content-Type": "application/json",
        }

        result = requests.post(url, json={"query": query}, headers=headers)

        # if 200 <= result.status_code < 300:
        #     print(f"Webhook sent {result.status_code} ${result.json()}")
        # else:
        #     print(f"Not sent with {result.status_code}, response:\n{result}")

        if 200 <= result.status_code < 300:
            matches = result.json()['data']['upcomingMatchesByDate']

            if matches == []:
                return { "error": False, "code": "NODATA", "message": "경기 일정 데이터가 없습니다." }
            

            # return { "error": False, "code": "SUCCESS", "team_1": msg_team_1, "team_2": msg_team_2, "match_id": msg_match_id, "match_type": msg_match_type, "match_set": msg_match_set, "match_title": msg_match_title, "match_winner_name": msg_winner_name, "match_winner_shortName": msg_winner_shortName, "dpm": msg_dpm, "dtpm": msg_dtpm, "gold": msg_gold, "cs": msg_cs, "firstBlood": msg_firstBlood, "mvp": msg_mvp, "match_league": msg_league }

            return matches

        else:
            return { "error": True, "code": "NOTSENT", "message": f"서버와의 통신 과정 중 오류가 발생함.\nStatus Code: {result.status_code}\nResponse: {result}" }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}" }
