# -*- coding = utf-8 -*-

import argparse
from Generator import getExercise

if __name__ == '__main__':
    # 主函数
    print('Caculate starts working...')
    print('--------------------------------')
    parser = argparse.ArgumentParser(description="This is a Caculate.")
    parser.add_argument("-n", metavar="--number", type=int, dest="num_arg", help="The numbers of questions.")
    parser.add_argument("-r", metavar="--range", type=int, dest="range_arg", help="The range of random numbers.")
    args = parser.parse_args()
    if args.num_arg and args.range_arg:
        print("-----------Generating....-----------")
        getExercise(args.range_arg, args.num_arg)
        print("------------Generated.--------------")
	print('--------------------------------')
	print('Thank you for using it!Bye,have a great time!')