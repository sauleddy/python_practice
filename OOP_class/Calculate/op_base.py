#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' this is a base class for operator '

__author__ = 'Eddie Hsu'


class OpBase(object):
    name = 'OpBase'

    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, num):
        self.__num1 = num

    @property
    def num2(self):
        return self.__num2

    def calculate(self):
        pass

    def show_expression(self):
        print(self.__num1 + '?' + self.__num2)

if __name__ == '__main__':
    pass
