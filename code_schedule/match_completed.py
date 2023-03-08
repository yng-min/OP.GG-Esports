# -*- coding: utf-8 -*-

def match_completed(match_info: dict):
    """
    OP.GG Esports API에서 경기가 종료되었을 때 데이터 처리를 위해 호출되는 함수

    - Input:
    {
        "matchId": "19972",
        "type": "complete",
        "set": 2,
        "title": "Semifinal 2: GEN vs DRX",
        "winner": "DRX",
        "winnerName": "DRX",
        "dpm": "GEN Ruler",
        "dtpm": "DRX Kingen",
        "gold": "DRX Deft",
        "cs": "DRX Zeka",
        "firstBlood": "GEN Ruler",
        "mvp": "DRX Zeka",
        "league": "Worlds"
    }

    - Output:
    {
        "error": False,
        "code": "SUCCESS",
        "message": "성공적으로 데이터를 불러왔습니다.",
        "data": {
            "team_1": "GEN",
            "team_2": "DRX",
            "match_id": "19972",
            "match_type": "complete",
            "match_set": "2",
            "match_title": "GEN vs DRX (Worlds)",
            "match_winner_name": "DRX",
            "match_winner_shortName": "DRX",
            "match_league": "Worlds",
            "dpm": "GEN Ruler",
            "dtpm": "DRX Kingen",
            "gold": "DRX Deft",
            "cs": "DRX Zeka",
            "firstBlood": "GEN Ruler",
            "mvp": "DRX Zeka"
        }
    }
    """
    try:
        match = match_info

        if match == None or match == "" or match == {} or match == []:
            return { "error": True, "code": "NOINPUT", "message": "호출된 함수에 대입할 데이터가 없습니다.", "data": None }
        elif match['type'] != "complete":
            return { "error": True, "code": "NOCOMPLETE", "message": "호출된 함수에 대입된 데이터가 경기 종료 데이터가 아닙니다.", "data": None }
        elif match['type'] == "complete":

            if match['dpm'] == "": match['dpm'] = "-"
            if match['dtpm'] == "": match['dtpm'] = "-"
            if match['gold'] == "": match['gold'] = "-"
            if match['cs'] == "": match['cs'] = "-"
            if match['firstBlood'] == "": match['firstBlood'] = "-"
            if match['mvp'] == "": match['mvp'] = "-"

            try: match_name = match['title'].split(': ')[1]
            except: match_name = match['title']
            msg_team_1 = match_name.split(' vs ')[0]
            msg_team_2 = match_name.split(' vs ')[1]
            msg_match_id = match['matchId']
            msg_match_type = match['type']
            msg_match_set = match['set']
            msg_match_title = f"{match_name} ({match['league']})"
            msg_winner_name = match['winnerName']
            msg_winner_shortName = match['winner']
            msg_league = match['league']
            msg_dpm = match['dpm']
            msg_dtpm = match['dtpm']
            msg_gold = match['gold']
            msg_cs = match['cs']
            msg_firstBlood = match['firstBlood']
            msg_mvp = match['mvp']

            return { "error": False, "code": "SUCCESS", "message": "성공적으로 데이터를 불러왔습니다.", "data": { "team_1": msg_team_1, "team_2": msg_team_2, "match_id": msg_match_id, "match_type": msg_match_type, "match_set": msg_match_set, "match_title": msg_match_title, "match_winner_name": msg_winner_name, "match_winner_shortName": msg_winner_shortName, "match_league": msg_league, "dpm": msg_dpm, "dtpm": msg_dtpm, "gold": msg_gold, "cs": msg_cs, "firstBlood": msg_firstBlood, "mvp": msg_mvp } }

    except Exception as error:
        return { "error": True, "code": "UNKNOWN", "message": f"알 수 없는 에러 발생.\n{error}", "data": None }
