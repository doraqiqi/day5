# Author：zhaoyanqi
import os,sys
dir_path = os.path.dirname
BASE_DIR = "%s\\Atm"%dir_path(dir_path(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main

shopping_list = []
product_list = []

f_shoppinglist = open("shoppinglist","r",encoding="utf-8")
#print(f_shoppinglist.read())
for line in f_shoppinglist:
    #print(line)
    if line != "":
        shopping_list.append(line.strip())
f_shoppinglist.close()
print(shopping_list)

with open("money","r") as money:
    money_sum = money.read()
    money_sum = int(money_sum)


list = open("product","r",encoding="utf-8")

for line in list:
    product_line = line.strip().split()
    product_line[1] = int(product_line[1])
    product_line = tuple(product_line)
    product_list.append(product_line)


while True:
    for index, i in enumerate(product_list):
        print(index+1, i)
    Number = input("请输入商品编号加入购物车，输入c查看购物车，按q退出:")
    if Number.isdigit():
        Number = int(Number)-1#刚刚编号加了1所以这里要减1
        if Number < len(product_list) and Number >= 0:
            p_item = product_list[Number]
            money_sum += p_item[1]
            shopping_list.append(p_item)
            print("你的商品一共需要\033[31;1m[%s]\033[0m"%money_sum)

        else:
            print("没有这个商品")
    elif Number == 'c':
        if len(shopping_list) < 1:
            print("购物车是空的~")
        else:
            for i3 in shopping_list:
                print(i3)
            while True:
                make_sure= input('您的商品一共要\033[31;1m[%s]\033[0m元，确认结帐吗？y确认，n返回继续购物'% money_sum)
                if make_sure == "y":
                    pay_success = main.custom(money_sum, "mall")
                    if pay_success:
                        print("\033[31;1m付款成功！\033[0m")
                        shopping_list = []#清空购物车
                        money_sum = 0#购物金额清零
                        # with open("shoppinglist","w") as o:#清空购物车
                        #     pass
                        # with open("money", "w") as money_w:#购物金额清零
                        #     money_w.write("0")
                        break
                    else:
                        print("\033[31;1m付款失败！\033[0m")
                        break
                elif make_sure == "n":
                    zero = input("是否清空购物车?y是，n否")
                    if zero == "y":
                        shopping_list = []
                        money_sum = 0
                        break
                    elif zero =="n":
                        break
                    else:
                        print("输入错误")
                else:
                    print("输入错误")

    elif Number == 'q':
        #退出时把购物车和money数量写入到文件里
        f_shoppinglist2 = open("shoppinglist", "w", encoding="utf-8")
        for i3 in shopping_list:
            f_shoppinglist2.write(str(i3)+"\n")
        f_shoppinglist2.close()
        with open("money", "w") as money:
            money.write(str(money_sum))
        exit()

    else:
        print("请正确输入")






