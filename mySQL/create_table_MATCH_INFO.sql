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

-- select * from MATCH_INFO limit 10;