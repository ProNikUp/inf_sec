#
import math

def hash(n):
    for i in range(len(n)):
        p1 = (n[i]+n[i])*n[i]
        p2 = (n[i]+n[i])*n[i]*p1
        p3 = (n[i-1]+n[i-1])*n[i-1]*p2*p1
        F = (p1+p2)*p3/((n[i-1]+n[i-1])*n[i-1]*p2*p1)
        F1 = p1*p2+p3+F
        F2 = math.log(F)**math.log(math.pi)
        F3 = math.exp(F2)
        F4 = F3 * F
        F5 = int(F4)
    return F5  
 
print(hash([8,6,7,4]))
