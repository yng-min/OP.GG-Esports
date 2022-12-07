# -*- coding: utf-8 -*-

# 패키지 라이브러리 설정
import asyncio
import sqlite3
import random
import time
import json
import datetime
import pytz
import traceback

import requests

leagues = {
    0: {"id": "85", "name": "League of Legends Circuit Oceania", "shortName": "LCO", "region": "OCE"},
    1: {"id": "86", "name": "Pacific Championship Series", "shortName": "PCS", "region": "SEA"},
    2: {"id": "87", "name": "Liga Latinoamérica", "shortName": "LLA", "region": "LAT"},
    3: {"id": "88", "name": "League of Legends Championship Series", "shortName": "LCS", "region": "NA"},
    4: {"id": "89", "name": "League of Legends European Championship", "shortName": "LEC", "region": "EU"},
    5: {"id": "90", "name": "Vietnam Championship Series", "shortName": "VCS", "region": "VN"},
    6: {"id": "91", "name": "League of Legends Continental League", "shortName": "LCL", "region": "CIS"},
    7: {"id": "92", "name": "League of Legends Japan League", "shortName": "LJL", "region": "JP"},
    8: {"id": "93", "name": "Turkish Championship League", "shortName": "TCL", "region": "TR"},
    9: {"id": "94", "name": "Campeonato Brasileiro de League of Legends", "shortName": "CBLOL", "region": "BR"},
    10: {"id": "95", "name": "Oceanic Pro League", "shortName": "OPL", "region": "COE"},
    11: {"id": "96", "name": "League of Legends World Championship", "shortName": "Worlds", "region": "INT"},
    12: {"id": "97", "name": "League of Legends Master Series", "shortName": "LMS", "region": "LMS"},
    13: {"id": "98", "name": "League of Legends Pro League", "shortName": "LPL", "region": "CN"},
    14: {"id": "99", "name": "League of Legends Champions Korea", "shortName": "LCK", "region": "KR"},
    15: {"id": "100", "name": "Mid-Season Invitational", "shortName": "MSI", "region": "INT"}
}



class SaveSchedule():

    def save_schedule(self):
        """
        OP.GG Esports 경기 일정 저장 함수
        """
        try:
            time_nowDetail = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%H:%M")
            # time_nowDetail = "00:00" # 테스트용

            if ("00:00" == time_nowDetail):
                webhook_url = "https://discord.com/api/webhooks/1004831743976689664/iJTrRuleg2KtVPST6Nfo4j4HCNYc9EMla5DnMvWKQbMmrsn0fBuT6i7sG-IkNz6SVDaM"
                webhook_headers = {
                    "Content-Type": "application/json"
                }

                print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                print("경기 일정 저장")

                webhook_data = {
                    "username": "QWER.GG Log",
                    "content": "``` ```\n>>> `({})`\n경기 일정 저장".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S"))
                }
                webhook_result = requests.post(webhook_url, json=webhook_data, headers=webhook_headers)
                if 200 <= webhook_result.status_code < 300: pass
                else: print(f'- [LOG] Not sent with {webhook_result.status_code}, response:\n{webhook_result.json()}')
                
                nowTime = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d")
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
""" % nowTime
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
                        date_delta = datetime.timedelta(hours=9)
                        time = date_temp + date_delta
                        box_originalScheduledAt.append(time.strftime("%Y-%m-%d %H:%M:%S"))

                    temp_scheduledAt = []
                    box_scheduledAt = []
                    for i in range(len(matches)):
                        temp_scheduledAt.append(matches[i]['scheduledAt'].replace("T", " ").split(".000Z")[0])
                        date_temp = datetime.datetime.strptime(temp_scheduledAt[i], "%Y-%m-%d %H:%M:%S")
                        date_delta = datetime.timedelta(hours=9)
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

        except Exception as error:
            print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
            print(traceback.format_exc())





def setup(bot):
    bot.add_cog(RoutineTASK(bot))
    print("routine.py 로드 됨")
