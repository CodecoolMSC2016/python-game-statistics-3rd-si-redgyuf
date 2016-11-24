from reports import *


def main():
    print("How many games are in the file?")
    print("Answer: " + str(count_games("game_stat.txt")))

    print("\nIs there a game from a given year?")
    year = int(input("Enter the year: "))
    print("Answer: " + str(decide("game_stat.txt", year)))

    print("\nWhich was the latest game?")
    print("Answer: " + get_latest("game_stat.txt"))

    print("\nHow many games do we have by genre?")
    genre = input("Enter the genre: ")
    print("Answer: " + str(count_by_genre("game_stat.txt", genre)))

    print("\nWhat is the line number of the given game (by title)?")
    title = input("Enter the title: ")
    print("Answer: " + str(get_line_number_by_title("game_stat.txt", title)))

    print("\nWhat is the alphabetic ordered list of the titles?")
    print(sort_abc("game_stat.txt"))

    print("\nWhat are the genres?")
    print(get_genres("game_stat.txt"))

    print("\nWhat is the release date of the top sold First-person shooter game?")
    print("Answer: " + str(when_was_top_sold_fps("game_stat.txt")))


if __name__ == "__main__":
    main()
