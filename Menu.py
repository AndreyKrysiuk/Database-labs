from Director import Director
from Film import Film

class Menu:
    def help(self):
        print "addDirector  -  add new director to database"
        print "addFilm - add new film to database"
        print "showDirectors - show all directors from database"
        print "showFilms - show all films from database"
        print "deleteDirector - delete director by id"
        print "deleteFilm - delete film by id"
        print "updateDirector - update director by id"
        print "updateFilm - update director by id"
        print "getFilm - get film by id"
        print "getDirector - get director by id"
        print "filter - filter directors, which films created in Ukraine"
        print "write - write database to file"

    def addDirector(self, db):
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        age = eval(raw_input("  Enter age: "))
        countFilms = eval(raw_input("  Enter count of films: "))
        db.add_director(Director(name, country, age, countFilms))

    def addFilm(self, db):
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        dir_id = eval(raw_input("  Enter directors id: "))
        duration = eval(raw_input("  Enter duration: "))
        db.add_film(Film(dir_id, name, country, duration))

    def updateFilm(self, db):
        id = eval(raw_input("  Enter id: "))
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        dir_id = eval(raw_input("  Enter directors id: "))
        duration = eval(raw_input("  Enter duration: "))
        db.update_film(id, dir_id, name, country, duration)

    def updateDirector(self, db):
        id = eval(raw_input("  Enter id: "))
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        age = eval(raw_input("  Enter age: "))
        countFilms = eval(raw_input("  Enter count of films: "))
        db.update_director(Director(id, name, country, age, countFilms))