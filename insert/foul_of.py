import pymysql
import json
def insertsql_from_json():

    #connect
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="premier",
        charset="utf8"
    )
    curs = conn.cursor()

    with open("../json/foul_of.json","r",encoding="utf8") as json_file:
        contents = json_file.read()
        json_data = json.loads(contents)

    sql="insert into foul_of(match_id, club_id, player_id,foul_time, sent_off) values(%s,%s,%s,%s,%s)"


    for i in range(len(json_data["foul_of"])):
        curs.execute(sql,(json_data["foul_of"][i]["match_id"],
                        json_data["foul_of"][i]["club_id"],
                        json_data["foul_of"][i]["player_id"],
                        json_data["foul_of"][i]["foul_time"],
                        json_data["foul_of"][i]["sent_off"]
                        )
                    )
    rows=curs.fetchall()
    conn.commit()
    conn.close()

insertsql_from_json()
# Reference by https://thalals.tistory.com/37