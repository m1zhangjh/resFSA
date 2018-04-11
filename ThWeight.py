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

nrApp = 40
HW = 20
HW2 = 11

AT = 50
DT = 15
SD = 5
SUFFIX = "0.325"

prev_dir = os.getcwd()

#app_dir = prev_dir + "/_AT" + str(AT) + "_DT" + str(DT) + "_SD" + str(SD) + "_" + SUFFIX  
app_dir = prev_dir + "/SampleOpenVX40"

sw_dir = app_dir + "/pureSW"
#easy_dir = app_dir + "/DmEasy"
opt_dir = app_dir + "/OPT"
#dssN_dir = app_dir + "/DmDSS_N/Weight1"
#dssF_dir = app_dir + "/DmDSS_F/Weight1"
dssD_dir = app_dir + "/DmDSS_D/Weight1"
#dssP_dir = app_dir + "/DmDSS_P/Weight1"
#dssA_dir = app_dir + "/DmDSS_A/Weight1"
#dssX_dir = app_dir + "/DmDSS_X/Weight1"

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
#dfEASY = pd.DataFrame()
#dfDSSN = pd.DataFrame()
#dfDSSF = pd.DataFrame()
dfDSSD = pd.DataFrame()
#dfDSSP = pd.DataFrame()
#dfDSSA = pd.DataFrame()
#dfDSSX = pd.DataFrame()

