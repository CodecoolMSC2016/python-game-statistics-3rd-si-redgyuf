import math


def get_most_played(file_name):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    max_num_of_sold = 0
    for i in range(0, len(list_of_games)):
        if float(list_of_games[i][1]) > max_num_of_sold:
            max_num_of_sold = float(list_of_games[i][1])

    for i in range(0, len(list_of_games)):
        if float(list_of_games[i][1]) == max_num_of_sold:
            return list_of_games[i][0]


def sum_sold(file_name):
    list_of_games = []
    total_sold = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_sold += float(list_of_games[i][1])

    return total_sold


def get_selling_avg(file_name):
    list_of_games = []
    total_sold = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_sold += float(list_of_games[i][1])

    return total_sold / len(list_of_games)


def count_longest_title(file_name):
    list_of_games = []
    length_of_longest_title = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        if len(list_of_games[i][0]) > length_of_longest_title:
            length_of_longest_title = len(list_of_games[i][0])

    return length_of_longest_title


def get_date_avg(file_name):
    list_of_games = []
    total_year = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_year += float(list_of_games[i][2])

    return math.ceil(total_year / len(list_of_games))


def get_game(file_name, title):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        if title == list_of_games[i][0]:
            list_of_games[i][1:3] = map(float, list_of_games[i][1:3])
            return list_of_games[i]

# Bonus


def count_grouped_by_genre(file_name):
    list_of_games = []
    dict_of_genres = {}

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for game in list_of_games:
        if game[3] not in dict_of_genres:
            dict_of_genres[game[3]] = 1
        else:
            dict_of_genres[game[3]] += 1

    return dict_of_genres


def get_date_ordered(file_name):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    sorted_list = sorted(list_of_games, key=lambda game: game[0])
    sorted_list = sorted(sorted_list, key=lambda game: game[2], reverse=True)

    sorted_names = []
    for game in sorted_list:
        sorted_names.append(game[0])

    return sorted_names
