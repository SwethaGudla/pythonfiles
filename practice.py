##lower = int(input("enter the lowernum"))
##upper = int(input("enter the uppernum"))
##for i in range(lower,upper+1):
##    if i>1:
##    
##        for j in range(2,i):
##            if i%j==0:
##            
##                break
##        else:
##            print(i)
                
####################################################################

##x='dileep'
##x1={}
##for i in x:
##    x1[i]=x.count(i)
####    if i in x1:
##        
####        x1[i]+=1
####    else:
####        x1[i]=1
##print(x1)

#############################################################

##s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##s1=''
##for i in range(0,len(s),4):
##    s1=s[i:i+4]
##    print(s1)
##    

###############################################################

##def palindrome(num):
##    temp = num
##    res=0
##    while temp:
##        d = temp%10
##        res = res*10+d
##        temp = temp//10
##    #return res
##    if num  == res:
##        print("palindrome")
##    else:
##        print("not palindrome")
##num = int(input("enter the num"))
##palindrome(num)

#######################################################################

##def armstrong(num):
##    temp = num
##    res = 0
##    while temp:
##        d = temp%10
##        res = res+d**len(str(num))
##        temp = temp//10
##    #return res
##    if num == res:
##        print("armstrong")
##    else:
##        print("not armstrong")
##num = int(input("enter the num"))
##armstrong(num)

###########################################################
    
##def fact(num):
##    if num == 0:
##        return 1
##    else:
##        return num*fact(num-1)
##print(fact(5))

##########################################################

##def fact(n):
##    for i in range(1,n):
##        n=n*i
##    print(n)
##fact(5)

###########################################################

##def panagram(s):
##    count=0
##    for i in range(97,97+26):
##        if chr(i) in s:
##            count+=1
##    if count == 26:
##        print("panagram")
##    else:
##        print("not panagram")
##s='abcdefghijklmnopqrstuvwxyz'
##panagram(s)

###############################################################

##def anagram(s1,s2):
##    if sorted(s1)==sorted(s2):
##        print("anagram")
##    else:
##        print("not anagram")
####s1='listen'
####s2='silent'
##s1=(input("enter the string1"))
##s2=(input("enter the string2"))
##anagram(s1,s2)

###############################################################

##def anagram(s1,s2):
##    count=0
##    for i in range(len(s1)):
##        if s1[i] in s2:
##            count+=1
##    if len(s1)==count:
##        print("anagram")
##    else:
##        print("not anagram")
##s1=(input("enter the string1"))
##s2=(input("enter the string2"))
##anagram(s1,s2)

##############################################################

##s = 'SwEtHaGuDlA'
##u=0
##l=0
##up=""
##low=""
##for i in s:
##    if i.isupper():
##        u+=1
##        up = up+i
##        
##    else:
##        l+=1
##        low = low+i
##print(up,"-",u)
##print(low,"-",l)

##def binarysearch(lst,key):
##    l=0
##    u=len(lst)-1
##    while l<=u:
##        mid=(l+u)//2
##        if lst[mid]==key:
##            return mid
##        elif lst[mid]<key:
##            l=mid+1
##        elif lst[mid]>key:
##            u=mid-1
##    return -1
##lst=[1,32,5,6,7,9,78]
##for i in range(len(lst)):
##    for j in range(len(lst)):
##        if lst[i]<lst[j]:
##            lst[i],lst[j]=lst[j],lst[i]
##print(lst)
##key=int(input("enter the num"))
##print(binarysearch(lst,key))
        

##import copy
##old_lst = [[1,2,3,4],[6,7,8,9]]
##new_lst = copy.copy(old_lst)
##old_lst[1][1]=9
##print('original copy',old_lst)
##print('shallow copy:',new_lst)
##
##
##import copy
##old_lst = [[1,2,3,4],[6,7,8,9]]
##new_lst = copy.deepcopy(old_lst)
##old_lst[1][1]=9
##print('original copy',old_lst)
##print('deep copy:',new_lst)

##class Employee:
##    age=18
##    
##    def __init__(self,name):
##        self.name=name
##        
##    def display(self):
##        print(f'{self.name},{self.age}')
##        
##    @classmethod
##    def clasmethod(cls,name):
##        cls.name=name
##        print(f'{cls.name},{cls.age}')
##        
##    @staticmethod
##    def staticmethod(age):
##        if age>18:
##            return f'age={age} is greaterthan 18'
##        else:
##            return f'age={age} is lessthan 18'
##emp=Employee('swetha',)
##emp.display()
##
##emp.clasmethod('parsad')
##print(emp.staticmethod(int(input("enter the age"))))
##
##s='copyassignment'
##
##for i in s:
##    if i=='a' or i=='c':
##        continue
##    else:
##        print(i)
###################################################################
##from datetime import date
##x=date(2021,2,15)
##y=date(2022,3,28)
##print(y-x)
#####################################################
##def diff(n):
##    if n<17:
##        return 17-n
##    else:
##        return (n-17)*2
##n=int(input("enter the number"))
##print(diff(n))
##################################################
##def finding(num):
##    for i in range(1,100):
##        if num == i:
##            print("found")
##            break
##    else:
##        print("not found")
##num = int(input("enter the num"))
##finding(num)

