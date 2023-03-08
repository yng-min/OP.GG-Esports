# 경기 정보 관련 코드
from .code_schedule.match_completed import * # OP.GG Esports API에서 경기가 종료되었을 때 데이터 처리를 위해 호출되는 함수
from .code_schedule.match_started import * # OP.GG Esports API에서 경기가 시작되었을 때 데이터 처리를 위해 호출되는 함수
from .code_schedule.save_schedule import * # OP.GG Esports 경기 일정 데이터 정리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_schedule.update_schedule import * # OP.GG Esports API에서 경기 일정이 업데이트 되었을 때 데이터 처리를 위해 호출되는 함수

# 리그 정보 관련 코드
from .code_league.league_standing import * # OP.GG Esports API에서 리그 순위 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
from .code_league.player_info_by_team import * # OP.GG Esports API에서 선수 정보 데이터 처리를 위해 호출되는 함수 (https://esports.op.gg/matches/graphql)
