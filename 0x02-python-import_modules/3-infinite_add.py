#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Adds sum of intergers(args)')
    parser.add_argument('nums', type=int, metavar='N', nargs='+', help='Numbers to add')
    parser.add_argument('--add', dest='func', default=sum)
    args = parser.parse_args()

    print("{} is FUNCTION".format(args.func))
    print("{} is LIST".format(args.nums))
    print("{} is the function call ".format(args.func(args.nums)))
