import mysql.connector as connector
from lab2app.csv import csv_parse
from lab2app.objects.Game_Release import Game_Release

add_game = ("INSERT INTO lab.games (id, title, genre, age_rating, engine, description) "
               "VALUES (%d, '%s', '%s', %d, '%s', '%s');")

add_developer = ("INSERT INTO lab.developers (id, name, year, headquarter, count_employees) "
               "VALUES (%d, '%s', %d, '%s', %d);")

add_publisher = ("INSERT INTO lab.publishers (id, name, year, headquarter) "
               "VALUES (%d, '%s', %d, '%s');")


def init_games(games):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()
    cursor.execute("delete from lab.games;")
    for game in games:
        game_request = add_game % (game.id, game.title, game.genre, game.age_rating, game.engine, game.description)
        cursor.execute(game_request)

    cnx.commit()
    cursor.close()
    cnx.close()


def init_developers(developers):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()
    cursor.execute("delete from lab.developers;")
    for developer in developers:
        developer_request = add_developer % (developer.id, developer.name, developer.year, developer.headquarter, developer.count_employees)
        cursor.execute(developer_request)

    cnx.commit()
    cursor.close()
    cnx.close()


def init_publishers(publishers):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()
    cursor.execute("delete from lab.publishers;")

    for publisher in publishers:
        publisher_request = add_publisher % (publisher.id, publisher.name, publisher.year, publisher.headquarter)
        cursor.execute(publisher_request)

    cnx.commit()
    cursor.close()
    cnx.close()


def init_side_tables():
    games = csv_parse.parse_games()
    developers = csv_parse.parse_developers()
    publisher = csv_parse.parse_publishers()

    init_games(games)
    init_developers(developers)
    init_publishers(publisher)


def select_titles_from_games():
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("SELECT id, title FROM lab.games ")

    cursor.execute(query)

    games = []
    for (id, title) in cursor:
        games.append(title)

    cursor.close()
    cnx.close()
    return games


def select_names_from_developers():
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("SELECT id, name FROM lab.developers ")

    cursor.execute(query)

    developers = []
    for (id, name) in cursor:
        developers.append(name)

    cursor.close()
    cnx.close()
    return developers


def select_names_from_publishers():
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("SELECT id, name FROM lab.publishers ")

    cursor.execute(query)

    publishers = []
    for (id, name) in cursor:
        publishers.append(name)

    cursor.close()
    cnx.close()
    return publishers


def select_all_from_game_releases():
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("SELECT game_releases.id, games.title, developers.name, publishers.name, date, profit from game_releases "
                "JOIN games ON game_id = games.id "
                "JOIN developers ON dev_id = developers.id "
                "JOIN publishers ON pub_id = publishers.id;")

    cursor.execute(query)

    game_releases = []
    for (id, game_id, dev_id, pub_id, release_date, profit) in cursor:
        game_releases.append(Game_Release(id, game_id, dev_id, pub_id, release_date, profit))

    cursor.close()
    cnx.close()
    return game_releases

def insert_into_game_releases(game_id, dev_id, pub_id, profit, date):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("INSERT INTO lab.game_releases (game_id, dev_id, pub_id, date, profit)"
               "VALUES (%d, %d, %d, '%s', %f);") % (game_id, dev_id, pub_id, date, float(profit))

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_release_from_table(id):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("DELETE FROM game_releases WHERE id = %d") % (int(id))

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def select_release_by_id(id):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("SELECT game_releases.id, games.title, developers.name, publishers.name, date, profit from game_releases "
                "JOIN games ON game_id = games.id "
                "JOIN developers ON dev_id = developers.id "
                "JOIN publishers ON pub_id = publishers.id "
                "WHERE game_releases.id = %d") % (int(id))

    cursor.execute(query)

    for (id, game_id, dev_id, pub_id, release_date, profit) in cursor:
        game_release = (Game_Release(id, game_id, dev_id, pub_id, release_date, profit))

    cursor.close()
    cnx.close()
    return game_release


def update_release_in_table(id, gid, did, pid, profit, date):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    query = ("UPDATE game_releases "
                "SET game_id = %d, dev_id = %d, pub_id = %d, date = '%s', profit = %f WHERE id = %d;") \
            % (gid, did, pid, date, float(profit), id)

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def filter_table(games, publishers, high, low):
    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    if(high < low):
        tmp = low
        low = high
        high = tmp

    query = ("SELECT game_releases.id, games.title, developers.name, publishers.name, date, profit from game_releases "
                "JOIN games ON game_id = games.id "
                "JOIN developers ON dev_id = developers.id "
                "JOIN publishers ON pub_id = publishers.id "
                "WHERE (developers.count_employees BETWEEN %d AND %d) ")

    if(len(games) != 0):
        query += "AND games.title IN ("
        for game in games:
            query += "'" + game + "'"
            if games.index(game) < len(games) - 1:
                query += ','
        query += ")"


    if(len(publishers) != 0):
        query += "AND publishers.name IN ("
        for publisher in publishers:
            query += "'" + publisher + "'"
            if publishers.index(publisher) < len(publishers) - 1:
                query += ', '
        query += ")"

    query = query % (low, high)
    cursor.execute(query)

    game_releases = []
    for (id, game_id, dev_id, pub_id, release_date, profit) in cursor:
        game_releases.append(Game_Release(id, game_id, dev_id, pub_id, release_date, profit))
    cursor.close()
    cnx.close()

    return game_releases


def fulltext_search_contains(word):

    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    words = word.split()
    result_words = ""
    for word in words:
        result_words += "+" + word + " "

    query = ("SELECT game_releases.id, games.title, developers.name, publishers.name, date, profit from game_releases "
                "JOIN games ON game_id = games.id "
                "JOIN developers ON dev_id = developers.id "
                "JOIN publishers ON pub_id = publishers.id "
                "WHERE MATCH(games.description)"
                "AGAINST ('%s' IN BOOLEAN MODE);") % (result_words)

    print query

    cursor.execute(query)

    game_releases = []
    for (id, game_id, dev_id, pub_id, release_date, profit) in cursor:
        game_releases.append(Game_Release(id, game_id, dev_id, pub_id, release_date, profit))

    cursor.close()
    cnx.close()
    return game_releases

def fulltext_search_not_contains(word):

    cnx = connector.connect(user='root', password='1111', database='lab')
    cursor = cnx.cursor()

    words = word.split()
    result_words = ""
    for word in words:
        result_words += "+" + word + " "



    query = ("SELECT game_releases.id, games.title, developers.name, publishers.name, date, profit from game_releases "
                "JOIN games ON game_id = games.id "
                "JOIN developers ON dev_id = developers.id "
                "JOIN publishers ON pub_id = publishers.id "
                "WHERE NOT MATCH(games.description)"
                "AGAINST ('%s' IN BOOLEAN MODE);") % (result_words)

    cursor.execute(query)

    game_releases = []
    for (id, game_id, dev_id, pub_id, release_date, profit) in cursor:
        game_releases.append(Game_Release(id, game_id, dev_id, pub_id, release_date, profit))

    cursor.close()
    cnx.close()
    return game_releases

