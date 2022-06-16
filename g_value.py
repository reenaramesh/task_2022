''''
l = [12,21,32,58]
n= len(l)
for i in range(n) :
    l[i] = l[i-2]-l[i]
print(l)
'''

list1 = [10, 1, 45, 6, 9, -35, 0]
t = len(list1)

for i in range(t):
    for j in range(t - i - 1):  #####(t-i-1)
        if list1[j] > list1[j + 1]:
            temp = list1[j + 1]
            list1[j + 1] = list1[j]
            list1[j] = temp

print(list1)


# Function to delete elements
def deleteElements(arr, n, k):
    # create an empty stack st
    st = []
    st.append(arr[0])

    # index to maintain the top
    # of the stack
    top = 0
    count = 0

    for i in range(1, n):

        # pop till the present element
        # is greater than stack's top
        # element
        while (len(st) != 0 and count < k
               and st[top] > arr[i]):
            st.pop()
            count += 1
            top -= 1

        st.append(arr[i])
        top += 1

    # print the remaining elements
    for i in range(0, len(st)):
        print(st[i], " ", end="")


# Driver code
k= 1
arr = [743, 23000, 608 , 23534, 253, 35647 ]
deleteElements(arr, len(arr), k)


##############################
l = [100, 250, 35461, 2566, 255]
n = len(l)
for i in l:
    for j in range(n - i -1):
        if l[j] > l[j+1]:
            a = l[j] - l[j+1]
            if l[j+1] > 2000:
                b =l[j+1]
                print(b)
                del(b)

print(l)

########################


Alist = [631,652,611,300]
# Given list
print("Given list : ",Alist)
# Using set and map
if all(str(i)[0] == str(Alist[0])[0] for i in Alist):
   print("All elements have same first digit")
else:
   print("Not all elements ,have same first digit")


##################################

a = [220,215, 20000, 2589, 321]     # your original list
b = []           # Empty list that will contain final product

for i in range(len(a)):
    if len(b) == 0:       # if the list is empty, we add first item from 'a' (In our example, it'll be 2)
        b.append(a[i])
    else:
        if a[i] > b[len(b)-1]:
            x = a[i] > b[len(b)-1]
            print(a[len(b)-1])
            if x >2000:

                del(a[len(b)-1])
                #or a[i] < b[len(b)-1]-7:   # for every value of a, we compare the last digit from list b
                b.append(a[i])
                print(b)


###############



a=[18020,1200,18025,800000, 200,18030,18035,500,9000000,1, 1080,18039,
750,18040,18032,18080,150000,18085]

#a=[250,252,280,230,258,300]
print("complete list",a)
b=[]
i=1
while i<len(a):

    value=a[i]-a[i-1]

    print(a[i], a[i-1])
    print(value)
    if ((value < 0)|(value>a[i-1])):
            b.append(a[i])
            a.remove(a[i])

    else:
            i+=1
            #a.remove(a[i])
print("after deletion",a)
print("deleted values",b)


a = [2, 5, 6, 12, 21, 25, 32, 41]     # your original list
b = []           # Empty list that will contain final product

for i in range(len(a)):
    if len(b) == 0:       # if the list is empty, we add first item from 'a' (In our example, it'll be 2)
        b.append(a[i])


        if a[i] > b[len(b)-1]: #or a[i] < b[len(b)-1]:   # for every value of a, we compare the last digit from list b
            b.append(a[i])
print(b)

########### USING DIFFERENCE  VALUE LOGIC ###########

a = [12,20,220,215, 20000,125,  2589, 321, 320,315, 40000,125,  2589, 321, 785,635,
     256,451,552,1600,1200,21890,60, 122, 220,215, 20, 66000,125,  2589, 321, 320,315, 20000,125,
     2589, 321, 785,635, 256,451,205,21,552,1600,1200,21890,12]
i=1
while i<len(a):
    if(a[i]-a[i-1] > 1000):
        a.remove(a[i])
    else:
        i+=1
print(a)

#######################################

"""
#a = [12,20,220,215, 20000,125,  2589, 321, 320,315, 40000,125,  2589, 321, 785,635,
   #  256,451,552,1600,1200,21890,60, 122, 220,215, 20, 66000,125,  2589, 321, 320,315, 20000,125,
    # 2589, 321, 785,635, 256,451,205,21,552,1600,1200,21890,12]

a= int(input("enetr no of  values:"))
l =[]
for i in range(0,a):
    b= int(input())
    l.append(b)
i=1
while i<len(l):
    if(l[i]-l[i-1] > 1000):
        l.remove(l[i])
    else:
        i+=1
print(l)

##################################################

a= int(input("enetr no of  values:"))
l =[]
for i in range(0,a):
    b= int(input())
    l.append(b)
i=1
while i<len(l):
    if(l[i]-l[i-1] > 1000):
        l.remove(l[i])
    else:
        i+=1
print(l)

############ USING 1ST 3DIGIT SIMILARITY LOGIC ##########

# take input
num = int(input('Enter any Number: '))

# get the first digit
while (num >= 10):
    num = num // 100

# printing first digit of number
#print('The first digit of number:', num)

"""


import math

def dig(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)
#num=[25441,575454,164454,514254]
print(dig(4325, 3))

import math

num=[25441,575454,164454,514254]
for i in num:
    value = i // 10 ** (int(math.log(i, 10)) - n + 1)
    print(value)


print("done ########################################################################")


def fun(mydict):
 x= mydict.keys()
 y= mydict.values()
 a= list(x)
 b= list(y)
 #print("original consumption:", b)
 l1=[]
 i=1
 b.reverse()
 n=len(b)
 while 1<n:

         value= b[i-1]-b[i]
         print(b[i-1],b[i])
         print(value)

         print("reversed list:",b)
         if  ((value < 0)|(value<b[i-1])):
                 b.remove(b[i-1])
                 l1.append(b[i-1])

         else:
                 i+=1

                 return l1
                 #print(l1)

dict={110:2656,102:200, 103:2700,104:36, 105:2775,106:2800,109:2856}


print(fun(dict))