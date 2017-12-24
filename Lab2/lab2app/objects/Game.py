class Game:
    def __init__(self, id, title, genre, age_rating, engine, description):
        self.id = id
        self.title = title
        self.genre = genre
        self.age_rating = age_rating
        self.engine = engine
        self.description = description

    def __str__(self):
        return str(self.id) + "\\" + str(self.title) + "\\" + str(self.genre) + "\\" + str(self.age_rating)\
               + "\\" + str(self.engine) + "\\" + str(self.description)
