# -*- coding: utf-8 -*-

from random import choice
from random import randint
from fractions import Fraction
from Arithmetic import suffix, evaluate


def getOperator():
    """
    随机生成'+,-,*,÷'的运算符
    :return: '+','-','*','÷'
    """
    op = ['+', '-', '*', '÷']
    return choice(op)


def getNumber(ran):
    """
    随机生成整数操作数
    :param ran: 整数操作数的最大范围，不能取这个数
    :return: 整数操作数int
    """
    return randint(0, ran - 1)


def getFraction(ran):
    """
    随机生成真/带分数
    :param ran: 分数的最大范围
    :return: 分数操作数str
    """
    denominator = randint(2, ran)
    numerator = randint(1, denominator - 1)
    fraction_int = randint(0, ran - 1)
    fra = str(Fraction(numerator, denominator))
    if fraction_int > 0:
        fra = str(fraction_int) + "'" + fra
    return fra


def getBrackets(ex, num_op):
    """
    在表达式中随机插入括号
    :param ex: 表达式List
    :param num_op: 运算符数量
    :return: None
    """
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


def getExercise(ran, frequency):
    """
    表达式生成主函数
    :param ran: 自然数、分数分母的最大范围
    :param frequency: 题目的个数
    :return: None
    """
    data = open("./Exercises.txt", "w+")
    answ = open("./Answer.txt", "w+")
    fre = 1
    while fre <= frequency:
        if randint(0, 2):
            ex = [getNumber(ran)]
        else:
            ex = [getFraction(ran)]
        n = randint(1, 3)
        num_op = n
        while n > 0:
            ex.append(getOperator())
            if randint(0, 1):
                if ex[-1] == '÷':
                    ex.append(getNumber(ran - 1) + 1)
                else:
                    ex.append(getNumber(ran))
            else:
                ex.append(getFraction(ran))
            n = n - 1
        if num_op > 1 and randint(0, 1):  # 当运算符有两个以上时，随机确认是否加入括号
            getBrackets(ex, num_op)

        result = evaluate(suffix(ex))
        if result:
            print(fre, ".", result, file=answ)
            print(fre, ".", result)
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
    # 测试函数
    getExercise(10, 10)
    getExercise(100, 100)
