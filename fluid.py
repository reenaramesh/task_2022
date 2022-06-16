"""a=[18020,1200,18025,800000, 200,18030,18035,500,9000000]
#a=[250,252,280,230,258,300]
print("complete list",a)
b=[]
i=1
n= len(a)
#while i<n:

v= a[n-1]-a[n-2]

i-=1
print("last", a[n - 1], a[n - 2])

if (v<1000):
        print("ok")
elif v > a[n-2]:
        a.remove(a[n-2])
        b.append(a[n-2])
else:
        i+=1
print(a)
print(b)


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
"""

"""
def data(**mydict):
x= mydict.keys()
y= mydict.values()
a= list(x)
b= list(y)

i=1
#while i<len(b):
   #     if ((b[n-1]-b[n-2]) < 0)|(b[n-1]-b[n-2]>b[i-1])):
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car)
print(a)"""

"""
def fun(marks):
 x= marks.keys()
 y= marks.values()
 a= list(x)
 b= list(y)

 i=1
 while i<len(b):
        if b[i] >200:
                i+=1
                print("got")
                break
        else:
                print("no")
                break

#mark = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#mark1 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 125, 'Pierre Cox': 190}
mark2 = {'Cierra Vega': 200, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

#print(fun(mark))
#print(fun(mark1))
print(fun(mark2))

"""
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

mydict = { "device_id": device_id, "consumption": consumption1, "date": datetime.datetime.now()}