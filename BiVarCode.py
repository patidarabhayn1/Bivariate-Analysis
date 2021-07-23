import math
import matplotlib.pyplot as mat

def mean(l):
    s=sum(l)
    c=len(l)
    mean=s/c
    return mean

def variance(l,m):
    s=0
    for i in l:
        s=s+(i-m)**2
    var=s/len(l) 
    return var  

def covariance(l1,m1,l2,m2):
    if(len(l1)!=len(l2)):
        print("Length of Lists is Not Same")
        return 0
    s=0
    for i in range(0,len(l1)):
        s=s+(l1[i]-m1)*(l2[i]-m2)
    covar=s/len(l1) 
    return covar

def correlation(covar,var1,var2):
    var1=math.sqrt(var1)
    var2=math.sqrt(var2)
    if( var1!=0 and var1!=0):
        corr=covar/(var1*var2)
    else:
        corr=0    
    return corr
