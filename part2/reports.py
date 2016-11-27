import math


# What is the title of the most played game?
# Expected output of the function: (string)
# Other expectation:  if there is more than one, then return the first
# from the file
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


# How many copies have been sold total?
# Expected output of the function: (number)
def sum_sold(file_name):
    list_of_games = []
    total_sold = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_sold += float(list_of_games[i][1])

    return total_sold


# What is the average selling?
# Expected output of the function: (number)
# Other expectation: if there is more than one, then return the first from
# the file
def get_selling_avg(file_name):
    list_of_games = []
    total_sold = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_sold += float(list_of_games[i][1])

    return total_sold / len(list_of_games)


# How many characters long is the longest title?
# Expected output of the function: (number)
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


# What is the average of the release dates?
# Expected output of the function: average year (number)
# Other expectation: the return value must be the rounded up average
def get_date_avg(file_name):
    list_of_games = []
    total_year = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        total_year += float(list_of_games[i][2])

    return math.ceil(total_year / len(list_of_games))


# What properties has a game?
# Expected output of the function: a list of all the properties of the
# game (a list of various type)
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
# How many games are there grouped by genre?
# Expected output of the function: a dictionary with this structure: {
# [genre] : [count] }
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


# What is the date ordered list of the games?
# Expected output of the function: the date ordered list of the titles (list of string)
# The secondary ordering rule is the alphabetical ordering of the titles.
# So if there are titles from the same year, you need to order them
# alphabetically in ascending order.
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
