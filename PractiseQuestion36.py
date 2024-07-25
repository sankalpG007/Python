def cal_fun(n):
    if(n==0):
        return 0
    
    return cal_fun(n-1) + n

sum=cal_fun(7)
print(sum)