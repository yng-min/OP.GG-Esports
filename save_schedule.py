# -*- coding: utf-8 -*-

import requests
import datetime
import pytz

time_delta = 9

def save_schedule():
    """
    OP.GG Esports 경기 일정 저장 함수
    """
    try:
        now_time = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d")
        url = "https://qwer.gg/matches/graphql"
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

            temp_originalScheduledAt = []
            box_originalScheduledAt = []
            for i in range(len(matches)):
                temp_originalScheduledAt.append(matches[i]['originalScheduledAt'].replace("T", " ").split(".000Z")[0])
                date_temp = datetime.datetime.strptime(temp_originalScheduledAt[i], "%Y-%m-%d %H:%M:%S")
                date_delta = datetime.timedelta(hours=time_delta)
                time = date_temp + date_delta
                box_originalScheduledAt.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            temp_scheduledAt = []
            box_scheduledAt = []
            for i in range(len(matches)):
                temp_scheduledAt.append(matches[i]['scheduledAt'].replace("T", " ").split(".000Z")[0])
                date_temp = datetime.datetime.strptime(temp_scheduledAt[i], "%Y-%m-%d %H:%M:%S")
                date_delta = datetime.timedelta(hours=time_delta)
                time = date_temp + date_delta
                box_scheduledAt.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            matchesDB = sqlite3.connect(r"./Data/matches.sqlite", isolation_level=None)
            matchesCURSOR = matchesDB.cursor()
            bettingDB = sqlite3.connect(r"./Data/betting.sqlite", isolation_level=None)
            bettingCURSOR = bettingDB.cursor()

            # DB 초기화
            for i in range(16):
                matchesCURSOR.execute(f"DELETE FROM {leagues[i]['shortName']}")
            print("- Table Deleted.")

            webhook_data = {
                "username": "QWER.GG Log",
                "content": "- Table Deleted."
            }
            webhook_result = requests.post(webhook_url, json=webhook_data, headers=webhook_headers)
            if 200 <= webhook_result.status_code < 300: pass
            else: print(f'- [LOG] Not sent with {webhook_result.status_code}, response:\n{webhook_result.json()}')

            # 경기 데이터 저장
            content_msg = ""
            for i in range(len(matches)):
                for j in range(16):
                    try: match_name = matches[i]['name'].split(': ')[1]
                    except: match_name = matches[i]['name']
                    if matches[i]['tournament']['serie']['league']['shortName'] == leagues[j]['shortName']:
                        matchesCURSOR.execute(f"INSERT INTO {leagues[j]['shortName']}(ID, TournamentID, Name, OriginalScheduledAt, ScheduledAt, Status) VALUES(?, ?, ?, ?, ?, ?)", (matches[i]['id'], matches[i]['tournamentId'], match_name, box_originalScheduledAt[i], box_scheduledAt[i], matches[i]['status']))
                        bettingCURSOR.execute(f"INSERT INTO {leagues[j]['shortName']}(ID, TournamentID, Name, TotalBet, TotalPoint, HomeBet, HomePoint, AwayBet, AwayPoint) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (matches[i]['id'], matches[i]['tournamentId'], match_name, 0, 0, 0, 0, 0, 0))
                print(f"- Saved match: [{matches[i]['tournament']['serie']['league']['shortName']}] {match_name} ({matches[i]['id']})")

                content_msg += f"\n- Saved match: `[{matches[i]['tournament']['serie']['league']['shortName']}] {match_name} ({matches[i]['id']})`"

            if content_msg == "": content_msg = "- No matches."

            webhook_data = {
                "username": "QWER.GG Log",
                "content": content_msg
            }
            webhook_result = requests.post(webhook_url, json=webhook_data, headers=webhook_headers)
            if 200 <= webhook_result.status_code < 300: pass
            else: print(f'- [LOG] Not sent with {webhook_result.status_code}, response:\n{webhook_result.json()}')

            matchesDB.close()
            bettingDB.close()

        else:
            print(f"Not sent with {result.status_code}, response:\n{result}")
