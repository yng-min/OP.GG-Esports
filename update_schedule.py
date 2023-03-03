# -*- coding: utf-8 -*-

def update_schedule(match_info: str):
    """
    OP.GG Esports API에서 경기 일정이 업데이트 되었을 때 데이터 처리를 위해 호출되는 함수

    - Input:
    {
        "matchId": "20014",
        "type": "reschedule",
        "scheduledAt": "2022-10-03T07:00:00.000Z",
        "originalScheduledAt": "2022-10-03T06:00:00.000Z",
        "title": "Tiebreaker: LLL vs TBD",
        "league": "Worlds"
    }

    - Output:
    {
        "error": False,
        "code": "SUCCESS",
        "team_1": "LLL",
        "team_2": "TBD",
        "match_id": "20014",
        "match_type": "reschedule",
        "match_title": "Tiebreaker: LLL vs TBD",
        "match_scheduledAt": "2022-10-03T07:00:00.000Z",
        "match_originalScheduledAt": "2022-10-03T06:00:00.000Z",
        "match_league": "Worlds"
    }
    """
    try:
        match_info = match_info.replace("null", "None")
        match = eval(match_info)

        if match['type'] == "":
            return { "error": True, "code": "NOINPUT", "message": "호출된 함수에 대입할 데이터가 없습니다." }
        elif match['type'] != "reschedule":
            return { "error": True, "code": "NOCOMPLETE", "message": "호출된 함수에 대입된 데이터가 일정 변경 데이터가 아닙니다." }
        if match['type'] == "reschedule":

            try: match_name = match['title'].split(': ')[1]
            except: match_name = match['title']
            msg_team_1 = match_name.split(' vs ')[0]
            msg_team_2 = match_name.split(' vs ')[1]
            msg_match_id = match['matchId']
            msg_match_type = match['type']
            msg_match_title = f"{match_name} ({match['league']})"
            msg_scheduledAt = match['scheduledAt']
            msg_originalScheduledAt = match['originalScheduledAt']
            msg_league = match['league']

            return { "error": False, "code": "SUCCESS", "team_1": msg_team_1, "team_2": msg_team_2, "match_id": msg_match_id, "match_type": msg_match_type, "match_title": msg_match_title, "match_scheduledAt": msg_scheduledAt, "match_originalScheduledAt": msg_originalScheduledAt, "match_league": msg_league }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}" }
