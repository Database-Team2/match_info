import pymysql
import json

with open("match_info.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    json_data = json.loads(contents)

conn = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="test",
    charset="utf8"
)

sql_insert = "insert into match_info(match_id, match_date, match_time, home_club, away_club, stadium) values(%s,%s,%s,%s,%s,%s)"

curs = conn.cursor()
for i in range(len(json_data["match_info"])):
    curs.execute(sql_insert, (json_data["match_info"][i]["match_id"],
                              json_data["match_info"][i]["match_date"],
                              json_data["match_info"][i]["match_time"],
                              json_data["match_info"][i]["home_club"],
                              json_data["match_info"][i]["away_club"],
                              json_data["match_info"][i]["stadium"]))

rows = curs.fetchall()
conn.commit()
conn.close()
