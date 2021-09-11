print("nhập vào 1 số")
n=int(input())
flag= true
if ( n < 2):
    flag = false
elif (n == 2):
    flag = true
if ( n % 2 == 0):
    flag = false
else:
    for i in range(3,n,2):
        if  (n % i == 0 ):
            flag=false
if flag == false
    print(n,"là số nguyên tố")
else
    print( n, "không phải")