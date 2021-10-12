#!/usr/bin/pytho3
if __name__ == "__main__":
    import calculator_1 as c
    import argparse

    operator = {
              '+':c.add,
              '-':c.sub,
              '/':c.div,
              '*':c.mul,
             }
    parser = argparse.ArgumentParser(description='Add Subtract Divide or Multiply two integers',usage='./100-my_calculator.py <a> <operator> <b>)')
    parser.add_argument('n1', type=int, metavar='<a>',
                        help='first number')
    parser.add_argument('sign', metavar='<operator>',
                        help='math operator', )
    parser.add_argument('n2', type=int, metavar='<b>',
                        help='secondNumber')
    args = parser.parse_args()
    if args.sign not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{}".format(args.n1))
    print("{}".format(args.n2))
    print("{}".format(operator[args.sign]))
    print("{}".format(operator[args.sign](args.n1, args.n2)))
    #print("{} {} {} = {}".format(args.n1, args.sign, args.n2,
    #                             operator[args.sign](args.n1, args.n2)))
