##def fact(x):
##    if x==0:
##        return 1
##    else:
##        return x*fact(x-1)
##x=5
##print(fact(x))
##
##n=5
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print(fact)

##n=int(input("enter the num"))
##sum = n
##temp = 0
##while sum:
##    x=sum%10
##    temp=temp+x**len(str(n))
##    sum = sum//10
##if n == temp:
##    print("yes")
##else:
##    print("no")

##n=int(input())
##if n > 1:
##    for i in range(2,n):
##        if n%i==0:
##            print("not")
##            break
##    else:
##        print("yes")

##l=1
##u=10
##for i in range(l,u+1):
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        print(i)

##def fib(x,y):
##    for i in range(10):
##        print(x)
##        x,y=y,x+y
##fib(0,1)

##l=[0,1,1,1,0,0]
##for i in range(len(l)):
##    if l[i]==0:
##        p=i
##        while p:
##            l[p],l[p-1]=l[p-1],l[p]
##            p-=1
##print(l)


##s="swethaGudla"
##s1={}
##for i in s:
##    if i in s1:
##        s1[i]+=1
##    else:
##        s1[i]=1
##print(s1)


##s=[1,2,3,4,1,4,2]
##s1=[]
##for i in s:
##    if i not in s1:
##        s1.append(i)
##print(s1)

from functools import reduce
x = reduce(lambda x,y: x+y, [47,11,42,13])
print(x)

def fib(a,b):
    for i in range(10):
        
       
        a,b=b,a+b
        print(a)
        
fib(1,0)
    

    


