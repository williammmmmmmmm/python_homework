x=0
firandlist =[]
print("欢迎使用好友系统\n1：添加好友\n2：删除好友\n3：备注好友\n4：展示好友\n5：退出")
while 1: 
    try:
        x=int(input("请输入你的选项"))
    except ValueError:
        print("请输入整数!!!",end="\n\n")
    if x > 0 and x < 6:
        if x==1:            
            firandlist.append(input("请输入要添加的好友:"))
            print("好友添加成功")
        elif x==2:
            try:
                firandlist.remove(input("请输入要删除的好友姓名:"))
            except ValueError:
                print("###对不起,你还没有这个好友")
        elif x==3:
            try:
                firandlist.remove(input("请输入要修改的好友姓名:"))
            except ValueError:
                print("###对不起,你还没有这个好友")
            else:
                firandlist.append(input("请输入修改后的好友姓名："))
                print("修改成功")
        elif x==4:
            for i in firandlist:
                print(i, end=" ")
            print()
        else:
            exit()
    else:
        print("输入有误!")

