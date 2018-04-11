#!/bin/bash

TOOLDIR=build/release/Linux/bin

AT=50
DT=15
SD=5
PREFIX=
SUFFIX=0.557

APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/${PREFIX}_AT${AT}_DT${DT}_SD${SD}_${SUFFIX}
APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/SampleOpenVX40

RESDIR=${APPSDIR}/GANO

FILENAME=resHW

ACCSNUM=20
GENERATION=20

OUTFILE=${RESDIR}/resR.txt
echo > $OUTFILE
echo "Grep GA Res."
for((n=0;n<$GENERATION;n++))
{
    echo "Generation: $n" >> $OUTFILE 
    for((i=1;i<$ACCSNUM;i++))
    {
	grep -w "G${n}Result:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr -d '\n' >> $OUTFILE
	echo -n " " >> $OUTFILE
    }
    echo >> $OUTFILE
    echo >> $OUTFILE
}


OUTFILE2=${RESDIR}/nrD.txt
echo > $OUTFILE2
echo "Grep nr Design Point."
for((i=1;i<$ACCSNUM;i++))
{
    echo "HW: $i" >> $OUTFILE2
    for((n=0;n<$GENERATION;n++))
    {
	grep -w "G${n}nrChm:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr -d '\n' >> $OUTFILE2
	echo -n " " >> $OUTFILE2
    }
    echo >> $OUTFILE2
    echo >> $OUTFILE2
}



#OUTFILE3=${RESDIR}/timeCal.txt
#INFILE3=${RESDIR}/time.txt
#echo "Calculate the execution time."
#echo "20G GA execution time for diff Budget" > $OUTFILE3
#while read budget start end
#do
#    echo "@@@"
    #echo $budget >> $OUTFILE3
#    echo $budget
    #echo $start >> $OUTFILE3
    #echo $end >> $OUTFILE3
    #echo $end
#done < $INFILE3
echo "Finish."
