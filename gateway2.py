# to initialize multiple lists
SC19201, SC19301,  SC19401, SC19501, SC19601, SC19701, SC19801, SC19901, SC19002, SC19102, SC19202, SC19302, SC19402, SC19502, SC19602, SC19702, SC19802, SC19902, SC19604, SC19704, SC19804, SC19904, SC19003, SC19103, SC19203, SC19303 ,SC19403, SC19503,SC19603, SC19703, SC19803, SC19903, SC19004 ,SC19104, SC19204, SC19304, SC19404, SC19504 = ([],) * 38

# printing lists
print("The initialized lists are : ")
print("List 1 : " + str(SC19201))
print("List 2 : " + str(SC19301))
print("List 3 : " + str(SC19401))
print("List 4 : " + str(SC19501))

import re

"""sp= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if (sp.search(con)==True):
  del con"""\



"""
import time
from datetime import datetime

f= open(r'C:\Users\EXOZENIOT1\Downloads\water logs_23_5_2022.xl - water logs_23_5_2022.xl.csv', "r", encoding='utf8')
for i in f:

    data = f.readline()

    #data1 = data.decode('utf8')
    # print(data1)
    #data2 = data1
    dev_type = data[0:-1]
    if len(dev_type) > 4:
       # ind = data[4:8]
       # print(ind)
        pos = data.find('-')
        pos1 = data.find('|')
        com= data.find('SSB')
        coma= data.find(',')


        #time = now.strftime("%H:%M:%S")
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%Y")
        data_type = data[pos+1:pos1]
        #val = dev_type[pos1+1:]
        #device_id = data[com:pos]

        #date = now.strftime("%d/%m/%Y")
        #print("Received_Data = " + dev_type)
        #print("Device_ID = " + device_id)
        #print("ping_val = " + data_type)
        #print("Consumption_value = " + val + " " + "ltr")
        #print("Date = " + date + " " + "Time = " + time + "\n")
        l_id = []
        l_con=[]
        #al = value
        val = dev_type[pos1 + 1:]
        device_id = data[com:pos]
        last= val[:]
        #print(device_id , last)


        count = 0
        count+=1
        l_id.append(device_id)
        #print(l_id)

#print(list(device_id), list(last))
        #for device_id in data:
        #if value < val[-1]:
          # print("ok")
"""