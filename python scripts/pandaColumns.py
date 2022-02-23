'''
This code produces important features for each workload
However, the indices are manually collected from the output of trainaccuracyAndPearsonCFBenchmarkAdded.py
'''
import pandas as pd
import csv

v1_pht_sa_indices = [12, 274, 273, 257, 251, 79, 65, 277, 34, 21, 78, 276, 72, 301, 112, 275, 229, 121, 233, 119, 0, 293, 200, 189, 136, 210]
v1_btb_sa_indices_pos = [125, 244, 234, 281, 241, 203, 133,  79,  16,  36, 207, 222,  29,  11,  24,  44]
v1_btb_sa_indices_neg = [275, 274, 154 ]

v1_btb_ca_indices_pos = [206, 229, 251, 125, 170, 252, 188, 248, 210, 145]
v1_btb_ca_indices_neg = [118, 283, 163, 157,  14, 298,   9]

v4_indices_pos = [67, 244, 268,   4,  15]
v4_indices_neg = [149, 221,  20,  45,  38, 121, 254]
#col = v1_pht_sa_indices

#f1 = open("/home/am/Videos/perceptronmod/v1_pht_sa_ImportantFeatures.csv", 'w')
#writer = csv.writer(f1)


df = pd.read_csv('/home/am/Videos/perceptronmod/perf_stat_record.csv')
'''
for col in df.columns[v1_pht_sa_indices]:
    print(col)
    #writer.writerow(col +','+str(v1_pht_sa_indices))
    
print("-ve p coeff  =\n", df.columns[278])

for col in df.columns[v1_btb_sa_indices_neg]:
    print(col)
    #writer.writerow(col +','+str(v1_pht_sa_indices))
'''
for col in df.columns[v4_indices_neg]:
    print(col)
