class Director(object):
    def __init__(self, name, country, age, countFilms):
        self.name = name
        self.country = country
        self.age = age
        self.countFilms = countFilms

    def __str__(self):
        return "id: %d / name: %s / country: %s / age: %d / countFilms: %d" % (self.d_id, self.name, self.country, self.age, self.countFilms)


