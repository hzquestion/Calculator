# -*- coding = utf-8 -*-

from Arithmetic import suffix, evaluate


def Proofread(file_exercise, file_answer):
    """
    对题目文件内的题目进行计算，得出答案与答案文件校对
    :param file_exercise: 题目文件
    :param file_answer: 答案文件
    :return: None
    """
    num = 1             # 题目号
    correct_num = 0     # 正确题目数量
    wrong_num = 0       # 错误题目数量
    correct_list = []   # 正确题目号集合
    wrong_list = []     # 错误题目号集合
    try:
        with open(file_exercise) as f1, open(file_answer) as f2, open("./Grade.txt", "w+") as Grade:
            for exercise, answer in zip(f1.readlines(), f2.readlines()):
                ex = exercise.split(" . ")[1].split(' = ')[0].split(' ')
                right_answer = evaluate(suffix(ex))
                an = answer.split(' . ')[1].split('\n')[0]
                if str(right_answer) == an:
                    correct_num = correct_num + 1
                    correct_list.append(num)
                else:
                    wrong_num = wrong_num + 1
                    wrong_list.append(num)
                num = num + 1
            print('Correct:', correct_num, tuple(correct_list), file=Grade)
            print('Correct:', correct_num, tuple(correct_list))
            print('Wrong:', wrong_num, tuple(wrong_list), file=Grade)
            print('Wrong:', wrong_num, tuple(wrong_list))
    except IOError:
        print('ERROR:Please check that the path is correct and that the file exists.')


if __name__ == '__main__':
    # 测试函数
    Proofread('exercisesfile.txt', 'answerfile.txt')