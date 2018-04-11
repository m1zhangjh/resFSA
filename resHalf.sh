#!/bin/bash

TOOLDIR=build/release/Linux/bin

AT=50
DT=10
SD=15
PREFIX=
SUFFIX=TEST

APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/${PREFIX}_AT${AT}_DT${DT}_SD${SD}_${SUFFIX}
APPSDIR=/ECEnet/home/student/zhangjinghan/FSA/SampleOpenVX40

#Exhaustive
#RESDIR=${APPSDIR}/Exhaustive
#FILENAME=${RESDIR}/resRR.txt
#ACCSNUM=17
#OUTFILE=${RESDIR}/resRRR.txt

#echo "ExHW_Th: " >> $OUTFILE
#for((i=1;i<$ACCSNUM;i++))
#{
#    grep -w "ExHW${i}_Th:" $FILENAME | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
#    echo >> $OUTFILE
#}
#echo "ExHW_ThI: " >> $OUTFILE
#for((i=1;i<$ACCSNUM;i++))
#{
#    grep -w "ExHW${i}_ThI:" $FILENAME | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
#    echo >> $OUTFILE
#}
#exit 1



#HALF
RESDIR=${APPSDIR}/MMM

FILENAME=resHW

ACCSNUM=20
GENERATION=(1 10)

OUTFILE=${RESDIR}/resR.txt
echo > $OUTFILE

echo "Grep Th Res."
echo "DSS_Th" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "DSS_Th:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "GANO_Th" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "GANO_Th:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "GADSS_Th" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "GADSS_Th:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "Ex_Th" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "Ex_Th:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

################################################
echo "Grep ThI Res"

echo "DSS_ThI" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "DSS_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "GANO_ThI" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "GANO_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "GADSS_ThI" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "GADSS_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE

echo "Ex_ThI" >> $OUTFILE
for((i=1;i<$ACCSNUM;i++))
{
    grep -w "Ex_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
    echo >> $OUTFILE
}
echo >> $OUTFILE
echo >> $OUTFILE






#echo "DSS_ThImprove" >> $OUTFILE
#for((i=1;i<$ACCSNUM;i++))
#{
#    grep -w "DSS_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
#    echo >> $OUTFILE
#}
#echo >> $OUTFILE
#echo >> $OUTFILE

#echo "Grep GA Res."
#for((n=0;n<${#GENERATION[@]};n++))
#{
#    echo "GA${GENERATION[$n]}_Th:" >> $OUTFILE 
#    for((i=1;i<$ACCSNUM;i++))
#    {
#	grep -w "GA${GENERATION[$n]}_Th:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
#	echo >> $OUTFILE
#    }
#    echo >> $OUTFILE
#    echo >> $OUTFILE
#}
#for((n=0;n<${#GENERATION[@]};n++))
#{
#    echo "GA${GENERATION[$n]}_ThImprove:" >> $OUTFILE 
#    for((i=1;i<$ACCSNUM;i++))
#    {
#	grep -w "GA${GENERATION[$n]}_ThI:" ${RESDIR}/${FILENAME}${i}.txt | sed -n 's/.* //p' | tr '\n' ' ' >> $OUTFILE
#	echo >> $OUTFILE
#   }
#    echo >> $OUTFILE
#    echo >> $OUTFILE
#}






echo "Finish."
