# my_mod.py

def enlarge(n):
    return n * 100


if __name__ == "__main__":
    # only run the code below if executing this script from the command line
    # otherwise don't run it (for example if we're trying to import something)

    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))