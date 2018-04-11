#!/bin/bash

TOOLDIR=build/release/Linux/bin

AT=50
DT=10
SD=15
PREFIX=
SUFFIX=TEST

APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/${PREFIX}_AT${AT}_DT${DT}_SD${SD}_${SUFFIX}
APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/SampleOpenVX25

#SUBDIR
RESDIR=${APPSDIR}/Exhaustive
FILEIN=resHW
PATTERN="Best FBs:"
FILEOUT=FBHW

ACCSNUM=17

echo "Grep FB."
for((i=1;i<$ACCSNUM;i++))
{
    OUTFILE=${RESDIR}/${FILEOUT}${i}.txt
    echo "Selected FBs:" > $OUTFILE
    sed -n 's/Best FBs: //p'  ${RESDIR}/${FILEIN}${i}.txt >> $OUTFILE
    #grep -w "Best" ${RESDIR}/${FILEIN}${i}.txt | sed -n 's/Best FBs: //p'
    #grep -w "Best FBs:" ${RESDIR}/${FILEIN}${i}.txt | sed -n 's/.* //p' | tr -d '\n' >> $OUTFILE
    #echo -n " " >> $OUTFILE
}

echo "Finish."
