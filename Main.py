from Database import Database
from Director import Director
from Film import Film


db = Database()

while True:
    command = raw_input("Enter your command: ")

    if command == "exit":
        break

    if command == "help":
        print "addDirector  -  add new director to database"
        print "addFilm - add new film to database"
        print "showDirectors - show all directors from database"
        print "showFilms - show all films from database"
        print "deleteDirector - delete director by id"
        print "deleteFilm - delete film by id"
        print "updateDirector - update director by id"
        print "updateFilm - update director by id"
        print "filter - filter directors, which films created in Ukraine"
        print "write - write database to file"
        continue

    if command == "showDirectors":
        db.show_directors()
        continue

    if command == "showFilms":
        db.show_films()
        continue

    if command == "addDirector":
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        age = eval(raw_input("  Enter age: "))
        countFilms = eval(raw_input("  Enter count of films: "))
        db.add_director(Director(name, country, age, countFilms))
        continue

    if command == "addFilm":
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        dir_id = eval(raw_input("  Enter directors id: "))
        duration = eval(raw_input("  Enter duration: "))
        db.add_film(Film(dir_id, name, country, duration))
        continue

    if command == "deleteDirector":
        id = eval(raw_input("  Enter id: "))
        db.delete_director(id)
        continue

    if command == "deleteFilm":
        id = eval(raw_input("  Enter id: "))
        db.delete_film(id)
        continue

    if command == "getFilm":
        id = eval(raw_input("  Enter id: "))
        print db.find_film(id)
        continue

    if command == "getDirector":
        id = eval(raw_input("  Enter id: "))
        print db.find_director(id)
        continue

    if command == "updateFilm":
        id = eval(raw_input("  Enter id: "))
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        dir_id = eval(raw_input("  Enter directors id: "))
        duration = eval(raw_input("  Enter duration: "))
        db.update_film(id, dir_id, name, country, duration)
        continue

    if command == "updateDirector":
        id = eval(raw_input("  Enter id: "))
        name = raw_input("  Enter name: ")
        country = raw_input("  Enter country: ")
        age = eval(raw_input("  Enter age: "))
        countFilms = eval(raw_input("  Enter count of films: "))
        db.update_director(Director(id, name, country, age, countFilms))
        continue

    if command == "filter":
        db.find_ukr_films()
        continue

    if command == "write":
        db.write_to_file();
        continue

    print "There is no such command. Use 'help' to get more information"
