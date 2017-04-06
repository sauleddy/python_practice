#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' this class is responsible for the substraction of integers '

from Calculate import op_base

__author__ = 'Eddie Hsu'


class Sub(op_base.OpBase):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def calculate(self):
        return self.num1 - self.num2


if __name__ == '__main__':
    pass
