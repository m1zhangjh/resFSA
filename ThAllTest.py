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

nrApp = 24
HW = 20
HW2 = 11

AT = 50
DT = 15
SD = 5
SUFFIX = "2.934"

prev_dir = os.getcwd()

app_dir = prev_dir + "/_AT" + str(AT) + "_DT" + str(DT) + "_SD" + str(SD) + "_" + SUFFIX  
#app_dir = prev_dir + "/SampleOpenVX25"

sw_dir = app_dir + "/pureSW"
easy_dir = app_dir + "/DmEasy"
opt_dir = app_dir + "/OPT"
dss_dir = app_dir + "/DmDSS_SS/Weight"
optAll_dir1 = app_dir + "/OPT/HW"
optAll_dir2 = "/Res"

#Read pureSW Result
dfSW = pd.DataFrame()
file_sw = "SWresult.txt"
cur_dir = sw_dir
os.chdir(cur_dir)
data = pd.read_csv(file_sw, sep=" ", header=None)
data.columns = ["sw", "icomp", "icomm", "icomm2", "itime"]
data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
dfSW = pd.concat([dfSW, data], axis=1)


file_prev = "resultHW"
file_back = ".txt"
#Read Result for OPT, DmEasy, DSS
dfOPT = pd.DataFrame()
dfEASY = pd.DataFrame()
dfDSS = {}
weight = [0,1,2,5]
for y in weight:
	dfDSS[y] = pd.DataFrame()
