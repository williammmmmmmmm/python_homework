pw=input("请输入密码六位:")
x=0
y=""
for a in pw:
    x = x + int(ord(a))
    
print("ASCII值求和为:" ,x)
for a in pw:
    y= y + str(ord(a))
    
print("ASCII值前后拼接结果为:" ,y)
print("ASCII值前后拼接后反转结果为:" ,y[::-1])
print("最后加密后的密码为:" , int(y[::-1])+int(x))