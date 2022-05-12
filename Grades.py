# this function finds the correct %
def calc_mark(level):

    mark = 0
    
    if level == "-1":
        return "51"
    elif level == "1":
        mark = "54.5"
    elif level == "+1":
        mark = "58"
    elif level == "-2":
        mark = "61"
    elif level == "2":
        mark = "63"
    elif level == "+2":
        mark = "68"
    elif level == "-3":
        mark = "71"
    elif level == "3":
        mark = "74.5"
    elif level == "+3":
        mark = "78"
    elif level == "-4":
        mark = "83"
    elif level == "4":
        mark = "90"
    elif level == "+4": 
        mark = "97.5"
    # invalid input checker
    else:
        print("Invalid input")
        mark = -1
    return mark


def main():
    # input
    level = input("Enter a level: ")

    # call functions
    percentage = calc_mark(level)
    try: 
        level = int(level)
    # invalid input checker 
        if level != 0:
            if level < 5 and level > -5:
        # output
                print("Level {} has a mid percentage of {}%".format(level, percentage))
    except ValueError:
        print("Enter a valid level")



if __name__ == "__main__":
    main()
