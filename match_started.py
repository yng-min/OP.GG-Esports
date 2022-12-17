# -*- coding: utf-8 -*-

def match_started(self):

    try:
        matchesDB = sqlite3.connect(r"./Data/matches.sqlite", isolation_level=None)
        matchesCURSOR = matchesDB.cursor()

        box_matches = []
        box_dates = []
        box_info = []
        box_teams = []
        box_league = []
        for i in range(16):
            result = matchesCURSOR.execute(f"SELECT * FROM {leagues[i]['shortName']}").fetchall()
            box_matches.append(result)
            if box_matches[i] != []:
                for j in range(len(result)):
                    box_dates.append(box_matches[i][j][4])
                    box_info.append(f"{box_matches[i][j][0]} {box_matches[i][j][1]}")
                    box_teams.append(box_matches[i][j][2])
                    box_league.append(f"{leagues[i]['shortName']}/{leagues[i]['region']}")

        # 현재 시간
        time_nowDay = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d")
        time_nowTime = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("X%m월 X%d일").replace("X0", "").replace("X", "")

        time_nowDetail = datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%H:%M:00")
        # time_nowDetail = "18:00:00" # 테스트용
        # time_nowDetail = "19:30:00" # 테스트용

        for j in range(len(box_dates)):
            date_day = box_dates[j].split(" ")[0]
            date_detail = box_dates[j].split(" ")[1]

            if date_day == time_nowDay:
                # 전송 시간
                time_earlyDetail_1_hour = date_detail[0:2]
                time_earlyDetail_1_minute = date_detail[3:5]
                # 24시간제 계산
                if time_earlyDetail_1_hour == "00": time_earlyDetail_1_hour = "24" # 만약 0시일 때, 시간을 24으로 바꿔줌 --> 00:00이면 24:00으로 바꿔줌 / 그럼 밑에서 최종 23:50이 됨
                if time_earlyDetail_1_minute == "00": time_earlyDetail_1_minute, time_earlyDetail_1_hour = "60", f"{int(time_earlyDetail_1_hour) - 1}" # 만약 0분일 때, 시간을 -1해주고 분을 60으로 바꿔줌 --> 18:00이면 17:60으로 바꿔줌 / 그럼 밑에서 최종 17:50이 됨
                if int(time_earlyDetail_1_hour) < 10: time_earlyDetail_1_hour = f"0{time_earlyDetail_1_hour}" # 시간이 열자리일 때, 0을 붙여줌
                time_earlyDetail = f"{time_earlyDetail_1_hour}:{int(time_earlyDetail_1_minute) - 30}:00"

                matchID = box_info[j].split(" ")[0]
                tournamentID = box_info[j].split(" ")[1]
                matchTitle = box_teams[j]

                # 경기 시작 알림
                if date_detail == time_nowDetail:
                    print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                    print("경기 일정 알림 전송 중...")

                    url = "https://qwer.gg/matches/graphql"
                    query = """
query {
matchPreviewByTournament(id: "%s", tournamentId: "%s") {
    teamStats{team{id}}
    teamStats{team{acronym}}
    teamStats{kills}
    teamStats{deaths}
    teamStats{assists}
    teamStats{winRate}
    teamStats{firstTower}
    teamStats{firstBaron}
    teamStats{firstBlood}
    teamStats{firstDragon}
    teamStats{goldEarned}
}
}
""" % (matchID, tournamentID)
                    headers = {
                        "Content-Type": "application/json",
                    }

                    result = requests.post(url, json={"query": query}, headers=headers)

                    if 200 <= result.status_code < 300:

                        try:
                            collecting_data = False
                            team_1 = result.json()['data']['matchPreviewByTournament']['teamStats'][0]
                            team_2 = result.json()['data']['matchPreviewByTournament']['teamStats'][1]
                            team_1_id = team_1['team']['id']
                            team_1_acronym = team_1['team']['acronym']
                            team_1_kda = ((team_1['kills'] + team_1['assists']) / team_1['deaths']).__round__(2)
                            team_1_kills = team_1['kills'].__round__(2)
                            team_1_deaths = team_1['deaths'].__round__(2)
                            team_1_assists = team_1['assists'].__round__(2)
                            team_1_kda_msg = f"{team_1_kda} 평점 `({team_1_kills} / {team_1_deaths} / {team_1_assists})`"
                            team_1_winRate = f"{(team_1['winRate'] * 100).__round__(1)}"
                            team_1_firstTower = f"{(team_1['firstTower'] * 100).__round__(1)}"
                            team_1_firstBaron = f"{(team_1['firstBaron'] * 100).__round__(1)}"
                            team_1_firstBlood = f"{(team_1['firstBlood'] * 100).__round__(1)}"
                            team_1_firstDragon = f"{(team_1['firstDragon'] * 100).__round__(1)}"
                            team_1_goldEarned = f"{(team_1['goldEarned']).__round__().__str__()[0:2]}K"
                            team_2_id = team_2['team']['id']
                            team_2_acronym = team_2['team']['acronym']
                            team_2_kda = ((team_2['kills'] + team_2['assists']) / team_2['deaths']).__round__(2)
                            team_2_kills = team_2['kills'].__round__(2)
                            team_2_deaths = team_2['deaths'].__round__(2)
                            team_2_assists = team_2['assists'].__round__(2)
                            team_2_kda_msg = f"{team_2_kda} 평점 `({team_2_kills} / {team_2_deaths} / {team_2_assists})`"
                            team_2_winRate = f"{(team_2['winRate'] * 100).__round__(1)}"
                            team_2_firstTower = f"{(team_2['firstTower'] * 100).__round__(1)}"
                            team_2_firstBaron = f"{(team_2['firstBaron'] * 100).__round__(1)}"
                            team_2_firstBlood = f"{(team_2['firstBlood'] * 100).__round__(1)}"
                            team_2_firstDragon = f"{(team_2['firstDragon'] * 100).__round__(1)}"
                            team_2_goldEarned = f"{(team_2['goldEarned']).__round__().__str__()[0:2]}K"

                        except IndexError:
                            collecting_data = True
                            team_1_acronym = f"{matchTitle.split(' vs ')[0]}"
                            team_2_acronym = f"{matchTitle.split(' vs ')[1]}"

                        try: # 셋업된 채널 불러오기
                            scheduleURL = f"https://qwer.gg/ko/matches/{matchID}"

                            for data_guild in os.listdir(r"./Data/Guild"):

                                if data_guild.endswith(".sqlite"):
                                    guildDB = sqlite3.connect(rf"./Data/Guild/{data_guild}", isolation_level=None)
                                    guildCURSOR = guildDB.cursor()
                                    notice_answer = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][1]
                                    channel_id = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][4]
                                    role_id = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][5]

                                    leagueLCO = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][1]
                                    leaguePCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][2]
                                    leagueLLA = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][3]
                                    leagueLCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][4]
                                    leagueLEC = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][5]
                                    leagueVCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][6]
                                    leagueLCL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][7]
                                    leagueLJL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][8]
                                    leagueTCL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][9]
                                    leagueCBLOL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][10]
                                    leagueOPL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][11]
                                    leagueWorlds = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][12]
                                    leagueLMS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][13]
                                    leagueLPL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][14]
                                    leagueLCK = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][15]
                                    leagueMSI = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][16]

                                    guildDB.close()

                                    if (channel_id) and (notice_answer == 1):

                                        if ((box_league[j].split("/")[0] == "LCO") and (leagueLCO == 1)) or ((box_league[j].split("/")[0] == "PCS") and (leaguePCS == 1)) or ((box_league[j].split("/")[0] == "LLA") and (leagueLLA == 1)) or ((box_league[j].split("/")[0] == "LCS") and (leagueLCS == 1)) or ((box_league[j].split("/")[0] == "LEC") and (leagueLEC == 1)) or ((box_league[j].split("/")[0] == "VCS") and (leagueVCS == 1)) or ((box_league[j].split("/")[0] == "LCL") and (leagueLCL == 1)) or ((box_league[j].split("/")[0] == "LJL") and (leagueLJL == 1)) or ((box_league[j].split("/")[0] == "TCL") and (leagueTCL == 1)) or ((box_league[j].split("/")[0] == "CBLOL") and (leagueCBLOL == 1)) or ((box_league[j].split("/")[0] == "OPL") and (leagueOPL == 1)) or ((box_league[j].split("/")[0] == "Worlds") and (leagueWorlds == 1)) or ((box_league[j].split("/")[0] == "LMS") and (leagueLMS == 1)) or ((box_league[j].split("/")[0] == "LPL") and (leagueLPL == 1)) or ((box_league[j].split("/")[0] == "LCK") and (leagueLCK == 1)) or ((box_league[j].split("/")[0] == "MSI") and (leagueMSI == 1)):

                                            channel_notice = self.bot.get_channel(channel_id)

                                            msg_content = f"<@&{role_id}>"
                                            msg_title = f"> 📢 {time_nowTime} 경기 시작 알림"
                                            # msg_title = f"> 📢 {time_nowTime} 경기 시작 알림 (테스트)"
                                            msg_description = f"```{team_1_acronym} vs {team_2_acronym} ({box_league[j]})```"

                                            embed = discord.Embed(title=msg_title, description=msg_description, color=colorMap['red'])
                                            embed.set_footer(text="TIP: 아래 버튼을 눌러 승부 예측 미니게임을 즐길 수 있어요.", icon_url=self.bot.user.display_avatar.url)
                                            embed.set_image(url=banner_image_url)

                                            if collecting_data == True:
                                                embed.add_field(name="\u200b", value=f"**> __{team_1_acronym}__ 팀 정보**\n매치 데이터를 수집하고 있습니다.", inline=False)
                                            elif collecting_data == False:
                                                embed.add_field(name="\u200b", value=f"**> __{team_1_acronym}__ 팀 정보**", inline=False)
                                                embed.add_field(name="KDA 정보", value=team_1_kda_msg, inline=False)
                                                embed.add_field(name="세트 승률", value=team_1_winRate + "%", inline=True)
                                                embed.add_field(name="첫 킬률", value=team_1_firstBlood + "%", inline=True)
                                                embed.add_field(name="첫 타워 파괴율", value=team_1_firstTower + "%", inline=True)
                                                embed.add_field(name="첫 드래곤 처치율", value=team_1_firstDragon + "%", inline=True)
                                                embed.add_field(name="첫 바론 처치율", value=team_1_firstBaron + "%", inline=True)
                                                embed.add_field(name="골드 획득량", value=team_1_goldEarned, inline=True)

                                            if collecting_data == True:
                                                embed.add_field(name="\u200b", value=f"**> __{team_2_acronym}__ 팀 정보**\n매치 데이터를 수집하고 있습니다.", inline=False)
                                            elif collecting_data == False:
                                                embed.add_field(name="\u200b", value=f"**> __{team_2_acronym}__ 팀 정보**", inline=False)
                                                embed.add_field(name="KDA 정보", value=team_2_kda_msg, inline=False)
                                                embed.add_field(name="세트 승률", value=team_2_winRate + "%", inline=True)
                                                embed.add_field(name="첫 킬률", value=team_2_firstBlood + "%", inline=True)
                                                embed.add_field(name="첫 타워 파괴율", value=team_2_firstTower + "%", inline=True)
                                                embed.add_field(name="첫 드래곤 처치율", value=team_2_firstDragon + "%", inline=True)
                                                embed.add_field(name="첫 바론 처치율", value=team_2_firstBaron + "%", inline=True)
                                                embed.add_field(name="골드 획득량", value=team_2_goldEarned, inline=True)

                                            msg = await channel_notice.send(msg_content, embed=embed)
                                            await msg.edit(msg_content, embed=embed, view=BettingButton(self.bot, msg, scheduleURL, matchID, team_1_acronym, team_2_acronym))

                        except Exception as error:
                            print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                            print(traceback.format_exc())

                        print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                        print("경기 일정 알림 전송 완료")

                    else:
                        print(f"Not sent with {result.status_code}, response:\n{result}")

                # 경기 시작 30분 전 알림
                elif time_earlyDetail == time_nowDetail:
                    print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                    print("경기 일정(30분 전) 알림 전송 중...")

                    try: # 셋업된 채널 불러오기
                        scheduleURL = f"https://qwer.gg/ko/matches/{matchID}"

                        for data_guild in os.listdir(r"./Data/Guild"):

                            if data_guild.endswith(".sqlite"):
                                guildDB = sqlite3.connect(rf"./Data/Guild/{data_guild}", isolation_level=None)
                                guildCURSOR = guildDB.cursor()
                                notice_answer = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][2]
                                channel_id = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][4]
                                role_id = guildCURSOR.execute("SELECT * FROM main").fetchall()[0][5]

                                leagueLCO = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][1]
                                leaguePCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][2]
                                leagueLLA = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][3]
                                leagueLCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][4]
                                leagueLEC = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][5]
                                leagueVCS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][6]
                                leagueLCL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][7]
                                leagueLJL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][8]
                                leagueTCL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][9]
                                leagueCBLOL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][10]
                                leagueOPL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][11]
                                leagueWorlds = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][12]
                                leagueLMS = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][13]
                                leagueLPL = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][14]
                                leagueLCK = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][15]
                                leagueMSI = guildCURSOR.execute("SELECT * FROM league").fetchall()[0][16]

                                guildDB.close()

                                if (channel_id) and (notice_answer == 1):

                                    if ((box_league[j].split("/")[0] == "LCO") and (leagueLCO == 1)) or ((box_league[j].split("/")[0] == "PCS") and (leaguePCS == 1)) or ((box_league[j].split("/")[0] == "LLA") and (leagueLLA == 1)) or ((box_league[j].split("/")[0] == "LCS") and (leagueLCS == 1)) or ((box_league[j].split("/")[0] == "LEC") and (leagueLEC == 1)) or ((box_league[j].split("/")[0] == "VCS") and (leagueVCS == 1)) or ((box_league[j].split("/")[0] == "LCL") and (leagueLCL == 1)) or ((box_league[j].split("/")[0] == "LJL") and (leagueLJL == 1)) or ((box_league[j].split("/")[0] == "TCL") and (leagueTCL == 1)) or ((box_league[j].split("/")[0] == "CBLOL") and (leagueCBLOL == 1)) or ((box_league[j].split("/")[0] == "OPL") and (leagueOPL == 1)) or ((box_league[j].split("/")[0] == "Worlds") and (leagueWorlds == 1)) or ((box_league[j].split("/")[0] == "LMS") and (leagueLMS == 1)) or ((box_league[j].split("/")[0] == "LPL") and (leagueLPL == 1)) or ((box_league[j].split("/")[0] == "LCK") and (leagueLCK == 1)) or ((box_league[j].split("/")[0] == "MSI") and (leagueMSI == 1)):

                                        channel_notice = self.bot.get_channel(channel_id)

                                        msg_content = f"<@&{role_id}>"
                                        msg_title = f"> 📢 {time_nowTime} 경기 알림"
                                        # msg_title = f"> 📢 {time_nowTime} 경기 알림 (테스트)"
                                        msg_description = f"30분 뒤 아래 경기가 시작됩니다.\n```{box_teams[j]} ({box_league[j]})```"

                                        embed = discord.Embed(title=msg_title, description=msg_description, color=colorMap['red'])
                                        # embed.set_footer(text="Powered by QWER.GG", icon_url=self.bot.user.display_avatar.url)
                                        embed.set_image(url=banner_image_url)
                                        await channel_notice.send(msg_content, embed=embed, view=LinkButton(scheduleURL), delete_after=1800)

                    except Exception as error:
                        print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                        print(traceback.format_exc())

                    print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
                    print("경기 일정(30분 전) 알림 전송 완료")

    except Exception as error:
        print("\n({})".format(datetime.datetime.now(pytz.timezone("Asia/Seoul")).strftime("%y/%m/%d %H:%M:%S")))
        print(traceback.format_exc())
