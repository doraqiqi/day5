# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

#1-2*((60-30+(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))-(-4*3)/ (16-3*2))

def calc(input_calc):
    while "("  in input_calc:#式子里有括号
        most_in_fomula = most_in(input_calc)#提取第一个最里面括号的算术式
        print(most_in_fomula)
        bracket_answer = most_in_fomula_calc(most_in_fomula)#计算括号里的内容
        print(bracket_answer)
        input_calc = re.sub(r'\([^()]+\)',str(bracket_answer),input_calc,count=1)
        print(input_calc)
        #把答案放回原来的位置
    else:
        no_bracket_answer = most_in_fomula_calc(input_calc)#这里没有括号的答案就是最终答案
        #print(no_bracket_answer)
    return no_bracket_answer

def most_in_fomula_calc(most_in_fomula):
    '''
    计算不含括号的内容
    :param most_in_fomula:
    :return:
    '''
    while "*" in most_in_fomula or "/" in most_in_fomula:#只要有乘除号就先做乘除法
        print(most_in_fomula)
        fomula_multiply_or_devide = re.search("(\d+\.\d+|\d+)(\*|\/)(\-{0,1}\d+\.\d+|\-{0,1}\d+)",most_in_fomula).group()#提取第一个含有乘除号的算式
        print(fomula_multiply_or_devide)
        if "*" in fomula_multiply_or_devide:#如果提取出来是乘法
            most_in_answer = multiply(fomula_multiply_or_devide)#计算出答案
            print("乘除法计算出的答案",most_in_answer)
            most_in_fomula = re.sub("(\d+\.\d+|\d+)\*(\-{0,1}\d+\.\d+|\-{0,1}\d+)",str(most_in_answer),most_in_fomula,count=1)#把答案替换原来的算式
            print("乘除法答案替换回原来的位置后的算式",most_in_fomula)
            most_in_fomula = re.sub("\-\-","+",most_in_fomula,count=1)#检查式子里是否存在减号加上负号
            most_in_fomula = re.sub("\+\-","-",most_in_fomula,count=1)#检查式子里是否存在减号加上负号

        else:#如果提取出是除法
            most_in_answer = devide(fomula_multiply_or_devide)#计算出答案
            print("乘除法计算出的答案",most_in_answer)
            most_in_fomula = re.sub("(\d+\.\d+|\d+)\/(\-{0,1}\d+\.\d+|\-{0,1}\d+)", str(most_in_answer), most_in_fomula, count=1)#替换原来的算式
            print("乘除法答案替换回原来的位置后的算式",most_in_fomula)
            most_in_fomula = re.sub("\-\-","+",most_in_fomula,count=1)#检查式子里是否存在减号加上负号,如果有就替换成加号
            most_in_fomula = re.sub("\+\-","-",most_in_fomula,count=1)#检查式子里是否存在减号加上负号，如果有就替换成减号
    else:#当没有乘除号就开始计算加减法
        print("这是没有乘除法的算式：",most_in_fomula)
        most_in_answer = plus_minus(most_in_fomula)
    return most_in_answer

def devide(fomula_devide):
    num1 = re.search("^\-{0,1}\d+\.\d+|\d+",fomula_devide).group()#提取第一个数字
    print(num1)
    num2_temp = re.search("\/(\-{0,1}\d+\.\d+|\d+)",fomula_devide).group()
    print(num2_temp)
    num2 = re.search("\-{0,1}\d+\.\d+|\d+",num2_temp).group()
    print(num2)
    fomula_devide_answer = float(num1) / float(num2)
    print(fomula_devide_answer)
    return fomula_devide_answer

def most_in(last_calc):
    '''
    提取最里面的括号内容
    :param last_calc: 
    :return: 
    '''
    most_in_fomula = re.search(r'\([^()]+\)', last_calc).group()
    return most_in_fomula

def multiply(fomula_multiply):
    num1 = re.search("^\-{0,1}\d+\.\d+|\d+",fomula_multiply).group()
    print(num1)
    num2_temp = re.search("\*(\-{0,1}\d+\.\d+|\d+)",fomula_multiply).group()
    print(num2_temp)
    num2 = re.search("\-{0,1}\d+\.\d+|\d+",num2_temp).group()
    print(num2)
    fomula_multiply_answer = float(num1) * float(num2)
    print(fomula_multiply_answer)

    return fomula_multiply_answer

def plus_minus(most_in_fomula):#把式子转换成正数和负数，然后把他们相加
        most_in_fomula_list = re.findall("(^\d+\.\d+|\d+)|(\+|\-|\*|\/)(\d+\.\d+|\d+)",most_in_fomula)
        most_in_answer = 0
        for i in most_in_fomula_list:
            print(i)
            if "-" in i:
                print("这是有减号的",i)
                number = float(i[2])*-1
                print(number)
                most_in_answer = most_in_answer+number
            elif "+" in i:
                print("这是有加号的",i)
                number = float(i[2])
                print(number)
                most_in_answer = most_in_answer+number
            else:
                print("这是没有符号的",i)
                number = float(i[0])
                print(number)
                most_in_answer = most_in_answer+number
            print("括号里的答案是：",most_in_answer)
        print(most_in_fomula_list)
        return most_in_answer

if __name__ == '__main__':

    input_calc = input("输入你想要计算的内容：")
    input_calc = re.sub("\s","",input_calc)#去除空格
    final_answer = calc(input_calc)
    print("\033[31m最终答案：%s\033[0m"%final_answer)



