import random
for x in range(1,9):
    print("第%d个老师随机分配到第%d间办公室" % (x,random.randint(1,3)))
