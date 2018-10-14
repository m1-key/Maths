def GCD(x,y):
    if(y == 0):
        return (x)
    return(GCD(y,x%y))


def LCM(x,y):
    return(x*y/GCD(x,y))


a,b = map(int,input().split())
print(GCD(a,b))
print(int(LCM(a,b)))
