n1=int(input("enter first numbers: "))
n2=int(input("enter second numbers: "))
n3=int(input("enter third numbers: "))

if(n1>=n2 and n2>=n3):
    print("n1 is greatest",n1)
elif(n2>=n3):
    print("n2 is greatest",n2)  
else:
    print("n3 is greatest",n3)      