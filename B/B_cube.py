
a = list(map(int,input().split()))
k = int(input())

s_a = list(set(a))
E_b1 = 0
E_sum = 0
#Pz0 = 0 # вероятность того что b_j == b_j-1
for i in range(len(s_a)):
    fr = 0
    for j in range(len(a)):
        if s_a[i] == a[j]:
            fr += 1
            
    E_b1 += s_a[i]*fr/len(a)
    
    #Pz0 = (fr/len(a))**2
    
    E_sum += (1-(fr/len(a)))*s_a[i]*fr/len(a)                        

print(E_b1 + (k-1)*E_sum)
