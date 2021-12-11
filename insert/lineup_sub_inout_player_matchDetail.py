import pymysql
import json

with open("./match_detail.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    json_data = json.loads(contents)

conn=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="jaesung4231@",
    database="epl",
    charset = "utf8"
)

sql_match_lineup = "insert into MATCH_LINEUPS(match_id, player_id) values(%s,%s)"
sql_match_sub="insert into MATCH_SUB(match_id, home_team_id,away_team_id,home_sub,away_sub) values(%s,%s,%s,%s,%s)"
sql_match_inout="insert into IN_OUT(match_id,in_out,time,player_id,club_id) values(%s,%s,%s,%s,%s)"
sql_players="insert into PLAYER(Player_id,Club_id,Player_name,Uniform_num,Date_of_birth,position) values(%s,%s,%s,%s,%s,%s)"
sql_match_details='insert into MATCH_DETAIL(match_id,home_score,away_score,home_possesion,away_possesion,home_shots_on_target,away_shots_on_target,home_shots,away_shots,King_of_the_match) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


temp=[]
curs=conn.cursor()

def insert_lineup():
    for i in range(len(json_data["match_lineup"])):
        for j in range(len(json_data["match_lineup"][i]["Home_lineups"])):
            curs.execute(sql_match_lineup ,(json_data["match_lineup"][i]["match_id"],
                        json_data["match_lineup"][i]["Home_lineups"][j]
                        ))
        for j in range(len(json_data["match_lineup"][i]["Away_lineups"])):
             curs.execute(sql_match_lineup ,(json_data["match_lineup"][i]["match_id"],
                        json_data["match_lineup"][i]["Home_lineups"][j]
                        ))

def insert_match_sub():
    for i in range(len(json_data["match_lineup"])):
        print(len(json_data["match_lineup"][i]["Home_sub"]))
        print(len(json_data["match_lineup"][i]["Away_sub"]))
        for j in range(9):
            if(len(json_data["match_lineup"][i]["Home_sub"])<9):
                json_data["match_lineup"][i]["Home_sub"].append(None)
            elif(len(json_data["match_lineup"][i]["Away_sub"])<9):
                json_data["match_lineup"][i]["Away_sub"].append(None)
            curs.execute(sql_match_sub,(json_data["match_lineup"][i]["match_id"],
                        json_data["match_lineup"][i]["Home_team"],
                        json_data["match_lineup"][i]["Away_team"],
                        json_data["match_lineup"][i]["Home_sub"][j],
                        json_data["match_lineup"][i]["Away_sub"][j],
                        ))

def insert_in_out():
    for i in range(len(json_data["players_in_out"])):
        curs.execute(sql_match_inout,(
            json_data["players_in_out"][i]["match_id"],
            json_data["players_in_out"][i]["in_out"],
            json_data["players_in_out"][i]["time"],
            json_data["players_in_out"][i]["player"],
            int(json_data["players_in_out"][i]["club_id"])
        ))



# for i in range(len(json_data["player"])):
#        curs.execute(sql_players,(
#            json_data["player"][i]["Player_id"],
#            json_data["player"][i]["Club_id"],
#            json_data["player"][i]["Player_name"],
#            json_data["player"][i]["Uniform_num"],
#            json_data["player"][i]["Date_of_birth"],
#            json_data["player"][i]["position"]
#        ))
def insert_match_detail():
    for i in range(len(json_data['match_detail'])):
            curs.execute(sql_match_details,(
            json_data["match_detail"][i]["Match_id"],
            json_data["match_detail"][i]["Home_score"],
            json_data["match_detail"][i]["Away_score"],
            json_data["match_detail"][i]["Home_possesion"],
            json_data["match_detail"][i]["Away_possesion"],
            json_data["match_detail"][i]["Home_shots_on_target"],
            json_data["match_detail"][i]["Away_shots_on_target"],
            json_data["match_detail"][i]["Home_shots"],
            json_data["match_detail"][i]["Away_shots"],
            json_data["match_detail"][i]["King_of_the_match"]
        ))



rows=curs.fetchall()
conn.commit()
conn.close()