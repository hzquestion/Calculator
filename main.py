# -*- coding = utf-8 -*-

import argparse
from Generator import getExercise

if __name__ == '__main__':
    # 主函数
    print('Calculator starts working...')
    print('------------------------------------')
    parser = argparse.ArgumentParser(description="This is a Caculate.")
    parser.add_argument("-n", metavar="--number", type=int, dest="num_arg", help="The numbers of questions.")
    parser.add_argument("-r", metavar="--range", type=int, dest="range_arg", help="The range of random numbers.")
    args = parser.parse_args()
    if args.num_arg and args.range_arg:
        print("-----------Generating....-----------")
        getExercise(args.range_arg, args.num_arg)
        print("------------Generated.--------------")
    print('------------------------------------')
    print('Thank you for using it!')
    print('Bye,have a great time!')
#    print('\n'.join([''.join([('Study'[(x - y) % 5] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))