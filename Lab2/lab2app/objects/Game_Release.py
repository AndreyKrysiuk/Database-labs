import datetime

class Game_Release:
    def __init__(self, id, gid, did, pid, release_date, profit):
        self.id = id
        self.gid = gid
        self.did = did
        self.pid = pid
        self.release_date = release_date
        self.profit = profit

    def __str__(self):
        return str(self.gid) + "\\" + str(self.title) + "\\" + str(self.genre) + "\\" + str(self.age_rating)\
               + "\\" + str(self.engine) + "\\" + str(self.description)
