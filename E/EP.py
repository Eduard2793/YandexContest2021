
def F(x0,C):
    x1 = []
    x2 = []
    for i in range(len(x0)):
        x1.append(x0[i]**2)
    for i in range(len(x0)-1):
        x2_i = []
        for j in range(1,len(x0)-i):
            x2_i.insert(0, (x0[i]*x0[-j]))
            
        x2 += x2_i
            
    x = x0 + x1 + x2
    
    y = 0
    for i in range(len(x)):
        y += x[i]*C[i]
        
    return y
    
def getX(x0):
    x1 = []
    x2 = []
    for i in range(len(x0)):
        x1.append(x0[i]**2)
    for i in range(len(x0)-1):
        x2_i = []
        for j in range(1,len(x0)-i):
            x2_i.insert(0, (x0[i]*x0[-j]))
            
        x2 += x2_i
            
    return x0 + x1 + x2


n = 1000

Y = []
X = []


for _ in range(n):
    xy = list(map(float,input().split('\t')))
    Y.append(xy.pop())
    X.append(getX(xy))
    
X_test = []
for _ in range(n):
    X_test.append(list(map(float,input().split('\t'))))
  
   
from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit(X,Y)


C = reg.coef_

for i in range(n):
    x = X_test[i]

    y = F(x,C)

    round_y = round(y,6)

    print(round_y)

    
