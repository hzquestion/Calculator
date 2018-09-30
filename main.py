# -*- coding = utf-8 -*-

import argparse
from Generator import getExercise
from Fetch_Proofread import Proofread

if __name__ == '__main__':
    # 主函数
    print('Generator_Calculator starts working...')
    print('------------------------------------')
    parser = argparse.ArgumentParser(description="This is a Generator_Calculator.")
    parser.add_argument("-n", metavar="--number", type=int, dest="num_arg", help="The numbers of questions.")
    parser.add_argument("-r", metavar="--range", type=int, dest="range_arg", help="The range of random numbers.")
    parser.add_argument("-e", metavar='--exercise file', dest="exercisefile_arg", help="Given the exercise file.")
    parser.add_argument("-a", metavar="--answer file", dest="answerfile_arg", help="Given the answer file.")
    args = parser.parse_args()
    if args.num_arg:
        if args.range_arg:
            print("-----------Generating....-----------")
            getExercise(args.range_arg, args.num_arg)
            print("-----------Generated.---------------")
        else:
            print('ERROR:Please give the numerical range.')
            exit(0)
    elif args.range_arg and args.num_arg is None:
        print("-----------Generating....-----------")
        getExercise(args.range_arg, 10)
        print("-----------Generated.---------------")

    if args.exercisefile_arg:
        if args.answerfile_arg:
            print("-----------Calculating...-----------")
            Proofread(args.exercisefile_arg, args.answerfile_arg)
            print("-----------Calculated.--------------")
        else:
            print('ERROR:Please check that the path is correct and that the answerfile exists.')
            exit(0)

    print('------------------------------------')
    print('Thank you for using it!')
    print('Bye,have a great time!')
#    print('\n'.join([''.join([('Study'[(x - y) % 5] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))