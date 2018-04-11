import os
import re
import sys
import glob
import numpy as np
import csv as csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

nrApp = 10
HW1 = 20
HW2 = 6

AT = 50
DT = 15
SD = 5
SUFFIX = "4.4"

prev_dir = os.getcwd()

app_dir = prev_dir + "/_AT" + str(AT) + "_DT" + str(DT) + "_SD" + str(SD) + "_" + SUFFIX  
#app_dir = prev_dir + "/SampleOpenVX"


easy_dir = app_dir + "/DmEasy/resR"
fss_dir = app_dir + "/DmDSS/resR"
resp1 = "resRSW"
resp2 = "resROPT" 
resb = ".txt"
df = pd.DataFrame()

for x in xrange(1, HW1):
	cur_dir = easy_dir
	os.chdir(cur_dir)
	filename = resp1 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["i"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df = pd.concat([df, data], axis=1)

	cur_dir = fss_dir
	os.chdir(cur_dir)
	filename = resp1 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["d"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df = pd.concat([df, data], axis=1)
print df

# Save
os.chdir(app_dir)
df.to_csv('ThroughputSW.txt', header=True, index=False, sep='\t')

# Plot
os.chdir(app_dir)
xaxis = []
for x in xrange(1,HW1):
	xaxis.extend([1.5*x-1, 1.5*x-0.5])
	
df.boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis,
	widths = 0.4)

plt.title("Throughput Improvement for Intuitive and DSS", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.xlim((0,(HW1-1)*1.5))
plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
plt.ylim((0,15))
plt.savefig('ThSW_Intuitive.png')
plt.clf()




df2 = pd.DataFrame()

for x in xrange(1, HW2):
	cur_dir = easy_dir
	os.chdir(cur_dir)
	filename = resp2 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["i"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df2 = pd.concat([df2, data], axis=1)

	cur_dir = fss_dir
	os.chdir(cur_dir)
	filename = resp2 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["d"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df2 = pd.concat([df2, data], axis=1)
print df2

# Save
os.chdir(app_dir)
df2.to_csv('ThroughputOPT.txt', header=True, index=False, sep='\t')

# Plot
os.chdir(app_dir)
xaxis = []
for x in xrange(1,HW2):
	xaxis.extend([1.5*x-1, 1.5*x-0.5])
	
df2.boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis,
	widths = 0.4)

plt.title("Throughput Achievement for Intuitive and DSS", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.xlim((0,(HW2-1)*1.5))
plt.ylabel('(Th(it) / (Th(App-Opt))', fontsize=16)
plt.ylim((0,1))
plt.savefig('ThAPPOPT_Intuitive.png')
plt.clf()




# AppOPT vs DSS

opt_dir = app_dir + "/OPT"
opt_prev = "AppOPT"
opt_back = ".txt"
sw_dir = app_dir + "/pureSW"
sw_file =  "SWresult.txt"
dfsw = pd.DataFrame()
dfopt = pd.DataFrame()
df3 = pd.DataFrame()

cur_dir = sw_dir
os.chdir(cur_dir)
data = pd.read_csv(sw_file, sep=" ", header=None)
data.columns = ["i", "icomp", "icomm", "icomm2", "itime"]
data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
dfsw = pd.concat([dfsw, data], axis=1)

for x in xrange(1, HW2):
	cur_dir = opt_dir
	os.chdir(cur_dir)
	filename = opt_prev + str(x) + opt_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["i"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfopt = pd.concat([dfopt, data], axis=1)
	df3["i"+index] = dfopt["i"+index] / dfsw["i"]

	cur_dir = fss_dir
	os.chdir(cur_dir)
	filename = resp1 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["d"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df3 = pd.concat([df3, data], axis=1)
print df3

# Save
os.chdir(app_dir)
df3.to_csv('ThroughputOPTSW.txt', header=True, index=False, sep='\t')

# Plot
os.chdir(app_dir)
xaxis = []
for x in xrange(1,HW2):
	xaxis.extend([1.5*x-1, 1.5*x-0.5])
	
df3.boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis,
	widths = 0.4)

plt.title("Throughput Achievement for App-OPT and DSS", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.xlim((0,(HW2-1)*1.5))
plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,1))
plt.savefig('ThSW_AppOPT.png')
plt.clf()


# DMOPT vs DSS
DMopt_dir = app_dir + "/OPT"
DMopt_prev = "DmOPT"
DMopt_back = ".txt"
dfDMopt = pd.DataFrame()
df4 = pd.DataFrame()

for x in xrange(1, HW2):
	cur_dir = DMopt_dir
	os.chdir(cur_dir)
	filename = DMopt_prev + str(x) + DMopt_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["i"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfDMopt = pd.concat([dfDMopt, data], axis=1)
	df4["i"+index] = dfDMopt["i"+index] / dfsw["i"]

	cur_dir = fss_dir
	os.chdir(cur_dir)
	filename = resp1 + str(x) + resb
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["d"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	df4 = pd.concat([df4, data], axis=1)
print df4

# Save
os.chdir(app_dir)
df4.to_csv('ThroughputDMOPTSW.txt', header=True, index=False, sep='\t')

# Plot
os.chdir(app_dir)
xaxis = []
for x in xrange(1,HW2):
	xaxis.extend([1.5*x-1, 1.5*x-0.5])
	
df4.boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis,
	widths = 0.4)

plt.title("Throughput Achievement for Domain-OPT and DSS", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.xlim((0,(HW2-1)*1.5))
plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,1))
plt.savefig('ThSW_DmOPT.png')
plt.clf()
