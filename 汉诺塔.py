
def hanoi(n,a,b,c):    #一共n个,从a移到c
    if n>0:
        hanoi(n-1,a,c,b)
        print("%s->%s" % (a,c))
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')

