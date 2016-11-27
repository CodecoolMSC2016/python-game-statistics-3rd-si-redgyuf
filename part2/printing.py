from reports import *


def main():
    print("What is the title of the most played game?")
    print("Answer: " + get_most_played("game_stat.txt"))

    print("\nHow many copies have been sold total?")
    print("Answer: " + str(sum_sold("game_stat.txt")))

    print("\nWhat is the average selling?")
    print("Answer: " + str(get_selling_avg("game_stat.txt")))

    print("\nHow many characters long is the longest title?")
    print("Answer: " + str(count_longest_title("game_stat.txt")))

    print("\nWhat is the average of the release dates?")
    print("Answer: " + str(get_date_avg("game_stat.txt")))

    print("\nWhat properties has a game?")
    title = input("Enter a game title to get the game's properties: ")
    print(get_game("game_stat.txt", title))

    print("\nHow many games are there grouped by genre?")
    print(count_grouped_by_genre("game_stat.txt"))

    print("\nWhat is the date ordered list of the games?")
    print(get_date_ordered("game_stat.txt"))


if __name__ == "__main__":
    main()
