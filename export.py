# Export the return values of the functions to a file (game_answers_export.txt)

from reports import *


def main():
    with open("game_answers_export.txt", mode="w") as my_file:

        my_file.write("How many games are in the file?\n")
        my_file.write("Answer: " + str(count_games("game_stat.txt")))

        print("\nIs there a game from a given year?")
        year = int(input("Enter the year: "))
        my_file.write("\n\nIs there a game from a given year?\n")
        my_file.write("Answer: " + str(decide("game_stat.txt", year)))

        my_file.write("\n\nWhich was the latest game?\n")
        my_file.write("Answer: " + get_latest("game_stat.txt"))

        print("\nHow many games do we have by genre?")
        genre = input("Enter the genre: ")
        my_file.write("\n\nHow many games do we have by genre?\n")
        my_file.write("Answer: " + str(count_by_genre("game_stat.txt", genre)))

        print("\nWhat is the line number of the given game (by title)?")
        title = input("Enter the title: ")
        my_file.write(
            "\n\nWhat is the line number of the given game (by title)?\n")
        my_file.write(
            "Answer: " + str(get_line_number_by_title("game_stat.txt", title)))

        my_file.write(
            "\n\nWhat is the alphabetic ordered list of the titles?\n")
        my_file.writelines('\n'.join(sort_abc("game_stat.txt")) + '\n')

        my_file.write("\nWhat are the genres?\n")
        my_file.writelines('\n'.join(get_genres("game_stat.txt")) + '\n')

        my_file.write(
            "\nWhat is the release date of the top sold First-person shooter game?\n")
        my_file.write("Answer: " + str(when_was_top_sold_fps("game_stat.txt")))


if __name__ == "__main__":
    main()
