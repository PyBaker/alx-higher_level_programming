#!/usr/bin/python3
''' Module with Rectangle Class '''


class Rectangle:
    ''' Defines a Rectangle with given values'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initialisation function of Rectangle'''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value_of_width):
        if type(value_of_width) is not int:
            raise typeerror('width must be an integer')
        elif value_of_width < 0:
            raise valueerror('width must be >= 0')
        else:
            self.__width = value_of_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value_of_height):
        if type(value_of_height) is not int:
            raise typeerror('height must be an integer')
        elif value_of_height < 0:
            raise valueerror('height must be >= 0')
        else:
            self.__height = value_of_height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare area of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an isinstance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an isinstance of Rectangle')
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    def area(self):
        '''Returns area of Rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns perimeter of Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ String representation of Square """
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """ Official string representation of Square """
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """Print message when an instastance of class is deleted"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print('Bye rectangle...')
