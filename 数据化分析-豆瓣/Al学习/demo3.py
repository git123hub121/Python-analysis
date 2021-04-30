#根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里去，最终用户输入q退出时，打印购买的商品列表

products = [["iphone",6888],["MacPro",14800],["小米",2499],["Coffee",31],["Book",60],["Nike",699]]
i = 0
for product in products:
    #print(product)
    print(i,end="\t")
    i += 1
    for x in product:
        print(x,end="\t")
    print("\n")
count = 0
total = []
print("欢迎来到XX商店！")
while len(products) > 0:
    x = input("你好，请在0-5中选择相应的商品,如需退出购物车，请输入q：")
    # print(type(x))
    if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        count += 1
        print("输入正确，商品添加购物车等待中...")
        print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        print("商品是：",end="\t")
        for y in products[int(x)]:
            print(y,end="\t")
        print("购物数量 +%d"%count,end="\t")
        print("\n")
        z = int(x)
        total.append(z)
        
    elif x == 'q':
        print("退出购物车！")
        break
    else:
        print("输入无效，请重新输入！")
        x = input("你好，请在0-5中选择相应的商品,如需退出购物车，请输入q：")
        if x == 'q':
            print("退出购物车！")
            break

print("商品总计为：",count)
print("打印列表如下：")
print("="*20)
 
for c in total:
    print(c,end=" ")
    for d in products[c]:
        print(d,end=" ")
    print("")       
print("="*20)
            
#列表作业游戏

# if x == '0':
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)
        # elif x == '1':
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)
        # elif x == '2':
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)
        # elif x == '3':
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)
        # elif x == '4':
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)
        # else:
        #     print("该商品编号为\t%s\t的商品已加入购物车"%x,end="\t")
        #     print("商品是：",end="\t")
        #     for y in products[int(x)]:
        #         print(y,end="\t")
        #     print("购物数量 +%d"%count,end="\t")
        #     print("\n")
        #     z = int(x)
        #     total.append(z)