# password = input("请输入密码！")
# print("你刚输入的密码是：",password)





#作业: 1.做一个石头剪刀布游戏，已完成，用时24分钟！，继续加油！
import random
print("欢迎来到mygame，本游戏三局两胜！，剪刀0,石头1，布2")
count = 0
for i in range(3):
    x = int(input("请输入0-2之间的一个整数："))
    if x < 0 or x > 2:
        # print("输入无效！游戏终止")
        # exit()
        print("警告：输入无效！")
        x = int(input("请重新输入0-2之间的一个整数："))
    print("机器人准备中......")
    y = random.randint(0,2)
    print(y)
    print("结果比对中......")
    if x == y == 0:
        print("剪刀 vs 剪刀,平局！")
    elif x == y == 1:
        print("石头 vs 石头,平局！")
    elif x == y == 2:
        print("布 vs 布,平局！")
    elif x== 0 and y== 1:
        print("剪刀 vs 石头,机器人胜！")
        count = count-1
    elif x==0 and y== 2:
        print("剪刀 vs 布,恭喜你——胜！")
        count = count+1
    elif x== 1 and y== 0:
        print("石头 vs 剪刀,恭喜你——胜！")
        count = count+1
    elif x==1 and y== 2:
        print("石头 vs 布,机器人胜！")
        count = count-1
    elif x== 2 and y== 0:
        print("布 vs 剪刀,机器人胜！")
        count = count-1
    elif x==2 and y== 1:
        print("布 vs 石头,恭喜你——胜！")
        count = count+1
print("计算中......")
print(count)
print("最终结果如下......")
if count > 0:
    print("you are victory!")
elif count == 0:
    print("平局")
else:
    print("you are failure!")


   
#作业游戏

