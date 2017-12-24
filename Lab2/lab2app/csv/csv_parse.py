from lab2app.objects.Developer import Developer
from lab2app.objects.Game import Game
from lab2app.objects.Publisher import Publisher

import csv


def parse_publishers():
    with open("D:\KPI\ThirdCourse\DB\Lab2\lab2app\csv\publishers.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        publishers = []
        for line in csv_reader:
            publishers.append(Publisher(int(line[0]), line[1], int(line[2], 10), line[3]))

        return publishers


def parse_games():
    with open('D:\KPI\ThirdCourse\DB\Lab2\lab2app\csv\games.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        games = []
        for line in csv_reader:
            games.append(Game(int(line[0]), line[1], line[2], int(line[3], 10), line[4], line[5]))

        return games


def parse_developers():
    with open("D:\KPI\ThirdCourse\DB\Lab2\lab2app\csv\developers.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        developers = []
        for line in csv_reader:
            developers.append(Developer(int(line[0]), line[1], int(line[2], 10), line[3], int(line[4], 10)))

        return developers
