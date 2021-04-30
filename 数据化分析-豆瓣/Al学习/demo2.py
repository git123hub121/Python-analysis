# namelist = []

# namelist = ["小张","1",1,"小李"]
# print(namelist[1])
# print(type(namelist[2]))

# print(len(namelist))

#增
# print("增加前")
# for name in namelist:
#     print(name)

# nametemp = input("请输入：")
# namelist.append(nametemp) 

# namelist.extend([3,4])

# namelist.insert(1,5)



# print("增加后")
# for name in namelist:
#     print(name)


import random
offices = [[],[],[]]
names = ["A","B","C","D","E","F","G","H"]

for name in names:
    index = random.randint(0,3)
    offices[index].append(name)
i = 1
for office in offices:
    print("办公室%d的人数为： %d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*10)
    
#列表