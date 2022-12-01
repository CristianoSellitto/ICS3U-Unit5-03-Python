#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# This program turns a level to a percentage


def find_percentage(level: str) -> int:
    # Turns a level to a percentage

    match level:
        case "4+":
            percent = 97
        case "4":
            percent = 91
        case "4-":
            percent = 83
        case "3+":
            percent = 78
        case "3":
            percent = 75
        case "3-":
            percent = 71
        case "2+":
            percent = 68
        case "2":
            percent = 65
        case "2-":
            percent = 61
        case "1+":
            percent = 58
        case "1":
            percent = 55
        case "1-":
            percent = 51
        case "R":
            percent = 30
        case "NE":
            percent = 0
        case _:
            percent = -1
    return percent


def main():
    # Gets the level and outputs the percent if the level is valid

    level_text = input("Enter a level to convert to percent: ")
    percent_text = find_percentage(level_text)
    if not percent_text == -1:
        print(
            "\nA level of {0} has a middle percent of {1}".format(
                level_text, percent_text
            )
        )
    else:
        print("\n{0} is not a valid level.".format(level_text))

    print("\nDone.")


if __name__ == "__main__":
    main()
