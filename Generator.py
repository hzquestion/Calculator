# -*- coding: utf-8 -*-

import argparse
from random import choice
from random import randint
from fractions import Fraction
from Suffix import suffix, evaluate

def getOperator():
    # 取计算符
    op = ['+', '-', '*', '÷']
    return choice(op)

def getNumber(range):
    # 取自然数
    return randint(0, range - 1)

def getFraction(range):
    # 取分数
    denominator = randint(2, range)
    numerator = randint(1, denominator - 1)
    fraction_int = randint(0, range - 1)
    fra = str(Fraction(numerator, denominator))
    if fraction_int > 0:
        fra = str(fraction_int) + "'" + fra
    return fra

def getBrackets(ex, num_op):
    # 取括号
    if num_op == 2:
        left_bra = randint(0, 1) * 2
        ex.insert(left_bra, '(')
        if left_bra:
            ex.append(')')
        else:
            ex.insert(-2, ')')
    else:
        left_bra = randint(0, 2) * 2
        ex.insert(left_bra, '(')
        if left_bra == 4:
            ex.append(')')
        elif left_bra == 2:
            if randint(0, 1):
                ex.append(')')
            else:
                ex.insert(-2, ')')
        elif left_bra == 0:
            ex.insert(0 - randint(1, 2) * 2, ')')

def getExercise(range, frequency):
    # 生成题目
    data = open("./Exercises.txt", "w+")
    answ = open("./Answer.txt", "w+")
    fre = 1
    while fre <= frequency:
        if randint(0, 1):
            ex = [getNumber(range)]
        else:
            ex = [getFraction(range)]
        n = randint(1, 3)
        num_op = n
        while n > 0:
            ex.append(getOperator())
            if randint(0, 1):
                if ex[-1] == '÷':
                    ex.append(getNumber(range - 1) + 1)
                else:
                    ex.append(getNumber(range))
            else:
                ex.append(getFraction(range))
            n = n - 1
        if num_op > 1 and randint(0, 1): 
            getBrackets(ex, num_op)

        if evaluate(suffix(ex)):
            print(fre, ".", evaluate(suffix(ex)), file=answ)
            print(fre, ".", end=' ', file=data)
            print(fre, ".", end=' ')
            for i in ex:
                print(i, end=' ')
                print(i, end=' ', file=data)
            print('= ')
            print('= ', file=data)
        else:
            fre = fre - 1

        fre = fre + 1
    data.close()

if __name__ == '__main__':
    #测试函数
    getExercise(10, 10)
    getExercise(100, 100)
