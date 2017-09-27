from Database import Database
from Menu import Menu

db = Database()
menu = Menu()

while True:
    command = raw_input("Enter your command: ")

    if command == "exit":
        break

    if command == "help":
        menu.help()
        continue

    if command == "showDirectors":
        db.show_directors()
        continue

    if command == "showFilms":
        db.show_films()
        continue

    if command == "addDirector":
        menu.addDirector(db)
        continue

    if command == "addFilm":
        menu.addFilm(db)
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
        menu.updateFilm(db)
        continue

    if command == "updateDirector":
        menu.updateDirector(db)
        continue

    if command == "filter":
        db.find_ukr_films()
        continue

    if command == "write":
        db.write_to_file();
        continue

    print "There is no such command. Use 'help' to get more information"