for x in xrange(1, HW):
	cur_dir = opt_dir
	os.chdir(cur_dir)
	filename = file_prev + str(x) + file_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["o"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfOPT = pd.concat([dfOPT, data], axis=1)

	cur_dir = easy_dir
	os.chdir(cur_dir)
	filename = file_prev + str(x) + file_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["i"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfEASY = pd.concat([dfEASY, data], axis=1)

	for y in weight:
		cur_dir = dss_dir + str(y)
		os.chdir(cur_dir)
		filename = file_prev + str(x) + file_back
		data = pd.read_csv(filename, sep=" ", header=None)
		index = str(x)
		data.columns = ["d"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
		data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
		dfDSS[y] = pd.concat([dfDSS[y], data], axis=1)

dfOPTALL = pd.DataFrame()
rOPTALL = pd.DataFrame()
oOPTALL = pd.DataFrame()
dfTemp = {}
dfTempR = {}
dfTempO = {}
for x in xrange(1, HW):
	dfTemp[x] = pd.DataFrame()
	dfTempR[x] = pd.DataFrame()
	dfTempO[x] = pd.DataFrame()
for x in xrange(1, HW2):
	cur_dir = optAll_dir1 + str(x) + optAll_dir2
	os.chdir(cur_dir)
	for z in xrange(0, nrApp):
		filename = "app" + str(z) + ".txt"
		data = pd.read_csv(filename, sep=" ", header=None)
		index = str(x)
		data.columns = ["oa"+index, "oacomp"+index, "oacomm"+index, "oacomm2"+index, "oatime"+index]
		data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
		swTh =  dfSW.ix[z].item()
		optTh = dfOPT.ix[z, x-1].item()
		dfTemp[x] = dfTemp[x].append(data, ignore_index=True);
		dfTempR[x] = dfTempR[x].append(data / swTh, ignore_index=True);
		dfTempO[x] = dfTempO[x].append(data / optTh, ignore_index=True);
	dfOPTALL = pd.concat([dfOPTALL, dfTemp[x]], axis=1)
	rOPTALL = pd.concat([rOPTALL, dfTempR[x]], axis=1)
	oOPTALL = pd.concat([oOPTALL, dfTempO[x]], axis=1)

print dfSW
print dfOPT
print dfEASY
print dfDSS
print dfOPTALL
print rOPTALL
print oOPTALL


# Calculate Improvement
rOPT = pd.DataFrame()
rEASY = pd.DataFrame()
rDSS = {}
for y in weight:
	rDSS[y] = pd.DataFrame()
for x in xrange(1, HW):
	index = str(x)
	rOPT["o"+index] = dfOPT["o"+index] / dfSW["sw"]
	rEASY["i"+index] = dfEASY["i"+index] / dfSW["sw"]
	for y in weight:
		rDSS[y]["d"+index] = dfDSS[y]["d"+index] / dfSW["sw"]
print rOPT
print rEASY
print rDSS
print rOPTALL


# Calculate Archievment
oSW = pd.DataFrame()
oEASY = pd.DataFrame()
oDSS = {}
for y in weight:
	oDSS[y] = pd.DataFrame()
for x in xrange(1, HW):
	index = str(x)
	oSW["sw"+index] = dfSW["sw"] / dfOPT["o"+index]
	oEASY["i"+index] = dfEASY["i"+index] / dfOPT["o"+index]
	for y in weight:
		oDSS[y]["d"+index] = dfDSS[y]["d"+index] / dfOPT["o"+index]
print oSW
print oEASY
print oDSS
print oOPTALL





# Calculate Mean
meanSW = np.repeat(dfSW["sw"].mean(), HW-1)
oMeanSW = []
for x in range (1, HW):
	index = "sw" + str(x)
	oMeanSW.append(oSW[index].mean())

meanOPT = []
rMeanOPT = []
for x in range (1, HW):
	index = "o" + str(x)
	meanOPT.append(dfOPT[index].mean())
	rMeanOPT.append(rOPT[index].mean())
for x in range (1, HW-1):
	index = x
	index2 = x-1
	meanOPT[index] = np.where(meanOPT[index] < meanOPT[index2], meanOPT[index2], meanOPT[index])
	rMeanOPT[index] = np.where(rMeanOPT[index] < rMeanOPT[index2], rMeanOPT[index2], rMeanOPT[index])


meanEASY = []
rMeanEASY = []
oMeanEASY = []
for x in range (1, HW):
	index = "i" + str(x)
	meanEASY.append(dfEASY[index].mean())
	rMeanEASY.append(rEASY[index].mean())
	oMeanEASY.append(oEASY[index].mean())

meanDSS = {}
rMeanDSS = {}
oMeanDSS = {}
for y in weight:
	meanDSS[y] = []
	rMeanDSS[y] = []
	oMeanDSS[y] = []
	for x in range (1, HW):
		index = "d" + str(x)
		meanDSS[y].append(dfDSS[y][index].mean())
		rMeanDSS[y].append(rDSS[y][index].mean())
		oMeanDSS[y].append(oDSS[y][index].mean())

meanOPTALL = []
rMeanOPTALL = []
oMeanOPTALL = []
for x in range (1, HW2):
	index = "oa" + str(x)
	meanOPTALL.append(dfOPTALL[index].mean())
	rMeanOPTALL.append(rOPTALL[index].mean())
	oMeanOPTALL.append(oOPTALL[index].mean())




# Print out the result
xaxis = np.arange(1, HW)
os.chdir(app_dir)
if not os.path.exists("Result_SS"):
	os.makedirs("Result_SS")
res_dir = app_dir + "/Result_SS"
os.chdir(res_dir)

dfSW.to_csv('resSW.txt', header=False, index=False, sep='\t')
dfOPT.to_csv('resOPT.txt', header=False, index=False, sep='\t')
dfEASY.to_csv('resESAY.txt', header=False, index=False, sep='\t')
dfOPTALL.to_csv('resOPTALL.txt', header=False, index=False, sep='\t')
for y in weight:
	fileOutput = "resDSS" + str(y) + ".txt"
	dfDSS[y].to_csv(fileOutput, header=False, index=False, sep='\t')

rOPT.to_csv('resR_OPT.txt', header=False, index=False, sep='\t')
rEASY.to_csv('resR_ESAY.txt', header=False, index=False, sep='\t')
rOPTALL.to_csv('resR_OPTALL.txt', header=False, index=False, sep='\t')
for y in weight:
	fileOutput = "resR_DSS" + str(y) + ".txt"
	rDSS[y].to_csv(fileOutput, header=False, index=False, sep='\t')

oSW.to_csv('resO_OPT.txt', header=False, index=False, sep='\t')
oEASY.to_csv('resO_ESAY.txt', header=False, index=False, sep='\t')
oOPTALL.to_csv('resO_OPTALL.txt', header=False, index=False, sep='\t')
for y in weight:
	fileOutput = "resO_DSS" + str(y) + ".txt"
	oDSS[y].to_csv(fileOutput, header=False, index=False, sep='\t')

fileMean = open("Mean.txt", "w")
fileMean.write("prueSW:\n")
for item in meanSW:
	fileMean.write("%s " % item)
fileMean.write("\n\n")
fileMean.write("appOPT:\n")
for item in meanOPT:
	fileMean.write("%s " % item)
fileMean.write("\n\n")
fileMean.write("appOPTALL:\n")
for item in meanOPTALL:
	fileMean.write("%s " % item)
fileMean.write("\n\n")
fileMean.write("dmEASY:\n")
for item in meanEASY:
	fileMean.write("%s " % item)
fileMean.write("\n\n")
for y in weight:
	fileMean.write("dmDSS%i:\n" % y)
	for item in meanDSS[y]:
		fileMean.write("%s " % item)
	fileMean.write("\n\n")
fileMean.close()

fileMeanR = open("MeanR.txt", "w")
fileMeanR.write("appOPT:\n")
for item in rMeanOPT:
	fileMeanR.write("%s " % item)
fileMeanR.write("\n\n")
fileMeanR.write("appOPTALL:\n")
for item in rMeanOPTALL:
	fileMeanR.write("%s " % item)
fileMeanR.write("\n\n")
fileMeanR.write("dmEASY:\n")
for item in rMeanEASY:
	fileMeanR.write("%s " % item)
fileMeanR.write("\n\n")
for y in weight:
	fileMeanR.write("dmDSS%i:\n" % y)
	for item in rMeanDSS[y]:
		fileMeanR.write("%s " % item)
	fileMeanR.write("\n\n")
fileMeanR.close()

fileMeanO = open("MeanO.txt", "w")
fileMeanO.write("appSW:\n")
for item in oMeanSW:
	fileMeanO.write("%s " % item)
fileMeanO.write("\n\n")
fileMeanO.write("appOPTALL:\n")
for item in oMeanOPTALL:
	fileMeanO.write("%s " % item)
fileMeanO.write("\n\n")
fileMeanO.write("dmEASY:\n")
for item in oMeanEASY:
	fileMeanO.write("%s " % item)
fileMeanO.write("\n\n")
for y in weight:
	fileMeanO.write("dmDSS%i:\n" % y)
	for item in oMeanDSS[y]:
		fileMeanO.write("%s " % item)
	fileMeanO.write("\n\n")
fileMeanO.close()


os.chdir(app_dir)
# PIC0: Diff Weight Relative Result
dss0 = plt.plot(xaxis, rMeanDSS[0], color = 'g')
dss1 = plt.plot(xaxis, rMeanDSS[1], color = 'b')
#dss2 = plt.plot(xaxis, rMeanDSS[2], color = 'y')
#dss5 = plt.plot(xaxis, rMeanDSS[5], color = 'r')
#dss10 = plt.plot(xaxis, rMeanDSS[10], color = 'm')

plt.title("Throughput Improvement DSS with Different Weight", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,1))
plt.savefig('DiffWeight.png')
plt.clf()


# PIC1: DSS vs EASY
xaxis0 = []
xaxis1 = []
for x in xrange(1,HW):
	xaxis0.extend([1.5*x-1])
	xaxis1.extend([1.5*x-0.5])
	
rEASY.boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis0,
	widths = 0.4)
rDSS[1].boxplot(showmeans=True, showfliers=True, sym='*', 
	positions = xaxis1,
	widths = 0.4)

plt.title("Throughput Improvement for Intuitive and DSS", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.xlim((0,(HW-1)*1.5))
plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,15))
plt.savefig('DSS_EASY.png')
plt.clf()


# PIC2: DSS vs SW vs OPT
sw = plt.plot(xaxis, meanSW, color = "g", marker = '*')
dss = plt.plot(xaxis, meanDSS[1], color = "y", marker = 'o')
opt = plt.plot(xaxis, meanOPT, color = "r", marker = '2')
optall = plt.plot(xaxis, meanOPTALL, color = "b", marker = '.')

plt.title("Throughput pureSW DSS OPT", fontsize=20)
plt.xlabel('Number of HWACCs', fontsize=16)
plt.ylabel('(Throughput (log))', fontsize=16)
plt.yscale('log')
plt.savefig('Absolute.png')
plt.clf()




