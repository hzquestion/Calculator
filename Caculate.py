# -*- coding: utf-8 -*-  

import sys
import argparse
from random import choice
from random import randint
from fractions import Fraction

def getOperator():
	#取计算符
	op = ('+','-','*','÷')
	return choice(op)

def getNumber(max):
	#取自然数
	return randint(0,max-1)
		
def getFraction(max):
	#取分数
	denominator = randint(2,max)
	numerator = randint(1,denominator-1)
	fraction_int = randint(0,max-1) 
	fra = str(Fraction(numerator,denominator))
	if fraction_int > 0:
		fra = str(fraction_int) + "'" + fra
	return fra
	
def getBrackets(e,num_op):
	#取括号
	if num_op == 2:
		left_bra = randint(0,1) * 2
		e.insert(left_bra,'(')
		if left_bra:
			e.append(')')
		else:
			e.insert(-2,')')
	else:
		left_bra = randint(0,2) * 2
		e.insert(left_bra,'(')
		if left_bra == 4:
			e.append(')')
		elif left_bra == 2:
			if randint(0,1):
				e.append(')')
			else:
				e.insert(-2,')')
		elif left_bra == 0:
			e.insert(0-randint(1,2)*2,')')
	
def getExercise(max):
	#生成题目
	e=[getNumber(max)]
	n = randint(1,3)
	num_op = n
	while n > 0:
		e.append(getOperator())
		if randint(0,1):
			if e[-1] == '÷':
				e.append(getNumber(max-1)+1)
			else:
				e.append(getNumber(max))
		else:
			e.append(getFraction(max))
		n = n - 1
	if num_op > 1 and randint(0,1):
		getBrackets(e,num_op)
	for i in e:
		print(i,end = ' ')
		print(i,end = ' ',file=data)
	print('= ')
	print('= ',file=data)

if __name__=='__main__':
	#主函数
	print('Caculate starts working...')
	print('--------------------------------')
	parser = argparse.ArgumentParser(description="This is a Caculate.")
	parser.add_argument("-n", metavar = "--number",  type=int, dest = "num_arg", help = "The numbers of questions.")
	parser.add_argument("-r", metavar = "--range", type=int, dest = "range_arg", help = "The range of random numbers.")
	args = parser.parse_args()
	if args.num_arg and args.range_arg:
		data = open("./Exercises.txt","w+")
		n = args.num_arg
		i = 1
		print("-----------generating....-----------")
		while n > 0:
			print(i,".",end = ' ')
			print(i,".",end = ' ',file = data)
			getExercise(args.range_arg)
			n = n - 1
			i = i + 1
		data.close()
		print("------------generated.--------------")
	