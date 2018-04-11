#!/bin/bash

TOOLDIR=build/release/Linux/bin

AT=50
DT=15
SD=5
PREFIX=
SUFFIX=0.557

APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/${PREFIX}_AT${AT}_DT${DT}_SD${SD}_${SUFFIX}
APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/SampleOpenVX15

RESDIR=${APPSDIR}/Exhaustive

FILENAME=resHW

ACCSNUM=20

OUTFILE=${RESDIR}/resR.txt
echo > $OUTFILE
echo "Grep GA Res."
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "Best Throughput Improvement:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr -d '\n' >> $OUTFILE
    echo -n " " >> $OUTFILE
}
echo >> $OUTFILE

echo "Finish."