for x in xrange(1, HW):
	cur_dir = opt_dir
	os.chdir(cur_dir)
	filename = file_prev + str(x) + file_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["o"+index, "icomp"+index, "icomm"+index, "icomm2"+index, "itime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfOPT = pd.concat([dfOPT, data], axis=1)

#	cur_dir = easy_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["i"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfEASY = pd.concat([dfEASY, data], axis=1)

#	cur_dir = dssN_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["dN"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfDSSN = pd.concat([dfDSSN, data], axis=1)

#	cur_dir = dssF_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["dF"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfDSSF = pd.concat([dfDSSF, data], axis=1)

	cur_dir = dssD_dir
	os.chdir(cur_dir)
	filename = file_prev + str(x) + file_back
	data = pd.read_csv(filename, sep=" ", header=None)
	index = str(x)
	data.columns = ["dD"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
	dfDSSD = pd.concat([dfDSSD, data], axis=1)

#	cur_dir = dssP_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["dP"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfDSSP = pd.concat([dfDSSP, data], axis=1)

#	cur_dir = dssA_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["dA"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfDSSA = pd.concat([dfDSSA, data], axis=1)

#	cur_dir = dssX_dir
#	os.chdir(cur_dir)
#	filename = file_prev + str(x) + file_back
#	data = pd.read_csv(filename, sep=" ", header=None)
#	index = str(x)
#	data.columns = ["dX"+index, "dcomp"+index, "dcomm"+index, "dcomm2"+index, "dtime"+index]
#	data.drop(data.columns[[1, 2, 3, 4]], axis=1, inplace=True)
#	dfDSSX = pd.concat([dfDSSX, data], axis=1)

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

for x in xrange(0, HW-2):
	for y in range(0, nrApp):
		if dfOPT.iloc[y,x] > dfOPT.iloc[y,x+1]:
			dfOPT.iloc[y,x+1] = dfOPT.iloc[y,x]

print dfSW
print dfOPT
#print dfEASY
#print dfDSSN
#print dfDSSF
print dfDSSD
#print dfDSSP
#print dfDSSA
#print dfDSSX
print dfOPTALL
print rOPTALL
print oOPTALL


# Calculate Improvement
rOPT = pd.DataFrame()
#rEASY = pd.DataFrame()
#rDSSN = pd.DataFrame()
#rDSSF = pd.DataFrame()
rDSSD = pd.DataFrame()
#rDSSP = pd.DataFrame()
#rDSSA = pd.DataFrame()
#rDSSX = pd.DataFrame()
for x in xrange(1, HW):
	index = str(x)
	rOPT["o"+index] = dfOPT["o"+index] / dfSW["sw"]
#	rEASY["i"+index] = dfEASY["i"+index] / dfSW["sw"]
#	rDSSN["dN"+index] = dfDSSN["dN"+index] / dfSW["sw"]
#	rDSSF["dF"+index] = dfDSSF["dF"+index] / dfSW["sw"]
	rDSSD["dD"+index] = dfDSSD["dD"+index] / dfSW["sw"]
#	rDSSP["dP"+index] = dfDSSP["dP"+index] / dfSW["sw"]
#	rDSSA["dA"+index] = dfDSSA["dA"+index] / dfSW["sw"]
#	rDSSX["dX"+index] = dfDSSX["dX"+index] / dfSW["sw"]
print rOPT
#print rEASY
#print rDSSN
#print rDSSF
print rDSSD
#print rDSSP
#print rDSSA
#print rDSSX
print rOPTALL


# Calculate Archievment
oSW = pd.DataFrame()
#oEASY = pd.DataFrame()
#oDSSN = pd.DataFrame()
#oDSSF = pd.DataFrame()
oDSSD = pd.DataFrame()
#oDSSP = pd.DataFrame()
#oDSSA = pd.DataFrame()
#oDSSX = pd.DataFrame()
for x in xrange(1, HW):
	index = str(x)
	oSW["sw"+index] = dfSW["sw"] / dfOPT["o"+index]
#	oEASY["i"+index] = dfEASY["i"+index] / dfOPT["o"+index]
#	oDSSN["dN"+index] = dfDSSN["dN"+index] / dfOPT["o"+index]
#	oDSSF["dF"+index] = dfDSSF["dF"+index] / dfOPT["o"+index]
	oDSSD["dD"+index] = dfDSSD["dD"+index] / dfOPT["o"+index]
#	oDSSP["dP"+index] = dfDSSP["dP"+index] / dfOPT["o"+index]
#	oDSSA["dA"+index] = dfDSSA["dA"+index] / dfOPT["o"+index]
#	oDSSX["dX"+index] = dfDSSX["dX"+index] / dfOPT["o"+index]
print oSW
#print oEASY
#print oDSSN
#print oDSSF
print oDSSD
#print oDSSP
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


#meanEASY = []
#rMeanEASY = []
#oMeanEASY = []
#for x in range (1, HW):
#	index = "i" + str(x)
#	meanEASY.append(dfEASY[index].mean())
#	rMeanEASY.append(rEASY[index].mean())
#	oMeanEASY.append(oEASY[index].mean())

#meanDSSN = []
#rMeanDSSN = []
#oMeanDSSN = []
#for x in range (1, HW):
#	index = "dN" + str(x)
#	meanDSSN.append(dfDSSN[index].mean())
#	rMeanDSSN.append(rDSSN[index].mean())
#	oMeanDSSN.append(oDSSN[index].mean())
#meanDSSF = []
#rMeanDSSF = []
#oMeanDSSF = []
#for x in range (1, HW):
#	index = "dF" + str(x)
#	meanDSSF.append(dfDSSF[index].mean())
#	rMeanDSSF.append(rDSSF[index].mean())
#	oMeanDSSF.append(oDSSF[index].mean())
meanDSSD = []
rMeanDSSD = []
oMeanDSSD = []
for x in range (1, HW):
	index = "dD" + str(x)
	meanDSSD.append(dfDSSD[index].mean())
	rMeanDSSD.append(rDSSD[index].mean())
	oMeanDSSD.append(oDSSD[index].mean())
#meanDSSP = []
#rMeanDSSP = []
#oMeanDSSP = []
#for x in range (1, HW):
#	index = "dP" + str(x)
#	meanDSSP.append(dfDSSP[index].mean())
#	rMeanDSSP.append(rDSSP[index].mean())
#	oMeanDSSP.append(oDSSP[index].mean())
#meanDSSA = []
#rMeanDSSA = []
#oMeanDSSA = []
#for x in range (1, HW):
#	index = "dA" + str(x)
#	meanDSSA.append(dfDSSA[index].mean())
#	rMeanDSSA.append(rDSSA[index].mean())
#	oMeanDSSA.append(oDSSA[index].mean())
#meanDSSX = []
#rMeanDSSX = []
#oMeanDSSX = []
#for x in range (1, HW):
#	index = "dX" + str(x)
#	meanDSSX.append(dfDSSX[index].mean())
#	rMeanDSSX.append(rDSSX[index].mean())
#	oMeanDSSX.append(oDSSX[index].mean())

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
if not os.path.exists("Result_Weight"):
	os.makedirs("Result_Weight")
res_dir = app_dir + "/Result_Weight"
os.chdir(res_dir)

dfSW.to_csv('resSW.txt', header=False, index=False, sep='\t')
dfOPT.to_csv('resOPT.txt', header=False, index=False, sep='\t')
#dfEASY.to_csv('resESAY.txt', header=False, index=False, sep='\t')
dfOPTALL.to_csv('resOPTALL.txt', header=False, index=False, sep='\t')
#dfDSSN.to_csv('resDSSN.txt', header=False, index=False, sep='\t')
#dfDSSF.to_csv('resDSSF.txt', header=False, index=False, sep='\t')
dfDSSD.to_csv('resDSSD.txt', header=False, index=False, sep='\t')
#dfDSSP.to_csv('resDSSG.txt', header=False, index=False, sep='\t')
#dfDSSA.to_csv('resDSSA.txt', header=False, index=False, sep='\t')
#dfDSSX.to_csv('resDSSX.txt', header=False, index=False, sep='\t')

rOPT.to_csv('resR_OPT.txt', header=False, index=False, sep='\t')
#rEASY.to_csv('resR_ESAY.txt', header=False, index=False, sep='\t')
rOPTALL.to_csv('resR_OPTALL.txt', header=False, index=False, sep='\t')
#rDSSN.to_csv('resR_DSSN.txt', header=False, index=False, sep='\t')
#rDSSF.to_csv('resR_DSSF.txt', header=False, index=False, sep='\t')
rDSSD.to_csv('resR_DSSD.txt', header=False, index=False, sep='\t')
#rDSSP.to_csv('resR_DSSG.txt', header=False, index=False, sep='\t')
#rDSSA.to_csv('resR_DSSA.txt', header=False, index=False, sep='\t')
#rDSSX.to_csv('resR_DSSX.txt', header=False, index=False, sep='\t')

oSW.to_csv('resO_OPT.txt', header=False, index=False, sep='\t')
#oEASY.to_csv('resO_ESAY.txt', header=False, index=False, sep='\t')
oOPTALL.to_csv('resO_OPTALL.txt', header=False, index=False, sep='\t')
#oDSSN.to_csv('resO_DSSN.txt', header=False, index=False, sep='\t')
#oDSSF.to_csv('resO_DSSF.txt', header=False, index=False, sep='\t')
oDSSD.to_csv('resO_DSSD.txt', header=False, index=False, sep='\t')
#oDSSP.to_csv('resO_DSSG.txt', header=False, index=False, sep='\t')
#oDSSA.to_csv('resO_DSSA.txt', header=False, index=False, sep='\t')
#oDSSX.to_csv('resO_DSSX.txt', header=False, index=False, sep='\t')

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
#fileMean.write("dmEASY:\n")
#for item in meanEASY:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
#fileMean.write("dmDSSN:\n")
#for item in meanDSSN:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
#fileMean.write("dmDSSF:\n")
#for item in meanDSSF:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
fileMean.write("dmDSSD:\n")
for item in meanDSSD:
	fileMean.write("%s " % item)
fileMean.write("\n\n")
#fileMean.write("dmDSSP:\n")
#for item in meanDSSP:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
#fileMean.write("dmDSSA:\n")
#for item in meanDSSA:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
#fileMean.write("dmDSSX:\n")
#for item in meanDSSX:
#	fileMean.write("%s " % item)
#fileMean.write("\n\n")
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
#fileMeanR.write("dmEASY:\n")
#for item in rMeanEASY:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
#fileMeanR.write("dmDSSN:\n")
#for item in rMeanDSSN:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
#fileMeanR.write("dmDSSF:\n")
#for item in rMeanDSSF:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
fileMeanR.write("dmDSSD:\n")
for item in rMeanDSSD:
	fileMeanR.write("%s " % item)
fileMeanR.write("\n\n")
#fileMeanR.write("dmDSSP:\n")
#for item in rMeanDSSP:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
#fileMeanR.write("dmDSSA:\n")
#for item in rMeanDSSA:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
#fileMeanR.write("dmDSSX:\n")
#for item in rMeanDSSX:
#	fileMeanR.write("%s " % item)
#fileMeanR.write("\n\n")
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
#fileMeanO.write("dmEASY:\n")
#for item in oMeanEASY:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
#fileMeanO.write("dmDSSN:\n")
#for item in oMeanDSSN:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
#fileMeanO.write("dmDSSF:\n")
#for item in oMeanDSSF:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
fileMeanO.write("dmDSSD:\n")
for item in oMeanDSSD:
	fileMeanO.write("%s " % item)
fileMeanO.write("\n\n")
#fileMeanO.write("dmDSSP:\n")
#for item in oMeanDSSP:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
#fileMeanO.write("dmDSSA:\n")
#for item in oMeanDSSA:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
#fileMeanO.write("dmDSSX:\n")
#for item in oMeanDSSX:
#	fileMeanO.write("%s " % item)
#fileMeanO.write("\n\n")
fileMeanO.close()


#os.chdir(app_dir)
# PIC0: Diff Weight Relative Result
#dssN = plt.plot(xaxis, rMeanDSSN, color = 'g')
#dssF = plt.plot(xaxis, rMeanDSSF, color = 'b')
#dssD = plt.plot(xaxis, rMeanDSSD, color = 'y')
#dssP = plt.plot(xaxis, rMeanDSSA, color = 'r')
#dss10 = plt.plot(xaxis, rMeanDSS[10], color = 'm')

#plt.title("Throughput Improvement DSS with Different Weight", fontsize=20)
#plt.xlabel('Number of HWACCs', fontsize=16)
#plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,1))
#plt.savefig('DiffWeightA.png')
#plt.clf()


# PIC0: Diff Weight Relative Result
#dssN = plt.plot(xaxis, rMeanDSSN, color = 'g')
#dssF = plt.plot(xaxis, rMeanDSSF, color = 'b')
#dssD = plt.plot(xaxis, rMeanDSSD, color = 'y')
#dssP = plt.plot(xaxis, rMeanDSSX, color = 'r')
#dss10 = plt.plot(xaxis, rMeanDSS[10], color = 'm')

#plt.title("Throughput Improvement DSS with Different Weight", fontsize=20)
#plt.xlabel('Number of HWACCs', fontsize=16)
#plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,1))
#plt.savefig('DiffWeightX.png')
#plt.clf()


# PIC1: DSS vs EASY
#xaxis0 = []
#xaxis1 = []
#for x in xrange(1,HW):
#	xaxis0.extend([1.5*x-1])
#	xaxis1.extend([1.5*x-0.5])
	
#rEASY.boxplot(showmeans=True, showfliers=True, sym='*', 
#	positions = xaxis0,
#	widths = 0.4)
#rDSS[1].boxplot(showmeans=True, showfliers=True, sym='*', 
#	positions = xaxis1,
#	widths = 0.4)

#plt.title("Throughput Improvement for Intuitive and DSS", fontsize=20)
#plt.xlabel('Number of HWACCs', fontsize=16)
#plt.xlim((0,(HW-1)*1.5))
#plt.ylabel('(Th(it) / (Th(SW))', fontsize=16)
#plt.ylim((0,15))
#plt.savefig('DSS_EASY.png')
#plt.clf()


# PIC2: DSS vs SW vs OPT
#sw = plt.plot(xaxis, meanSW, color = "g", marker = '*')
#dss = plt.plot(xaxis, meanDSS[1], color = "y", marker = 'o')
#opt = plt.plot(xaxis, meanOPT, color = "r", marker = '2')
#optall = plt.plot(xaxis, meanOPTALL, color = "b", marker = '.')

#plt.title("Throughput pureSW DSS OPT", fontsize=20)
#plt.xlabel('Number of HWACCs', fontsize=16)
#plt.ylabel('(Throughput (log))', fontsize=16)
#plt.yscale('log')
#plt.savefig('Absolute.png')
#plt.clf()




