# -*- coding: utf-8 -*-

def match_started(match_info: dict):
    """
    OP.GG Esports API에서 경기가 시작되었을 때 데이터 처리를 위해 호출되는 함수

    - Input:
    {
        'id': '21003',
        'tournamentId': '1021',
        'tournament': {
            'serie': {
                'league': {
                    'shortName': 'LLA'
                }
            }
        },
        'name': 'TK vs INF',
        'originalScheduledAt': '2023-03-08T00:00:00.000Z',
        'scheduledAt': '2023-03-08T00:00:00.000Z',
        'status': 'not_started'
    }

    - Output:
    {
        "error": False,
        "code": "SUCCESS",
        "message": "성공적으로 데이터를 불러왔습니다.",
        "data": {
            "team_1": "TK",
            "team_2": "INF",
            "match_id": "21003",
            "match_type": "not_started",
            "match_title": "TK vs INF (LLA)",
            "match_league": "LLA"
        }
    }
    """
    try:
        match = match_info

        if match == None or match == "" or match == {} or match == []:
            return { "error": True, "code": "NOINPUT", "message": "호출된 함수에 대입할 데이터가 없습니다.", "data": None }
        elif match['status'] != "not_started":
            return { "error": True, "code": "NOCOMPLETE", "message": "호출된 함수에 대입된 데이터가 경기 시작 데이터가 아닙니다.", "data": None }
        elif match['status'] == "not_started":

            try: match_name = match['name'].split(': ')[1]
            except: match_name = match['name']
            msg_team_1 = match_name.split(' vs ')[0]
            msg_team_2 = match_name.split(' vs ')[1]
            msg_match_id = match['id']
            msg_match_type = match['status']
            msg_match_title = f"{match_name} ({match['tournament']['serie']['league']['shortName']})"
            msg_league = match['tournament']['serie']['league']['shortName']

            return {"error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": { "team_1": msg_team_1, "team_2": msg_team_2, "match_id": msg_match_id, "match_type": msg_match_type, "match_title": msg_match_title, "match_league": msg_league } }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
