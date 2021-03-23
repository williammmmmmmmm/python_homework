for x in range(1,10):
    for y in range(1,x+1):
        # if y>x:
        #     continue
        print("%d*%d=%d" % (y,x,x*y) ,end=" ")
        if x==y :
            print()
            continue