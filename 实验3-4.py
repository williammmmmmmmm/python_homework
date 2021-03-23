print("================\n欢迎使用通讯录:\n1.添加联系人\n2.查看通讯录\n3.删除联系人\n4.修改联系人\n5.查找联系人\n6.退出\n================")
adbook = []
name = ""
find = 0
while 1:
    try:
        x = int(input("请输入你的选项"))
    except ValueError:
        print("请输入整数!!!", end="\n\n")
    if x > 0 and x < 7:
        if x == 1:
            adbook.append([input("请输入联系人的姓名："), input(
                "请输入联系人的手机号："), input("请输入联系人的邮箱："), input("请输入联系人的地址：")])
            print("好友添加成功")
        elif x == 3:
            name = input("请输入要删除的好友姓名:")
            for i in adbook:
                if i[0] == name:
                    adbook.remove(i)
                    print("删除成功")
                    find = 1
                    break
            if find == 0:
                print("###对不起,你还没有这个联系人")
            find = 0
        elif x == 4:
            name = input("请输入要修改的好友姓名:")
            for i in adbook:
                if i[0] == name:
                    adbook.remove(i)
                    find = 1
                    break
            if find == 0:
                print("###对不起,你还没有这个联系人")
                continue
            adbook.append([input("请输入新联系人的姓名："), input(
                "请输入新联系人的手机号："), input("请输入新联系人的邮箱："), input("请输入新联系人的地址：")])
            print("好友修改成功")
            find = 0
        else:
            exit()
    else:
        print("输入有误!")
