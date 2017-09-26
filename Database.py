import pickle

class Database(object):

    def __init__(self):
        try:
            file = open('data.pkl', 'rb')
        except IOError as e:
            print "Can't load database from file. Create new database."
            self.directors = []
            self.films = []
        else:
            with file:
                db = pickle.load(file)
                self.directors = db.directors
                self.films = db.films
                file.close()

    def show_directors(self):
        for director in self.directors:
            print(director)

    def show_films(self):
        for film in self.films:
            print(film)

    def add_director(self, director):
        if len(filter(lambda x: x.name == director.name, self.directors)) == 0:
            director.d_id = self.max_director_id() + 1
            self.directors.append(director)
        else :
            print "Such director already exists"

    def add_film(self, film):
        if type(self.find_director(film.dir_id)) is str:
            print("Can't add film to database, such Director is not found")
            return
        if len(filter(lambda x: x.name == film.name, self.films)) == 0:
            film.film_id = self.max_film_id() + 1
            self.films.append(film)
        else:
            print "Such film already exists"

    def max_director_id(self):
        if len(self.directors) != 0:
            return max(director.d_id for director in self.directors)
        else:
            return 0

    def max_film_id(self):
        if len(self.films) != 0:
            return max(film.film_id for film in self.films)
        else:
            return 0

    def find_director(self, id):
        result = filter(lambda x: x.d_id == id, self.directors)
        if len(result) == 0:
            return "Can`t find Director with id=%s" % (id)
        else:
            return result[0]

    def find_film(self, id):
        result = filter(lambda x: x.film_id == id, self.films)
        if len(result) == 0:
            return "Can`t find Film with id=%s" % (id)
        else:
            return result[0]

    def delete_director(self, id):
        if len(self.find_films_by_director(id)) != 0:
            print "Can't delete director. Some films connected with this director"
            return

        director = self.find_director(id)
        if type(director) is not str:
            self.directors.remove(director)
        else:
            print director

    def find_films_by_director(self, d_id):
        result = filter(lambda x: x.dir_id == d_id, self.films)
        return result

    def delete_film(self, id):
        film = self.find_film(id)
        if type(film) is not str:
            self.films.remove(film)
        else:
            print film

    def update_director(self, id, name="", country="", age=-1, countFilms=-1):
        if len(self.find_films_by_director(id)) != 0:
            print "Can't update director. Some films connected with this director"
            return

        director = self.find_director(id);
        if type(director) is str:
            print director
            return
        if name != "":
            director.name = name
        if country != "":
            director.country = country
        if age > -1:
            director.age = age
        if countFilms > -1:
            director.countFilms = countFilms

    def update_film(self, id, dir_id=-1, name="", country="", duration=-1):
        film = self.find_film(id)
        if type(film) is str:
            print film
            return
        if name != "":
            film.name = name
        if country != "":
            film.country = country
        if dir_id != -1 and type(self.find_director(dir_id)) is not str:
            film.dir_id = dir_id
        else:
            print self.find_director(dir_id)
        if duration > -1:
            film.duration = duration

    def find_ukr_films(self):
        films = filter(lambda film: film.country == "Ukraine", self.films)
        directors = []

        for film in films:
            director = self.find_director(film.dir_id)
            if not directors.__contains__(director):
                directors.append(director)

        for director in directors:
            print director

    def write_to_file(self):
        output = open('data.pkl', 'wb')
        obj = self
        pickle.dump(obj, output)
        output.close()
