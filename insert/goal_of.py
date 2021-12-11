import pymysql
import json
def insertsql_from_json():

    #connect
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="test",
        charset="utf8"
    )
    curs = conn.cursor()


    with open("../json/goal_of.json","r",encoding="utf8") as json_file:
        contents = json_file.read()
        json_data = json.loads(contents)

    sql="insert into goal_of(match_id, club_id, player_id,goal_id,goal_time) values(%s,%s,%s,%s,%s)"


    for i in range(len(json_data["goal_of"])):
        curs.execute(sql,(json_data["goal_of"][i]["match_id"],
                        json_data["goal_of"][i]["club_id"],
                        json_data["goal_of"][i]["player_id"],
                        json_data["goal_of"][i]["goal_id"],
                        json_data["goal_of"][i]["goal_time"]
                        )
                    )
    rows=curs.fetchall()
    conn.commit()
    conn.close()

insertsql_from_json()
# Reference by https://thalals.tistory.com/37