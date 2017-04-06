#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' this class is responsible for the addition of integers '

from Calculate import op_base

__author__ = 'Eddie Hsu'


class Add(op_base.OpBase):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def calculate(self):
        return self.num1 + self.num2

    def __inner_func(self):
        return isinstance(self.num1, int)


if __name__ == '__main__':
    obj_add = Add(10, 20)
    print(obj_add.calculate())
