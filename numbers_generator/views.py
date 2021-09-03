from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

import random

# english_balls = list(range(1, 59))
# euro_balls_main = list(range(1, 50))
# euro_balls_bonus = list(range(1, 12))
message = "Please select the lotto game you wish to play, and the number of games."


lotto_games = {
    "UKLotto": [[59,6],[None,None]],
    "EuroLotto": [[50,6],[12,2]],
    "IrishLotto": [[46,6],[None,None]],
    "USLotto": [[70,5],[25,1]]
}

def create_lotto_pot(game, numbers):

    pots = []
    main = []
    bonus = []
    main_pot = list(range(1,lotto_games[game][0][0]))
    if lotto_games[game][1][0] is not None:
        bonus_pot = list(range(1,lotto_games[game][1][0]))
    else:
         bonus_pot = [None, None]

    quantity_main = lotto_games[game][0][1]
    # pots.append([main_pot, quantity_main])
    quantity_bonus = lotto_games[game][1][1]
    # pots.append([bonus_pot, quantity_bonus])
    # picks_line

    for num in list(range(numbers)):

        main_line = draw_balls_main(main_pot,quantity_main)
        main.append(main_line)

        bonus_line = draw_balls_bonus(bonus_pot, quantity_bonus)
        bonus.append(bonus_line)

    pots.append(main)
    pots.append(bonus)
    return pots



def draw_balls_main(current_pot, quantity):

    # picks = []
    return sorted(random.sample(current_pot, quantity))
    # return sorted(random.sample(current_pot[0][0], current_pot[0][1]))
    # bonus_picks = sorted(random.sample(current_pot[1][0], current_pot[1][1]))

    # picks.append(main_picks)
    # picks.append(bonus_picks)
    # return picks

def draw_balls_bonus(current_pot, quantity):

    # picks = []
    # main_picks = sorted(random.sample(current_pot[0][0], current_pot[0][1]))
    # print(current_pot)
    if None in current_pot:
        return current_pot
    else:
        return sorted(random.sample(current_pot, quantity))

    # return sorted(random.sample(current_pot[1][0], current_pot[1][1]))

    # picks.append(main_picks)
    # picks.append(bonus_picks)
    # return picks




def index(request):

    return render(request, "lotto.html")

# def dropdown(request):
#     # print(request.POST)
#     # x = request.POST.get('numberOfGames')
#     # print(x)
#     # if request.method == "POST":
#     #     # request.POST.get('value')
#     #     print("WORKING!>>>???")
#     #     x = request.POST.get('numbers')
#     #     print(request.path)
#     #     print(request.method)
#     #     print(request.scheme)
#     #     print(request.GET)
#     #     print(request.user)
#
#     return render(request, "test.html")


def clicked(request):

    # x = request.POST.get('form')
    # print(x)
    if request.method == "POST":
        # request.POST.get('value')
        # print("WORKING!>>>???")
        number_of_games = request.POST.get('numberOfGames')
        print(number_of_games)
        number_of_games = int(number_of_games)
        type_of_game = request.POST.get('typeOfGame')

    balls = create_lotto_pot(type_of_game, number_of_games)
    print(balls[1][0])
    if None in balls[1][0]:
        bonus_balls = ""
    else:
        bonus_balls = balls[1]
    main_balls = balls[0]

    context = {
        # 'euro_balls_main' : euro_balls_main,
        'message' : message,
        'main_balls' : main_balls,
        'bonus_balls' : bonus_balls,
        'type_of_game': type_of_game
    }
    return render(request, 'balls_output.html', context)

