
def countCloseToZero(a):
    n = len(a) #1000
    k = 0
    for (x,y) in a:
        if (x**2 + y**2)**0.5 <= 0.25:
            k += 1
    return k/n

for J in range(100):
    arr = list(map(float,input().split()))
    a = []
    for i in range(0,len(arr),2):
        a.append((arr[i],arr[i+1]))
        
    kn = countCloseToZero(a)
    
    if kn > 0.15:
        print(1)
    else:
        print(2)