##lst1=[1,2,3,4,5]
##lst2=[10,20,30,40,50]
##lst3=[j for i in [lst1,lst2] for j in i]
##print(lst3)

##class Singleton:
##   __instance = None
##   @staticmethod 
##   def getInstance():
##      """ Static access method. """
##      if Singleton.__instance == None:
##         Singleton()
##      return Singleton.__instance
##   def __init__(self):
##      """ Virtually private constructor. """
##      if Singleton.__instance != None:
##         raise Exception("This class is a singleton!")
##      else:
##         Singleton.__instance = self
##s = Singleton()
##print(s)
##s2 = Singleton()
##print(s2)
##s = Singleton.getInstance()
##print s
##
##s = Singleton.getInstance()
##print s


####ls = ['aa','aa','bb','cc']
##lst={i:ls.count(i) for i in ls}
##for i in ls:
##    if i in lst:
##        lst[i]+=1
##    else:
##        lst[i]=1
##print(lst)
##
##
##self.assert(rand(e_l,h_l,m_l),100)
##self.assert(mail(regx,ojas-it.com))
##self.assert(option(sublist),4)
##
##import smtplib
##content="HelloWorld"
##mail=smtplib.SMTP('smtp.gmail.com',587)
##mail.ehlo()
##mail.starttls()
##sender='bhargavk950@gmail.com'
##receipient='muday3114@gmail.com'
##mail.login('bhargavk950@gmail.com','....pwd....')
##header='To:'+receipient+'\n'+'From:'\
##+sender+'\n'+'subject:testmail\n'
##content=header+content
##mail.sendmail(sender,receipient, content)
##mail.close()
##
##
##


##import unittest
##class TestStringMethods(unittest.TestCase):
##    def setUp(self):
##        print("It executes before each test case")
##    def test_upper(self):
##        self.assertEqual('Hello world'.upper(), 'HELLO WORLD')
##    def test_Email(self):
##        self.assertTrue(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",'swetha@gmail.com')
##    def test_is_upper(self):
##        self.assertTrue('FOO'.isupper())
##        self.assertFalse('Foo'.isupper())
##    def test_add(self):
##        self.assertEqual(2+3,5)
##    def tearDown(self):
##        print('It executes after test case')
##if __name__ == '__main__':
##    unittest.main()


##def sum(x,y):
##
##    try:
##        z=x/y
##        print(z)
##    except ZeroDivisionError as ex:
##        print(ex)
##sum(10,10)

##user='aaabbsss'
##lst=[]
##for i in user:
##    if (i,user.count(i)) not in lst:
##        lst.append((i,user.count(i)))
##for i in lst:
##    print(i[0],i[1])
    

##s='aabbbbcs'
##s1={}
##for i in s:
##    if i in s1:
##        s1[i]+=1
##    else:
##        s1[i]=1
##print(s1)

##s='aabbbbcs'
##s1={}
##for i in s:
##    s1[i]=s.count(i)
##print(s1)

##def fact(n):
##    if n == 1:
##        return 1
##    else:
##        return n*fact(n-1)
##print(fact(5))

##def fact(n):
##    for i in range(1,n):
##        n=n*i
##    print(n)
##fact(5)
##########################################################
##def validate(fun):
##    def authorizedUsers(user):
##        l = ['swetha','Gudla']
##        if user in l:
##            return fun(user)
##        else:
##            return "I am sorry, you are not authorized"
##    return authorizedUsers
##@validate
##def fileopen(user):
##    return f"Hello {user}. Your file is opening"
##print(fileopen('Swetha'))
            

##def array_frequency(Input_Array):
##  dict_count = {} # Empty Dictionary to assign array count
##  for i in set(Input_Array): # set is for remove duplicate elements
##    count = Input_Array.count(i) # Each element count 
##    try:
##      dict_count[count].append(i) # appending count as a key and element as a value
##    except:
##      dict_count[count]=[i] # elements contain with single count 
##  Output_Array=[]  # Empty array for printing sorted array 
##  for i in sorted(dict_count):  # Iteratin sorted Dictionary keys , i.e count
##    for j in sorted(dict_count[i],reverse=True):  # Iteratin values and then reverse the array
##      Output_Array.extend([j]*i)  # Multiplying Elements with count 
##  return Output_Array[::-1]   # Final Array in reverse order
##Input_Array=[0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1] # Given input 
##print(array_frequency(Input_Array)) # calling function with array
##

##def input(a):
##    dc = {}
##    for i in set(a):   
##        c = a.count(i)       
##        try:
##            dc[c].append(i)           
##        except:
##            dc[c]=[i]
##            
##    output=[]
##    for i in sorted(dc):
##        
##        for j in sorted(dc[i],reverse=True):
##            output.extend([j]*i)
##    return output[::-1]
##a=[0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
##print(input(a))


##def fact(n):
##   if n <= 1:
##       return 1
##   else:
##       return (fact(n-1)+fact(n-2))
##n=int(input("enter te num"))
##for i in range(n):
##    print(fact(i))

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
   for j in range(C):
      print(matrix[i][j], end = " ")
   print()
















