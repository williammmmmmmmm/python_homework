week=["Monday","Tuesday","Wednesday","Thusday","Friday","Saturday","Sunday"]
x=input("请输入字母")
for j in week:
    if len(x)==2:
        if j[0]==x[0] and j[1]==x[1]:
            print(j)
    elif j[0]==x[0]:
        print(j)
