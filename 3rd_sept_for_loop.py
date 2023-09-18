#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1
a=range(1,11)
for i in a:
    print(i)


# In[6]:


#2
list=[1,2,3,4,5]
sum=0
for i in list:
    sum=sum+i
print(sum)


# In[5]:


#3
a=input("enter any character = ")
for i in a[::-1]:
    print(i)


# In[7]:


#4
a=int(input("enter any number = "))
fac=1
for i in range(1,a+1):
    fac=fac*i
print(fac)


# In[13]:


#5
num=int(input("enter any number ="))
for i in range(1,11):
    print(num,'x',i,'=',num*i)


# In[14]:


#6
list=[1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
for i in list:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("the no. of even numbers = ",even_count)
print("the no. of odd numbers = ",odd_count)


# In[19]:


#7
list=[1,2,3,4,5]
for i in list:
    a=i**2
    print(a)


# In[3]:


#8
a=input("enter the string =")
count=0
for i in a:
    count+=1
print(count)
    


# In[12]:


#9
a=[50,20,10,10,10]
sum=0
for i in a:
    sum=(sum+i)
    b=sum/len(a)
print(b)


# In[10]:


#10
a=int(input('Enter any number = '))
m,n=0,1
for i in range(a):
    print(m)
    m,n=n,m+n
    


# In[10]:


#11
list=[1,2,3,4,2,5,67,5,3]
my_list=[]
dup_list=[]
for i in list:
    if i not in my_list:
        my_list.append(i)
    elif i not in dup_list:
        dup_list.append(i)
print(dup_list)


# In[11]:


#12
a=int(input("enter the number = "))
for i in range(1,a+1):
    if i > 1:
        for num in range(2,i):
            if (i%num)==0:
                break
            else:
                print(num)


# In[ ]:


#13
a=input("enter the string = ")
b=a.lower()
vowels=set('aeoui')
count=0
for i in b:
    if i in vowels:
        count+=1
print(count)
        


# In[11]:


#14
matrix=[
    [2,4,6],
    [3,5,7],
    [9,7,5]
]
max_element=matrix[0][0]
for row in matrix:
    for element in row:
        if element>max_element:
            
            print(element)
    


# In[7]:


#15
list=[1,2,3,4,5,6,5,4,3,2]
n=int(input("enter the number which you want to remove = "))
for i in list:
    if i==n:
        list.remove(i)
print(list)


# In[22]:


#16
start_num = 1
end_num = 5

for multiplicand in range(start_num, end_num + 1):
    for multiplier in range(start_num, end_num + 1):
        product = multiplicand * multiplier
        print(f"{multiplicand} x {multiplier} = {product}")
    print()


# In[8]:


#17
fah_list=[40,50,66,70,80]
celsius=[]
for i in fah_list:
    celsius=[(i-32)*5/9]
    print(celsius,end='')  
print()


# In[20]:


#18
a1=[1,2,3,4,5,6,7,8,9]
a2=[2,4,6,8,10,11]
list=[]
for i in a1:
    if i in a2:
        list.append(i)
print(list)
        
            

            


# In[56]:


#19
a=int(input("enter the number"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()


# In[6]:


#20
a=int(input("enter any number = "))
b=int(input("enter any number = "))
gcd=1
for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD of numbers is = ",gcd)


# In[58]:


#21
a=[1,2,3,4,5,6,7,8,9,10]
b=sum(x for x in a)

print(b)


# In[23]:


#22
a=int(input("enter any number : "))
prime_fac=[x for x in range(1,a+1) if a%x==0 and all(x%i!=0 for i in range(2,x))]
print(prime_fac)


# In[27]:


#23
list=[1,2,2,3,4,4,4,4,5]
new_list=[x for x in list if list.count(x)==1]
print(new_list)


# In[6]:


#24
a=int(input("enter the limit = "))
palidromic_list=[i for i in range(a+1) if str(i)== str(i)[::-1]]
print(palidromic_list)


# In[2]:


#25
list=[[1],[2,3],[4,5,6]]
flatten_list=[b for x in list for b in x]
print(flatten_list)


# In[40]:


#26
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,4]
even_sum=sum(i for i in list if i%2==0)
odd_sum=sum(i for i in list if i%2!=0)
print("the sum of even numbers = ",even_sum)
print("the sum of odd numbers = ",odd_sum)


# In[34]:


#27
a=(range(1,11))
square_odd=[i**2 for i in a if i%2!=0]
print(square_odd)


# In[6]:


#28
keys=['jaskaran','python','pwskills']
values=[2,4,6]
resultant={keys[i]:values[i] for i in range(len(keys))}
print(resultant)


# In[43]:


#29
a="i am learning python from pwskills"
vowels='aeoui'
vowels_list=[x for x in a if x in vowels]
print(vowels_list)


# In[12]:


#30
list=['abc23','jas987','har567','iou098']
list_digit=[''.join(char for char in string if char.isdigit()) for string in list]
print(list_digit)


# In[3]:


#31
a=int(input("enter the limit of prime = "))
prime=[True]*(a+1)
prime[0]=prime[1]=False
for i in range(2,int(a**0.5)+1):
    if prime[i]:
        for b in range(i*i,a+1,i):
            prime[b]=False
prime_number=[i for i in range(2,a+1) if prime[i]]
print(prime_number)
        
    


# In[8]:


#32
limit=int(input ("enter the limit = "))
pythgorean_triplet=[(a,b,c) for a in range(1,limit+1)
                    for b in range(a,limit+1)
                    for c in range(b,limit+1)
                    if a**2 + b**2 == c**2]
print("the pythgorean_triplet = ",pythgorean_triplet)


# In[6]:


#33
a=[1,2,3,4,5]
b=[6,7,8,9,10]
combination=[(x,y) for x in a for y in b]
print(combination)


# In[16]:


#34
list=[12, 15, 17, 20, 12, 15, 22, 19, 20, 22,20]

Mean=sum(list)/len(list)
print("the mean of list is = ",Mean)

sorted_list=sorted(list)
median_index=len(sorted_list)//2
if len(sorted_list) % 2 == 0:
    median=(sorted_list[median_index - 1] + sorted_list[median_index]) / 2
else:
    median = sorted_list[median_index]
print("the median of list is = ",median)

number_count = {num: list.count(num) for num in list}
mode= [num for num, count in number_count.items() if count == max(number_count.values())]
print("the mode of list is = ",mode)


# In[12]:


#35
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = [[1]]
[pascals_triangle.append([1] + [pascals_triangle[row - 1][col - 1] + pascals_triangle[row - 1][col] for col in range(1, row)] + [1]) for row in range(1, num_rows)]
for row in pascals_triangle:
    print(row)


# In[6]:


#36
factorial=1
digit_sums = [sum(digit) for digit in factorial for factorial in [1, 1, 2, 6, 24, 120]]
for num, digit_sum in enumerate(digit_sums, start=1):
    print(f"Sum of digits for {num}! is {digit_sum}")


# In[37]:


#37
sentence=input("enter the sentence ")
word=sentence.split()
max_word=max((i for i in word),key=len)
print(max_word)


# In[26]:


#38
str=['bike','car','aeroplane','ship','bus','train']
list_vowel=[i for i in str if sum(1 for char in i.lower() if char in 'aeoui')>3]
print(list_vowel)


# In[5]:


#39
digit_sums = [sum(int(digit) for digit in str(i)) for i in range(1, 1001)]
total_sum = sum(digit_sums)
print("The sum of digits of numbers from 1 to 1000 is:", total_sum)


# In[5]:


#40
a=int(input("enter the limit : "))
prime_pal=[i for i in range(a+1) if all (i % n != 0 for n in range(2,int(i**0.5)+1) ) and str(i)==str(i)[::-1]]
print("The prime palindromic numbers are : ",prime_pal)



# In[ ]:




