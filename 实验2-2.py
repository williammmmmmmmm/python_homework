import math
x=int(input("请输入需要判断的数:"))
if x <1000 and x > 99:
    if math.pow(x//100,3)+math.pow(x%100//10,3)+math.pow(x%100%10,3)==x:
        print("是水仙花数")
    else:
        print("不是水仙花数")
