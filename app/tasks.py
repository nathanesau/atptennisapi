# background tasks
import os
import psycopg2
import time
from atpparser import downloadArchive, downloadDraw, \
    parseArchive, parseDraw

"""
def is_tournament_in_db(conn, tournament_name):
    cursor = conn.cursor()
    cursor.execute("select * from atptennisschema.tournament where name like '{}'".format(
        tournament_name)
    )
    records = cursor.fetchall()
    cursor.close()
    return True if records else False

def read_tournament_table(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * from atptennisschema.tournament")
    records = cursor.fetchall()

    if not records:
        return {}

    tournaments = {}
    for row in records:
        id, name, start_date, end_date = row
        tournaments[name] = {"id": id, "name": name, "start_date": start_date, "end_date": end_date}

    cursor.close()
    return tournaments

def read_player_table(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT * from atptennisschema.player")
    records = cursor.fetchall()

    if not records:
        return {}

    players = {}
    for row in records:
        id, name, country_code = row
        players[name] = {"id": id, "name": name, "country_code": country_code}

    cursor.close()
    return players

def write_draw_to_db(conn, draw_data, tournament_info):
    cursor = conn.cursor()

    tournaments = read_tournament_table(conn)
    players = read_player_table(conn)
    tournament_name = tournament_info["name"] + str(tournament_info["year"])

    if tournament_name in tournaments:
        # nothing to do, we have already written this draw to DB
        return

    # update tournament table 
    cmd = "insert into atptennisschema.tournament(name, start_date, end_date) " + \
        "VALUES('{name}', to_date('{start_date}', 'YYYY.MM.DD'), to_date('{end_date}', 'YYYY.MM.DD')) returning id;".format(
        name=tournament_name, start_date=draw_data["dates"]["start"], end_date=draw_data["dates"]["end"])
    cursor.execute(cmd)
    tournament_id = cursor.fetchone()[0]
    conn.commit()

    # update player table
    for player in draw_data["players"]:
        name = player["name"]
        if name not in players:
            cmd = "insert into atptennisschema.player(name, country_code) " + \
                "VALUES('{name}', '{country_code}') returning id;".format(name=player["name"], country_code=player["countryCode"])
            cursor.execute(cmd)
            player_id = cursor.fetchone()[0]
            players[name] = {"id": player_id, "name": name, "country_code": player["countryCode"]}
    conn.commit()

    # update entrants table
    for player in draw_data["players"]:
        name = player["name"]
        player_result = player["result"]
        player_seed = player["seed"]
        player_id = players[name]["id"]
        cmd = "insert into atptennisschema.entrants(tournament_id, player_id, player_seed, player_result) " + \
                "VALUES({tournament_id}, {player_id}, '{player_seed}', {player_result});".format(
                tournament_id=tournament_id, player_id=player_id, player_seed=player_seed, player_result=player_result)
        cursor.execute(cmd)
    conn.commit()

    # update matchups table
    for matchup in draw_data["matchups"]:
        player1_name = matchup["player1"]
        player2_name = matchup["player2"]
        winner_name = matchup["winner"]

        if not (player1_name and player2_name): # exclude matchup if player name missing
            continue

        if not winner_name: # match was never completed
            continue 

        if player1_name == "unknown" or player2_name == "unknown": # bracket was never completed
            continue

        player1_id = players[player1_name]["id"]
        player2_id = players[player2_name]["id"]
        round_num = matchup["round"]
        winner_name = matchup["winner"]
        winner_id = players[winner_name]["id"]
        cmd = "insert into atptennisschema.matchups(tournament_id, player1_id, player2_id, round_num, winner_id) " + \
                "VALUES({tournament_id}, {player1_id}, {player2_id}, {round_num}, {winner_id});".format(
                tournament_id=tournament_id, player1_id=player1_id, player2_id=player2_id, round_num=round_num, winner_id=winner_id)
        cursor.execute(cmd)
    conn.commit()

    cursor.close()

def update_db():
    dbUrl = os.environ['DATABASE_URL']
    conn = psycopg2.connect(os.environ['DATABASE_URL'])

    for draw_year in [2014, 2015, 2016, 2017, 2018, 2019]:
        archive_file = downloadArchive(draw_year)
        archive_data = parseArchive(archive_file)

        for draw in archive_data:
            draw_title = draw["title"]
            draw_link = draw["link"]
            tournament_name = draw_title + str(draw_year)

            if is_tournament_in_db(conn, tournament_name):
                continue

            print("Downloading draw {} ({})...".format(draw_title, draw_year))
            draw_file = downloadDraw(draw_title, draw_link, draw_year)
            draw_data = parseDraw(draw_file)
            tournament_info = {"name": draw_title, "year": draw_year}

            if draw_data:
                print("Writing draw {} ({}) to db...".format(draw_title, draw_year))
                write_draw_to_db(conn, draw_data, tournament_info)
            else:
                print("Unable to parse draw {} ({})...".format(draw_title, draw_year))
"""

def threaded_task(wait):
    while True:
        print("Running ATP Parser")
        #update_db()
        time.sleep(wait)