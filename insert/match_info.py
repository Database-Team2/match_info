import pymysql
import json

with open("../json_data/match_info.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    json_data = json.loads(contents)

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="test",
    charset="utf8"
)

sql_insert = "insert into match_info(match_id, match_date, home_club_id, away_club_id) values(%s,%s,%s,%s)"

curs = conn.cursor()
for i in range(len(json_data["match_info"])):
    curs.execute(sql_insert, (json_data["match_info"][i]["match_id"],
                              json_data["match_info"][i]["match_date"],
                              json_data["match_info"][i]["home_club_id"],
                              json_data["match_info"][i]["away_club_id"]))

rows = curs.fetchall()
conn.commit()
conn.close()