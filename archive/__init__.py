# 경기 정보 관련 코드
from .code_schedule.match_completed import * # OP.GG Esports API에서 경기 결과 데이터 처리를 위해 호출되는 함수
from .code_schedule.match_finished import * # OP.GG Esports의 경기 종료 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_schedule.match_started import * # OP.GG Esports API에서 경기 시작 데이터 처리를 위해 호출되는 함수
from .code_schedule.save_schedule import * # OP.GG Esports의 경기 일정 데이터 정리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_schedule.update_schedule import * # OP.GG Esports API에서 경기 일정 업데이트 데이터 처리를 위해 호출되는 함수

# 리그 정보 관련 코드
from .code_league.league_standing import * # OP.GG Esports의 리그 순위 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_league.player_info_by_team import * # OP.GG Esports의 팀에서 선수 정보 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_league.player_info import * # OP.GG Esports의 선수 정보 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_league.player_mvp_rank import * # OP.GG Esports의 선수 랭킹 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)

# 시즌 정보 관련 코드
from .code_season.ban_pick_info import * # OP.GG Esports의 밴/픽 순위 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
