-- 1. 골 득점이 많은 팀 순서로 정렬해줘 (Order BY)
    - SELECT *
        FROM CLUB_RESULT
        ORDER BY Goal_for;

-- 2. 모든 경기의 경기당 골 count를 보고 싶어 (GROUP BY)
    - SELECT match_id, count(*)
        FROM GOAL_OF
        GROUP BY match_id;

-- 3. 각 클럽의 클럽 이름, 경기장 이름을 보고 싶어 (JOIN)
    - SELECT club_name, stadium_name
        FROM CLUB_INFO as c JOIN STADIUM as s ON (c.stadium_id=s.stadium_id)

-- 4. 2021.11.07날 승리한 팀의 골 넣은 선수의 이름, 출신나라, 생년월일을 보고 싶어 - 중복 제거! distinct
--     - SELECT player_name, country, date_of_birth
--         FROM MATCH_WIN as mw, MATCH_INFO as mi, GOAL_OF as g, PLAYER as p
--         JOIN mw on
--       -> 수정 필요

-- 5. 첼시(cid=4)에 속한 선수들(팀이름, 선수이름, 포지션)을 보고 싶어
    - SELECT club_name, player_name, position
        FROM PLAYER as p JOIN CLUB_INFO as c ON (p.club_id=c.club_id)
        WHERE club_id=4;

-- 6. 팀에서 저지른 파울(옐로카드 or 레드카드) 총 횟수를 내림차순 정렬해서 보고 싶어
    - SELECT club_name, count(*)
        FROM FOUL_OF as f JOIN CLUB_INFO as c ON (f.club_id=c.club_id)
        GROUP BY club_id
        ORDER BY count(*) DESC;

-- 7. 첼시가 골을 넣은 경기에 대해 match_id,날짜,골수(total_goal)를 보고 싶어. 날짜로 정렬해서 보여줘
    - SELECT match_id, match_date, count(*) as total_goal
        FROM GOAL_OF as g JOIN MATCH_INFO as m ON (g.club_id=m.club_id)
        WHERE club_id=4
        GROUP BY match_id, match_date
        ORDER BY match_date

-- 8. 첼시에서 포지션이 FW인 선수들의 팀이름, 선수이름, 포지션을 보고 싶어
    - SELECT club_name, player_name, position
        FROM CLUB_INFO as c JOIN PLAYER as p (c.club_id=p.club_id)
        WHERE club_id=4 and position='FW'

-- 9. 모든 경기에서 경기당 골 수가 4개 이상인 경기(match_id)를 보고 싶어 (GROUP BY)
    - SELECT match_id, count(*)
        FROM GOAL_OF
        GROUP BY match_id;
        HAVING count(*) >= 4;