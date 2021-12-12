-- create schema premier;

-- use premier;

-- CREATE TABLE STADIUM
-- (
--    stadium_id INT UNSIGNED PRIMARY KEY,
--    stadium_name VARCHAR(45),
--    capacity VARCHAR(45)
-- );

-- CREATE TABLE CLUB_INFO
-- (
--    club_id INT UNSIGNED PRIMARY KEY,
--    club_name VARCHAR(30),
--    stadium INT UNSIGNED NOT NULL,
--    badge_images_url VARCHAR(100),
--    club_url VARCHAR(100),
--    FOREIGN KEY(Stadium) REFERENCES STADIUM(Stadium_id) ON DELETE CASCADE
-- );

-- CREATE TABLE PLAYER
-- (
--    player_id INT UNSIGNED PRIMARY KEY,
--    club_id INT UNSIGNED NOT NULL,
--    player_name VARCHAR(45),
--    uniform_num INT,
--    date_of_birth CHAR(10),
--    position VARCHAR(45),
--    FOREIGN KEY(club_id) REFERENCES CLUB_INFO(club_id) ON DELETE CASCADE
-- );

-- CREATE TABLE MATCH_INFO
-- (
--    match_id INT UNSIGNED primary key,
--     match_date char(10),
--     home_club_id INT UNSIGNED,
--     away_club_id INT UNSIGNED,
--     foreign key (home_club_id) references CLUB_INFO(Club_id) ON DELETE CASCADE,
--     foreign key (away_club_id) references CLUB_INFO(Club_id) ON DELETE CASCADE
-- );

-- -- craete 이후에 해야 함!
-- UPDATE MATCH_INFO
-- SET match_date = null
-- WHERE match_date = "";

-- CREATE TABLE MATCH_DETAILS
-- (
--     match_id int unsigned not null,
--     home_score int unsigned not null,
--     away_score int unsigned not null,
--     home_possesion float unsigned not null,
--     away_possesion float unsigned not null,
--     home_shots_on_target int unsigned not null,
--     away_shots_on_target int unsigned not null,
--     home_shots int unsigned not null,
--     away_shots int unsigned not null,
--     King_of_the_match int unsigned not null,
--     foreign key(match_id) references MATCH_INFO(match_id) ON DELETE CASCADE,
--     foreign key(King_of_the_match) references PLAYER(player_id) ON DELETE CASCADE
-- );

-- CREATE TABLE MATCH_WIN
-- (
--    match_id INT UNSIGNED NOT NULL,
--    winner_club_id INT UNSIGNED,
--    foreign key(match_id) references MATCH_INFO(match_id) ON DELETE CASCADE,
--     foreign key(winner_club_id) references CLUB_INFO(club_id) ON DELETE CASCADE
-- );

-- CREATE TABLE CLUB_RESULT
-- (
--    club_id INT UNSIGNED PRIMARY KEY,
--    position INT UNSIGNED,
--    played INT UNSIGNED,
--    won INT UNSIGNED,
--    draw INT UNSIGNED,
--    lost INT UNSIGNED,
--    gf INT UNSIGNED,
--    ga INT UNSIGNED,
--    form VARCHAR(5),
--    FOREIGN KEY(Club_id) REFERENCES CLUB_INFO(Club_id) ON DELETE CASCADE
-- );

-- CREATE TABLE GOAL_OF
-- (
--    match_id INT UNSIGNED NOT NULL, -- USING UNSIGNED INT, SET FOREIGN KEY
--     club_id INT UNSIGNED NOT NULL, -- USING UNSIGNED TINT, SET FOREIGN KEY
--     player_id INT UNSIGNED NOT NULL, -- USING UNSIGNED INT
--     goal_id INT UNSIGNED PRIMARY KEY, -- USING UNSIGNED INT, SET PK
--     goal_time CHAR(10), -- USING UNSIGNED CHAR
--     FOREIGN KEY(match_id) REFERENCES MATCH_INFO(Match_id) ON DELETE CASCADE, -- USING MATCH_INFO.match_id FOR FOREIGN KEY
--     FOREIGN KEY(player_id) REFERENCES PLAYER(player_id) ON DELETE CASCADE, -- USING PLAYER.player_id FOR FOREIGN KEY
--     FOREIGN KEY(club_id) REFERENCES CLUB_INFO(club_id) ON DELETE CASCADE -- USING CLUB_INFO.club_id FOR FOREIGN KEY
-- );

-- CREATE TABLE FOUL_OF
-- (
--    match_id INT UNSIGNED NOT NULL, -- USING UNSIGNED INT, SET FOREIGN KEY
--     club_id INT UNSIGNED NOT NULL, -- USING UNSIGNED INT, SET FOREIGN KEY
--     player_id INT UNSIGNED NOT NULL, -- USING UNSIGNED INT
--     foul_time CHAR(10) NOT NULL, -- USING UNSIGNED CHAR
--     sent_off BOOLEAN NOT NULL, -- USING BOOLEAN
--     FOREIGN KEY(match_id) REFERENCES MATCH_INFO(Match_id) ON DELETE CASCADE, -- USING MATCH_INFO.match_id FOR FOREIGN KEY
--     FOREIGN KEY(player_id) REFERENCES PLAYER(player_id) ON DELETE CASCADE, -- USING PLAYER.player_id FOR FOREIGN KEY
--     FOREIGN KEY(club_id) REFERENCES CLUB_INFO(club_id) ON DELETE CASCADE -- USING CLUB_INFO.club_id FOR FOREIGN KEY
-- );

-- CREATE TABLE MATCH_LINEUPS
-- (
--     match_id int unsigned not null,
--     player_id int unsigned not null,
--     club_id int unsigned not null,
--     foreign key(match_id) references MATCH_INFO(match_id) ON DELETE CASCADE,
--     foreign key(player_id) references PLAYER(player_id) ON DELETE CASCADE,
--     foreign key(club_id) references CLUB_INFO(club_id) ON DELETE CASCADE
-- );

-- CREATE TABLE MATCH_SUB
-- (
--    match_id int unsigned not null,
--     player_id int unsigned not null,
--     club_id int unsigned not null,
--     foreign key(match_id) references MATCH_INFO(match_id) ON DELETE CASCADE,
--     foreign key(club_id) references CLUB_INFO(club_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IN_OUT
-- (
--     match_id int unsigned not null,
--     in_out varchar(20) not null,
--     in_out_time char(10) not null,
--     player_id int unsigned not null,
--     club_id int unsigned not null,
--     foreign key(match_id) references MATCH_INFO(match_id) ON DELETE CASCADE,
--     foreign key(club_id) references CLUB_INFO(club_id) ON DELETE CASCADE
-- );