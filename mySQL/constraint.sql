-- 1. 후보선수는 한 팀에서 경기당 최대 9명까지 가능하다.
CREATE ASSERTION SUB_PLAYERS_CONSTRAINT
CHECK ( NOT EXISTS ( SELECT match_id, count(*)
                        FROM MATCH_SUB
                        GROUP BY match_id
                        HAVING count(*) > 9 ));

-- 2. 한 팀에서 경기당 교체선수는 최대 5명까지 가능하다.
CREATE ASSERTION SUB_PLAYERS_CONSTRAINT
CHECK (NOT EXISTS ( SELECT match_id, club_id, count(*)
                        FROM INOUT_OF
                        GROUP BY match_id, club_id
                        HAVING count(*) > 5 ));