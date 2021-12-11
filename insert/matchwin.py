import pymysql
import json


def mysql_insert():

    # ====insert match_win====
    with open("../json/premier_match_win.json", "r", encoding="utf8") as json_file:
        contents = json_file.read()
        json_data = json.loads(contents)

    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="premier",
        charset="utf8"
    )

    sql_insert = "insert into match_win(Match_id, Winner_club_id) values(%s,%s)"

    curs = conn.cursor()
    for i in range(len(json_data["match_win"])):
        curs.execute(sql_insert, (json_data["match_win"][i]["Match_id"],
                                  json_data["match_win"][i]["Winner_club_id"]))

    rows = curs.fetchall()

    conn.commit()

    conn.close()


mysql_insert()
