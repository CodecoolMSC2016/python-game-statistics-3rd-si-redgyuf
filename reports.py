

# How many games are in the file?
# Expected output of the function: integer
def count_games(file_name):
    counter = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            counter += 1

    return counter


# Is there a game from a given year?
# Expected output of the function: boolean value
def decide(file_name, year):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for game in list_of_games:
        if int(game[2]) == year:
            return True
    return False


# Which was the latest game?
# Other expectation: if there is more than one, then return the first from the file
# Expected output of the function: string
def get_latest(file_name):
    list_of_games = []
    name_of_latest_game = ""

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    latest_game_year = 0

    for game in list_of_games:
        if int(game[2]) > latest_game_year:
            latest_game_year = int(game[2])
            name_of_latest_game = game[0]

    return name_of_latest_game


# How many games do we have by genre?
# Expected output of the function: integer
def count_by_genre(file_name, genre):
    counter = 0
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for game in list_of_games:
        if game[3] == genre:
            counter += 1

    return counter


# What is the line number of the given game (by title)?
# Expected output of the function: integer (if there is no game found,
# then raises ValueError exception)
def get_line_number_by_title(file_name, title):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        if list_of_games[i][0] == title:
            return i + 1

    raise ValueError("Could not find it")


#  Bonus #
# What is the alphabetical ordered list of the titles?
# Expected output of the function: a list of strings
def sort_abc(file_name):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    return sorted([game[0] for game in list_of_games], key=lambda game_title: game_title.lower())


# What are the genres?
# Expected output of the function: a list of the genres (without
# duplicates, in alphabetical order)
def get_genres(file_name):
    list_of_games = []

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    return sorted(set([game[3] for game in list_of_games]),
                  key=lambda game_genre: game_genre.lower())


# What is the release date of the top sold "First-person shooter" game?
# Expected output of the function: integer (if there is no game with genre
# "First-person shooter" then raises ValueError exception
def when_was_top_sold_fps(file_name):
    list_of_games = []
    max_num_of_sold = 0

    with open(file_name, mode="r") as my_file:
        for lines in my_file:
            list_of_games.append(lines.replace('\n', "").split(sep='\t'))

    for i in range(0, len(list_of_games)):
        if list_of_games[i][3] == "First-person shooter":
            if float(list_of_games[i][1]) > max_num_of_sold:
                max_num_of_sold = float(list_of_games[i][1])

    for i in range(0, len(list_of_games)):
        if list_of_games[i][3] == "First-person shooter":
            if float(list_of_games[i][1]) == max_num_of_sold:
                return int(list_of_games[i][2])

    raise ValueError("There is no game with genre First-person shooter")
