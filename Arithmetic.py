# -*- coding = utf-8 -*-

from fractions import Fraction

def suffix(ex):
    #中缀转后缀表达式
    op_weight = {'+': 1, '-': 1, '*': 2, '÷': 2}
    suffix_exp = []   
    op_stack = []   
    infix_exp = [str(x) for x in ex] 
    for element in infix_exp:
        if element in ['+', '-', '*', '÷']:  
            while len(op_stack) >= 0:
                if len(op_stack) == 0:  
                    op_stack.append(element)
                    break
                op = op_stack.pop() 
                if op == '(' or op_weight[element] > op_weight[op]:
                    op_stack.append(op)
                    op_stack.append(element)
                    break
                else:
                    suffix_exp.append(op)  
        elif element == '(':   
            op_stack.append(element)
        elif element == ')':  
            while len(op_stack) > 0 :
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
    #后缀表达式求值函数
    result_stack = []  
    for element in ex:
        if element in ['+', '-', '*', '÷']:
            num2 = result_stack.pop()
            num1 = result_stack.pop()
            re = arithmetic(num2, num1, element)
            if re < 0 or re == False:
                return False
            result_stack.append(re)
        else:
            if element.find('/') > 0:  
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
                re = Fraction(nume, deno)
                result_stack.append(re)
            else:
                result_stack.append(Fraction(int(element), 1))   

    if result_stack[0] < 0:   
        return False

    if str(result_stack[0]).find('/') > 0:   
        if result_stack[0] > 1:
            nu = result_stack[0].numerator
            de = result_stack[0].denominator
            re2 = str(int(nu / de)) + "'" + str(Fraction(nu % de, de))
            result_stack[0] = re2

    return result_stack[0]

def arithmetic(x, y, op):
    #算术函数
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '÷' and y > 0:
        return x / y
    else:
        return False

if __name__ == '__main__':
    #测试函数
    ex = [1, '*', '2/3', '+', 3, '*', 4]
    re = suffix(ex)
    print(re)
    print(evaluate(re))