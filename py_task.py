##l=[1,2,3,4]
##l[1],l[-1]=l[-1],l[1]
##print(l)
#--------------------
##for i in l:
##    if i%2!=0:
##        temp = l[i]
##        l[i]=l[-1]
##        l[-1]=temp
##        break
##print(l)

##l=[1,2,3]
##print(l[::-1])

##x = "10"+20+10
##print(x)

##k = [1,2,3]
##print(k*2)

##s="hello how are your"
##count=0
##for i in s.split(" "):
##    if len(i)>3:
##        count+=1
##print(count)
##l=[i for i in s.split(" ") if len(i)>3]
##print(len(l))
##a=(1,2,3,4)
##b=(5,6)
##print(id(a))
##print(id(b))
##b=a+b
##a=a+b
##print(a,b)
##print(id(a))
##print(id(b))
##l=[1,2,3]
##print(l*2)


##x='swetha'
##l=[]
##for i in range(len(x)):
##    if x[i] in ('a','e','i','o','u'):
##        l.append(x[:i])
##    
##print(l)
##import re
##res=re.split("['a','e','i','o','u']",x)
##print(res)
##x='sharnam'
##print(x.split('a'))
##keyword='thursday'
##x=keyword[:3]+keyword[3:]
##print(x)
##

##import re
##s=input("enter the num")
##x=re.search(r'^[456][\d]{3}[\-]?[\d]{4}[\-]?[\d]{4}[\-][\d]{4}$',s)
##if x:
##    print("valid")
##else:
##    print("invalid")

##s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##s1=''
##for i in range(0,len(s),4):
##     s1=s[i:i+4]
##     print(s1)
##


##x='swetha'
##if len(x)>2:
##     x1=x[:2]+x[-2:]
##print(x1)

##x="restart"
##x1=x[0]
##for i in x[1:]:
##     if i == x[0]:
##          x1+='$'
##     else:
##          x1+=i
##print(x1)

##x='xyz'
##y='abc'
##x1=x[:2]+y[2:]
##y1=y[:2]+x[2:]
##print(x1,y1)

##x=input("enter the string: ")
##if x[-3:]=='ing':
##     x+='ly'
##else:
##     x+='ing'
##print(x)

##a=['python','programming','language']
##x=len(a[0])
##x1=a[0]
##print(x,x1)
##for i in a:
##     if len(i)>x:
##          x=len(i)
##          x1=i
##print(x,x1)

##x='python'
##y=x[:-1]
##print(y)
##
##y=x[-1]+x[1:-1]+x[1]
##print(y)

##x='swetha'
##x1=''
##for i in range(len(x)):
##     if i%2==0:
##          x1+=x[i]
##print(x1)

##x='programming'
##x='my name is swetha swetha is a good girl'.split(" ")
##x1={}
##for i in x:
##     if i in x1:
##          x1[i]+=1
##     else:
##          x1[i]=1
##print(x1)

##x='bBhargav'
##x1={}
##for i in x:
##     x1[i]=x.count(i)
##print(x1)

##x='SswWeEtTHhAaa'
##x1={}
##for i in x:
##     if i in x1:
##          x1[i]+=1
##     else:
##          x1[i]=1
##print(x1)

##import random
##l=[2,4,6,5,9]
##l1=[]
##random.shuffle(l)
##l1.extend(l)
##print(l1)

##s='fariha'
##s1=[]
##for i in s:
##     s1.append(ord(i))
##s1.sort()
##x={chr(i):s.count(chr(i)) for i in s1}
##print(x)

##s='swethaa'
##s1=''
##for i in s:
##     s1=i+s1
##print(s[::-1])

##x=[2,5,7,10,8,9]
##def fun(x):
##     for i in range(len(x)):
##          for i in range(0,len(x)-1):
##               if x[i]>x[i+1]:
##                    x[i],x[i+1]=x[i+1],x[i]
##     return x[-2]
##print(fun(x))

##def fact(n):
##     if n == 1:
##          return 1
##     return n*fact(n-1)
##n=5
##print(fact(n))

##x="ojas innovative technologies"
##x1=[]
##count=0
##for i in range(len(x)):
##     if x[i] in 'aeiou':
##          x1.append(x[i])
##     else:
##          count+=1
##print(count,x1)

##print([1000]*2)
##import random
##l=[1,7,4,5,2,9,1]
##x=re.random.choice(l)
##print(x)

import pandas as pd
##df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[9,8,7]})
##x=df.to_dict()
##print(x)
##a=x['c'].values()
##print(a)
##y=pd.Series(data=[2,4,6],index=a)
##print(y.to_dict())
##print(df)

##df1 = pd.DataFrame([['a', 20], ['b', 25]],
##                   columns=['Name', 'Age'])
##df2 = pd.DataFrame([['w', 18], ['x',23]],
##                   columns=['Name1', 'Age1'])
##
##with pd.ExcelWriter('Deloitte.xlsx') as writer:
##    df1.to_excel(writer, sheet_name='first')
##    df2.to_excel(writer, sheet_name='second')


##def fun(n):
##    x=[0,1]
##    for i in range(n):
##        x.append(x[-1]+x[-2])
##    print(x)
##fun(10)

##import random
##x=[1,2,3,4,5,7]
##random.shuffle(x)
##print(x)

##x=[1,7,4,2,8,9]
##x.sort()
##print(x[-2])
##for i in range(len(x)):
##    for j in range(len(x)):
##        if x[i]<x[j]: # linear_sort
##            x[i],x[j]=x[j],x[i]
####        if x[j]>x[j+1]: bubble_sort,range(len(x)-1)
####            x[j],x[j+1]=x[j+1],x[j]
##        
##print(x[-2])
##
##x='swethaGudla'
##x1={}
##for i in x:
##    if i in x1:
##        x1[i]+=1
##    else:
##        x1[i]=1
##print(x1)
##for i in x:
##    x1[i]=x.count(i)
##print(x1)



##l1=[1,3,5,6,8]
##l2=[90,50,20,10]
##l3=[j for i in [l1,l2] for j in i]
##for i in range(len(l3)):
##    for j in range(len(l3)-1):
##        if l3[i]<l3[j]:
##            l3[i],l3[j]=l3[j],l3[i]
##print(l3)

##d = {1:"Hello prasad",
##       2:"hi",
##       3:"Wel come to Cisco network"}
##
##for i in d.keys():
##    for j in d.keys():
##        if len(d[i])<len(d[j]):
##            d[i],d[j]=d[j],d[i]
##print(d)

##s='cat,cat,rat,rat,hat,hat,pot,top'.split(',')
##for i in s:
##    count=0
##    for j in s:
##        if i == j:
##            count+=1
##        if count>1:
##            break
##    if count==1:
##        print(i)













