from django.shortcuts import render

import random

"""stores the number of balls in pot, and number of balls drawn, for both main and bonus balls"""
lotto_games = {
    "UKLotto": [[59, 6], [None, None]],
    "EuroLotto": [[50, 5], [12, 2]],
    "IrishLotto": [[46, 6], [None, None]],
    "USLotto": [[70, 5], [25, 1]],
    "PowerBall": [[69, 5], [26, 1]]
}


def create_lotto_pot(game, numbers):

    pots = []
    main = []
    bonus = []

    main_pot = list(range(1, lotto_games[game][0][0]))

    if lotto_games[game][1][0] is not None:
        bonus_pot = list(range(1, lotto_games[game][1][0]))
    else:
        bonus_pot = [None, None]

    balls_drawn_main = lotto_games[game][0][1]
    balls_drawn_bonus = lotto_games[game][1][1]

    for num in list(range(numbers)):

        main_line = draw_balls_main(main_pot, balls_drawn_main)
        main.append(main_line)

        bonus_line = draw_balls_bonus(bonus_pot, balls_drawn_bonus)
        bonus.append(bonus_line)

    pots.append(main)
    pots.append(bonus)
    return pots


def draw_balls_main(current_pot, quantity):
    """ returns a sorted list of randomly picked lotto numbers """

    return sorted(random.sample(current_pot, quantity))


def draw_balls_bonus(current_pot, quantity):
    """ returns sorted list of randomly picked lotto numbers. Returns original list [None,None]if game has no bonus balls"""

    if None in current_pot:
        return current_pot
    else:
        return sorted(random.sample(current_pot, quantity))


def index(request):

    return render(request, "lotto.html")


def clicked(request):

    if request.method == "POST":

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
        'main_balls': main_balls,
        'bonus_balls': bonus_balls,
        'type_of_game': type_of_game
    }
    print(context)
    return render(request, 'balls_output.html', context)
