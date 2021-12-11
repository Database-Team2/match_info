#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pymysql
import json

with open("../json/clubs_info.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    stadi = json.loads(contents)

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="test",
    charset="utf8"
)

with open("../json/Stadium.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    json_data = json.loads(contents)

with conn:
    with conn.cursor() as curs:
        sql = "insert into stadium(Stadium_id, Stadium_name, Capacity) values(%s,%s,%s)"
        for i in range(len(json_data['Stadium_info'])):
            curs.execute(sql, (json_data['Stadium_info'][i]["Stadium_id"], json_data['Stadium_info'][i]["Stadium_name"],
                               json_data['Stadium_info'][i]["Capacity"]))

    conn.commit()


with conn:
    with conn.cursor() as curs:
        sql = "insert into club_info(Club_id, Club_name, Stadium, Club_url, Club_badge_image) values(%s,%s,%s,%s,%s)"
        for i in range(len(stadi['clubs_info'])):
            curs.execute(sql, (stadi['clubs_info'][i]["club_id"], stadi['clubs_info'][i]["club_name"],
                               stadi['clubs_info'][i]["stadium_id"], stadi['clubs_info'][i]["club_url"],
                               stadi['clubs_info'][i]["badge_images_url"]))
    # conn.close()
    # rows=cur.fetchall()
    conn.commit()

with open("clubs_results.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    club = json.loads(contents)


with conn:
    with conn.cursor() as curs:
        sql = "insert into club_result(Club_id, position, played, Won, Drawn, lost, ga, gf, Form) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for i in range(len(club['clubs_detail'])):
            curs.execute(sql, (
            club['clubs_detail'][i]["club_id"], club['clubs_detail'][i]["position"], club['clubs_detail'][i]["played"],
            club['clubs_detail'][i]["won"], club['clubs_detail'][i]["drawn"], club['clubs_detail'][i]["lost"],
            club['clubs_detail'][i]["ga"], club['clubs_detail'][i]["gf"], club['clubs_detail'][i]["form"]))
    # conn.close()
    # rows=cur.fetchall()
    conn.commit()

with open("player_fix3.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    player = json.loads(contents)


with conn:
    with conn.cursor() as curs:
        sql = "insert into player(Player_id, Club_id, Player_name, Uniform_num, Date_of_birth, position) values(%s,%s,%s,%s,%s,%s)"
        for i in range(len(player)):
            curs.execute(sql, (
            player[i]["Player_id"], player[i]["Club_id"], player[i]["Player_name"], player[i]["Uniform_num"],
            player[i]["Date_of_birth"], player[i]["position"]))
    # conn.close()
    # rows=cur.fetchall()
    conn.commit()

