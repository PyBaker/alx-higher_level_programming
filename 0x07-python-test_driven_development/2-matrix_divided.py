#!/usr/bin/python3
''' Module with function to test matrix division '''


def matrix_divided(matrix, div):
    '''
    Function to divide all elements in matrix and return
    a new matrix with results
    '''

    if not isinstance(div, (int, float)):
        #print("we foung a wrong div")
        raise TypeError("div must be a number")
    elif div < 0:
        raise ZeroDivisionError("division by zero")
    elif not len(set(map(len, matrix))) == 1:
        #print((set(map(len, matrix))))
        #print("we got an arrat here boys")
        raise TypeError("Each row of the matrix must "
                        + "have the same size")
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            #print([num for num in row])
            raise TypeError("matrix must be a "
                        + "matrix (list of lists) of integers/floats")
    return [[round((num / div), 2) for num in row] for row in matrix]

def main():
    print("just to test :)")
    matrix = [[0, 4 ],[3, 4.4, 4,]]
    print(matrix_divided(matrix, 3))


if __name__ == "__main__":
    main()
