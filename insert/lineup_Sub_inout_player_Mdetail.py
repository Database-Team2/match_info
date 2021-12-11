import pymysql
import json

with open("./match_lineup_id.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    lineup_data = json.loads(contents)

with open("./player_in_out.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    in_out_data = json.loads(contents)

with open("./match_details.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    match_detail_data = json.loads(contents)

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="premier",
    charset="utf8"
)

sql_match_lineup = "insert into MATCH_LINEUPS(match_id,club_id ,player_id) values(%s,%s,%s)"
sql_match_sub = "insert into MATCH_SUB(match_id,club_id,player_id) values(%s,%s,%s)"
sql_match_inout = "insert into IN_OUT(match_id,in_out,time,player_id,club_id) values(%s,%s,%s,%s,%s)"
sql_players = "insert into PLAYER(Player_id,Club_id,Player_name,Uniform_num,Date_of_birth,position) values(%s,%s,%s,%s,%s,%s)"
sql_match_details = 'insert into MATCH_DETAIL(match_id,home_score,away_score,home_possesion,away_possesion,home_shots_on_target,away_shots_on_target,home_shots,away_shots,King_of_the_match) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

temp = []
curs = conn.cursor()


def insert_lineup():
    for i in range(len(lineup_data["match_lineup"])):
        for j in range(len(lineup_data["match_lineup"][i]["Home_lineups"])):
            curs.execute(sql_match_lineup, (lineup_data["match_lineup"][i]["match_id"],
                                            lineup_data["match_lineup"][i]["Home_team"],
                                            lineup_data["match_lineup"][i]["Home_lineups"][j]
                                            ))
        for j in range(len(lineup_data["match_lineup"][i]["Away_lineups"])):
            curs.execute(sql_match_lineup, (lineup_data["match_lineup"][i]["match_id"],
                                            lineup_data["match_lineup"][i]["Away_team"],
                                            lineup_data["match_lineup"][i]["Home_lineups"][j]
                                            ))


def insert_match_sub():
    for i in range(len(lineup_data["match_lineup"])):
        for j in range(len(lineup_data["match_lineup"][i]['Home_sub'])):
            curs.execute(sql_match_sub, (lineup_data["match_lineup"][i]["match_id"],
                                         lineup_data["match_lineup"][i]["Home_team"],
                                         lineup_data["match_lineup"][i]["Home_sub"][j]
                                         ))
        for j in range(len(lineup_data["match_lineup"][i]['Away_sub'])):
            curs.execute(sql_match_sub, (lineup_data["match_lineup"][i]["match_id"],
                                         lineup_data["match_lineup"][i]["Away_team"],
                                         lineup_data["match_lineup"][i]["Away_sub"][j]
                                         ))


def insert_in_out():
    for i in range(len(in_out_data["players_in_out"])):
        curs.execute(sql_match_inout, (
            in_out_data["players_in_out"][i]["match_id"],
            in_out_data["players_in_out"][i]["in_out"],
            in_out_data["players_in_out"][i]["time"],
            in_out_data["players_in_out"][i]["player"],
            int(in_out_data["players_in_out"][i]["club_id"])
        ))


def insert_match_detail():
    for i in range(len(match_detail_data['match_detail'])):
        curs.execute(sql_match_details, (
            match_detail_data["match_detail"][i]["Match_id"],
            match_detail_data["match_detail"][i]["Home_score"],
            match_detail_data["match_detail"][i]["Away_score"],
            match_detail_data["match_detail"][i]["Home_possesion"],
            match_detail_data["match_detail"][i]["Away_possesion"],
            match_detail_data["match_detail"][i]["Home_shots_on_target"],
            match_detail_data["match_detail"][i]["Away_shots_on_target"],
            match_detail_data["match_detail"][i]["Home_shots"],
            match_detail_data["match_detail"][i]["Away_shots"],
            match_detail_data["match_detail"][i]["King_of_the_match"]
        ))


insert_lineup()
insert_match_sub()
insert_in_out()
insert_match_detail()
rows = curs.fetchall()
conn.commit()
conn.close()
