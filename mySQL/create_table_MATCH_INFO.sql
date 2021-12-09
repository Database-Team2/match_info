-- create schema premier_db;

CREATE TABLE MATCH_INFO
(
	match_id int primary key,
    match_date char(8),
    home_club_id int,
    away_club_id int,
    foreign key (home_club_id) references CLUB_INFO(club_id),
    foreign key (away_club_id) references CLUB_INFO(club_id)
);

UPDATE test.MATCH_INFO
SET match_date = null
WHERE match_date = "";

-- select * from test.MATCH_INFO where match_date is NULL limit 10;