from reports import *
import json


def main():
    with open("game_answers_export.txt", mode="w") as my_file:

        my_file.write("What is the title of the most played game?\n")
        my_file.write("Answer: " + get_most_played("game_stat.txt"))

        my_file.write("\n\nHow many copies have been sold total?\n")
        my_file.write("Answer: " + str(sum_sold("game_stat.txt")))

        my_file.write("\n\nWhat is the average selling?\n")
        my_file.write("Answer: " + str(get_selling_avg("game_stat.txt")))

        my_file.write("\n\nHow many characters long is the longest title?\n")
        my_file.write("Answer: " + str(count_longest_title("game_stat.txt")))

        my_file.write("\n\nWhat is the average of the release dates?\n")
        my_file.write("Answer: " + str(get_date_avg("game_stat.txt")))

        title = input("Enter a game title to get the game's properties: ")
        my_file.write("\n\nWhat properties has " + title + "?\n")
        my_file.writelines(str(get_game("game_stat.txt", title)))

        my_file.write("\n\nHow many games are there grouped by genre?\n")
        json.dump(count_grouped_by_genre("game_stat.txt"), my_file, indent=2)

        my_file.write("\n\nWhat is the date ordered list of the games?\n")
        json.dump(get_date_ordered("game_stat.txt"), my_file, indent=2)


if __name__ == "__main__":
    main()
