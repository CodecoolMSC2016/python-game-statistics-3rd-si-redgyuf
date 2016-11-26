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
    pass


def get_selling_avg(file_name):
    pass


def count_longest_title(file_name):
    pass


def get_date_avg(file_name):
    pass


def get_game(file_name, title):
    pass

# Bonus


def count_grouped_by_genre(file_name):
    pass


def get_date_ordered(file_name):
    pass
