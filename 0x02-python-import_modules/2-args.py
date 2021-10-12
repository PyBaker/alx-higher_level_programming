#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Prints arguments")
    parser.add_argument('strings', type=str, metavar='', nargs='+', help='string arguments')
    args = parser.parse_args()
    count = len(args.strings) - 1

    if count == 0:
        print("{} arguments".format(count))
    elif count == 1:
        print("{} argument".format(count))
    else:
        print("{} arguments".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, args.strings[i + 1]))
