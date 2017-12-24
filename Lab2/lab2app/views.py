from django.shortcuts import render
from database.database import *
from django.http import HttpResponseRedirect

def home(request):

    game_list = select_titles_from_games()
    dev_list = select_names_from_developers()
    pub_list = select_names_from_publishers()

    if(request.POST):
        developer = request.POST.get('developer')
        publisher = request.POST.get('publisher')
        game_id = request.POST.get('game')
        profit = request.POST.get('profit')
        date = request.POST.get('date')

        for game in game_list:
            if game_id == game: game_id = game_list.index(game) + 1
        for dev in dev_list:
            if developer == dev: developer = dev_list.index(dev) + 1
        for pub in pub_list:
            if publisher == pub: publisher = pub_list.index(pub) + 1

        insert_into_game_releases(game_id, developer, publisher, profit, date)

    releases = select_all_from_game_releases()

    return render(request, 'home.html', locals())


def delete(request, id):
    delete_release_from_table(id)
    return HttpResponseRedirect("/home/")

def update(request, id):

    game_list = select_titles_from_games()
    dev_list = select_names_from_developers()
    pub_list = select_names_from_publishers()

    release = select_release_by_id(id)

    if(request.POST):
        developer = request.POST.get('developer')
        publisher = request.POST.get('publisher')
        game_id = request.POST.get('game')
        profit = request.POST.get('profit')
        date = request.POST.get('date')


        if len(date) < 5: date = release.release_date

        for game in game_list:
            if game_id == game: game_id = game_list.index(game) + 1
        for dev in dev_list:
            if developer == dev: developer = dev_list.index(dev) + 1
        for pub in pub_list:
            if publisher == pub: publisher = pub_list.index(pub) + 1

        update_release_in_table(int(id), game_id, developer, publisher, profit, date)
        return HttpResponseRedirect("/home/")

    return render(request, 'update.html', locals())

def filter(request):

    game_list = select_titles_from_games()
    dev_list = select_names_from_developers()
    pub_list = select_names_from_publishers()

    if(request.POST):
        games = request.POST.getlist('games')
        publishers = request.POST.getlist('publishers')
        low = request.POST.get('low')
        high = request.POST.get('high')

        releases = filter_table(games, publishers, int(low), int(high))

        return render(request, 'home.html', locals())


def search_1(request):

    game_list = select_titles_from_games()
    dev_list = select_names_from_developers()
    pub_list = select_names_from_publishers()

    releases = fulltext_search_contains(request.GET.get('search1'))

    return render(request, 'home.html', locals())

def search_2(request):

    game_list = select_titles_from_games()
    dev_list = select_names_from_developers()
    pub_list = select_names_from_publishers()

    releases = fulltext_search_not_contains(request.GET.get('search2'))

    return render(request, 'home.html', locals())