# -*- coding = utf-8 -*-

from fractions import Fraction


def suffix(ex):
    """
    中缀表达式转后缀表达式
    :param ex: 中缀表达式
    :return: 后缀表达式 suffix_exp[]
    """
    op_weight = {'+': 1, '-': 1, '*': 2, '÷': 2}
    suffix_exp = []  # 后缀表达式存储栈
    op_stack = []  # 运算符栈
    infix_exp = [str(x) for x in ex]
    for element in infix_exp:
        if element in ['+', '-', '*', '÷']:
            while len(op_stack) >= 0:
                if len(op_stack) == 0:
                    op_stack.append(element)
                    break
                op = op_stack.pop()
                if op == '(' or op_weight[element] > op_weight[op]:
				# 若栈顶元素为左括号，或栈顶元素的优先级低于所取运算符，则将栈顶元素返回，并将运算符入栈
                    op_stack.append(op)
                    op_stack.append(element)
                    break
                else:
                    suffix_exp.append(op)
        elif element == '(':  # 若所取为左括号，则直接入运算符栈
            op_stack.append(element)
        elif element == ')':  # 若所取为右括号，则栈顶元素依次出栈，压入表达式栈，直到遇到左括号
            while len(op_stack) > 0:
                op = op_stack.pop()
                if op == '(':
                    break
                else:
                    suffix_exp.append(op)
        else:
            suffix_exp.append(element)

    while len(op_stack) > 0:
        suffix_exp.append(op_stack.pop())

    return suffix_exp


def evaluate(ex):
    """
    后缀表达式求值函数（逆波兰算法）
    :param ex: 后缀表达式
    :return: 运算结果 int、str、分数
    """
    result_stack = []  # 结果栈
    for element in ex:
        if element in ['+', '-', '*', '÷']:
            # 取到运算符，则将栈顶的两个数字弹出，并做运算，并将结果压入结果栈中
            num2 = result_stack.pop()
            num1 = result_stack.pop()
            res = arithmetic(num1, num2, element)   #BUG
            if res is False:
                return False
            result_stack.append(res)
        else:
            if element.find('/') > 0:  # 若取到分数，做特殊运算处理后，压入结果栈
                int_fra = 0
                if element.find("'") > 0:
                    li = element.split("'")
                    int_fra = int(li[0])
                    fra = li[1]
                else:
                    fra = element
                li = fra.split('/')
                nume = int_fra * int(li[1]) + int(li[0])
                deno = int(li[1])
                res = Fraction(nume, deno)
                result_stack.append(res)
            else:
                result_stack.append(Fraction(int(element), 1))

    if str(result_stack[0]).find('/') > 0:  # 若结果为假分数，将其转化为字符型的带分数
        if result_stack[0] > 1:
            nu = result_stack[0].numerator
            de = result_stack[0].denominator
            res2 = str(int(nu / de)) + "'" + str(Fraction(nu % de, de))
            result_stack[0] = res2

    return result_stack[0]


def arithmetic(x, y, op):
    """
    算术函数
    :param x: 操作数1
    :param y: 操作数2
    :param op: 运算符
    :return: 运算结果
    """
    if op == '+':
        return x + y
    elif op == '-' and x >= y:
        return x - y
    elif op == '*':
        return x * y
    elif op == '÷' and y > 0:
        return x / y
    else:
        return False


if __name__ == '__main__':
    # 测试函数
    ex = [1, '*', '2/3', '+', 3, '*', 4]
    re = suffix(ex)
    print(re)
    print(evaluate(re))
