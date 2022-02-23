'''This code differs from dataCollectionBenchmarkAdded.py in that it does not dum target value, i.e., this code produces test data for the workolad with no label
'''
import subprocess

import sys

import pandas as pd
import numpy as np

argv =  sys.argv[1]
#filename = argv +".txt"


f_append = open('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/perf_recordTest.txt', 'a+')
#f = open('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/testrecTestData.txt', 'w+')

#df = pd.read_csv('perf_stat_record.txt', delimiter = '\t')


f1 = open('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/skycol_modified.txt', 'r')
features = f1.readlines()

n = input('How many times do you want to run for this workload?')
for iter in range(int(n)):
    for feature in features:
        subprocess.call(['perf', 'stat', '-o', '/home/am/Videos/perceptronmod/testcodesforworkloadvariants/testrecTestData.txt',  '-e', feature, '--', './'+argv])
        f3 = open('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/testrecTestData.txt', 'r')
        temp_lines = f3.readlines()
        for  temp_line in  temp_lines:
             if feature in  temp_line:
            #list_result.append(temp_line)
                temp_line = temp_line.split()
                temp_line[0] = temp_line[0].replace(",", "")
                f_append.write(temp_line[0]+'\t' ) 
            #print(temp_line[1] + '\t' + temp_line[0])
            
            
   
   
    f_append.write('\n')



#f_append.close()
print("Reading text file into csv file")
#df = pd.read_csv('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/perf_recordTest.txt', delimiter ='\t')
df = pd.read_csv('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/perf_recordTest.txt', delimiter ='\t')
print("Saving the csv file")

df.to_csv('/home/am/Videos/perceptronmod/testcodesforworkloadvariants/perf_recordTest.csv', index = None)


print (df.shape)
#print (df.head())
#print(df.iloc[1,0:301])


print("Intitializing parameters")

m, n = df.shape
print("Number of rows = " + str(m) + "\n Number of columns = "+ str(n))

#print(df.iloc[:,302])

X = df.iloc[1:m,range(n-1)]
#yframe = df.iloc[1:m, n-1]

x = np.array(X)
#x = np.where(np.max(x, axis=0)==0, x, x*1./np.max(x, axis=0))

print("X shape == ", X.shape) 
          
           

 
           
        





    
    
