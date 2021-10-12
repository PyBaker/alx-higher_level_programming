#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in range(len(names)):
        if names[i].startswith("__"):
            continue
        else:
            print("{}".format(names[i]))
