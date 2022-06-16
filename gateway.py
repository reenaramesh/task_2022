import serial
import logging
import os
import time
import pymongo
import paho.mqtt.client as paho
from datetime import datetime
import re
import pandas

broker = "35.154.14.203"
"""ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

while True:
    while ser.in_waiting:
        data = ser.readline()
        # print(data)
        try:
            data1 = str(data.decode('utf8'))
            print(data1)
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            date = now.strftime("%d/%m/%Y")
            print(time)
            file_name = '/home/pi/Documents/Log_%s_%s_%s.csv' % (now.day, now.month, now.year)
            file = open(file_name, "a")
            try:

                if os.stat(file_name).st_size == 0:
                    file.write("DATE" + "," + "TIME" + "," + "DATA" + "\n")
                file.write(str(date) + "," + str(time) + "," + data1 + "\n")
                file.flush()
                print("saved")
                
                
                
 if x in d_id:
            num=''
            if x.isdigit():
                num= num+x
                    if len(num)>=2:
                        print(+num)

        while i> len(d_id): """
#with open(filename, encoding='utf8') as infile:
#file_name = (r'\Users\EXOZENIOT1\python_codes\Python\log1.txt')
#file_name = open("C:\Users\EXOZENIOT1\python_codes\Python\log1.txt", "r",encoding='utf8')

#file = open("C:\Users\EXOZENIOT1\python_codes\Python\log1.txt" , encoding='utf8')
#lines= file.readlines()
data = pandas.read_csv("C:/Users/EXOZENIOT1/python_codes/Python/log1.txt")

#get number of occurrences of the substring in the string
occurrences = data.count("VH006-0")

count=0
i=1
d_id = []
#for line in lines:
        #count+=1
        #print("lines:",lines)

        #d_id.append(line)
#print(d_id)
num=''
b=[]
li=[]


print("occur:", occurrences)


#for i in d_id:


        #for x in patterns_list:
            #print("loop:", re.search(x, val))
#val = re.findall(r"VH00[0-9]*[-]+[0-9]+[|]+[0-9]*",file)

#print("in between 1 and 4 times",  val)



"""
for  x in d_id:
      #y=int(x)

      num = re.findall(r'\d+', x)
      #if x.isdigit():

                #num= num+x
      #print("num:", num)
      if len(num)>2:
            print("num:",num)
            for m in num:
                n= int(m)
                print(n)
                if n>10:
                    b.append(n)
#a= b.reverse()
print("final list",b)
while i< len(b):

    value=b[i]-b[i-1]
    print(b[i], b[i-1])
    print(value)
    print("reversed value:", b)
    if ((b[i]>b[i-1])and(value> 12)):
        del b[i]

        #

    elif (value<0) :
        del b[i]
        print("final b:", b)

    else:
         i+=1"""

