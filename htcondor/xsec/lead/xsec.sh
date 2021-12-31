#!/usr/bin/bash

ClusterId=$1
ProcId=$2

NuFlav=$3
NuCode=$4

RandNo=$(( 1314159 + RANDOM %9662607 ))

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

export DataPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/xsec/lead

echo "Checking for the output data directory.."
if [  ! -d "$DataPath"/"$NuFlav" ]; then
  mkdir -p "$DataPath"/"$NuFlav"
fi

echo "Processing $Flavor flavor.."
gmkspl -p $NuCode -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -n 500 -e 400 -o "$DataPath"/"$NuFlav"/"$ClusterId"_"$ProcId".xml --seed $RandNo &&

echo "Process has finished successfully!"
