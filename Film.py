class Film(object):
    def __init__(self, dir_id, name, country, duration):
        self.dir_id = dir_id
        self.name = name
        self.country = country
        self.duration = duration

    def __str__(self):
        return "id: %d / name: %s / director: %d / country: %s / duration: %d" % (self.film_id, self.name, self.dir_id, self.country, self.duration)

