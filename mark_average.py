#!/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Oct 2021
# This program uses a list to calculate a user's mark percentages
#  and outputs their average


def calculate_average(percentage_list):
    # this function calculates the average of percentages inside a list
    #  and rounds it off

    # process
    average_result = sum(percentage_list) / len(percentage_list)
    average_rounded = round(average_result, 1)

    return average_rounded


def main():
    # this function creates a list and lets the user enter as many marks as
    #  they want until they use '-1' to end the prompts and call a function
    #  that calculates their average

    percentages = []
    temp_percentages = None

    # input
    print("Enter your mark percentages. Then enter -1 to find the average.")
    print("")

    temp_percentages = input("Mark (%): ")

    # output
    try:

        temp_percentages_int = int(temp_percentages)
        percentages.append(temp_percentages_int)
        if temp_percentages_int < -1:
            print("\nThe last mark you wrote makes no sense.")
        elif temp_percentages_int > 100:
            print("\nThe last mark you wrote makes no sense.")
        else:
            while True:
                if temp_percentages_int < -1:
                    print("\nThe last mark you wrote makes no sense.")
                    break
                if temp_percentages_int > 100:
                    print("\nThe last mark you wrote makes no sense.")
                    break
                if temp_percentages_int == -1:
                    break

                temp_percentages = input("Mark (%): ")
                temp_percentages_int = int(temp_percentages)
                percentages.append(temp_percentages_int)

            percentages.pop()

            calculated_average = calculate_average(percentages)
            print("\nYour average percentage is {0}%".format(calculated_average))

    except Exception:
        print("\nThat is an invalid percentage.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
