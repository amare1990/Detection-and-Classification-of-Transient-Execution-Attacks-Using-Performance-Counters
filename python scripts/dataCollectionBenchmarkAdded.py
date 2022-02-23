import subprocess

import sys

import pandas as pd
import numpy as np

argv =  sys.argv[1]
#filename = argv +".txt"


f_append = open('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/perf_stat_record.txt', 'a+')

#df = pd.read_csv('perf_stat_record.txt', delimiter = '\t')


f1 = open('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/skycol_modified.txt', 'r')
features = f1.readlines()

n = input('How many times do you want to run for this workload?')
for iter in range(int(n)):
    for feature in features:
        subprocess.call(['perf', 'stat', '-o', '/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/testrec.txt',  '-e', feature, '--', './'+argv])
        f3 = open('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/testrec.txt', 'r')
        temp_lines = f3.readlines()
        for  temp_line in  temp_lines:
             if feature in  temp_line:
            #list_result.append(temp_line)
                temp_line = temp_line.split()
                temp_line[0] = temp_line[0].replace(",", "")
                f_append.write(temp_line[0]+'\t' ) 
            #print(temp_line[1] + '\t' + temp_line[0])
            
            
    if argv == 'spectre_v1_pht_sa': f_append.write(str(1))
    elif argv == 'spectre_v1_btb_sa': f_append.write(str(2))
    elif argv == 'spectre_v1_btb_ca': f_append.write(str(3))
    elif argv == 'spectre_v4': f_append.write(str(4))
    elif argv == 'unmitigated': f_append.write(str(5))  # Unmitigated  = Benign workload found in /build/benchmark/spectre_v1 
    #else: f_append.write(str(10))  
   
    f_append.write('\n')



#f_append.close()
print("Reading text file into csv file")
df = pd.read_csv('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/perf_stat_record.txt')
print("Saving the csv file")

df.to_csv('/home/am/Desktop/Compark Project and Report/safeside-main/build/benchmarks/spectre_v1/perf_stat_record.csv', index = None)


print (df.shape)
#print (df.head())
#print(df.iloc[1,0:301])


print("Intitializing parameters")

m, n = df.shape
print("Number of rows = " + str(m) + "\n Number of columns = "+ str(n))

#print(df.iloc[:,302])

X = df.iloc[1:m,range(n-1)]
#X = X/X.max()
yframe = df.iloc[1:m, n-1]

x = np.array(X)
x = np.where(np.max(x, axis=0)==0, x, x*1./np.max(x, axis=0))
#if x[:,:]!=0:
 #  x = x/(np.max(x, axis=0))
y = np.array(yframe)
y = y.reshape((m-1), 1)

print("X shape == ", X.shape)
print("y shape= ", y.shape)





           
          
           

 
           
        





    
    
