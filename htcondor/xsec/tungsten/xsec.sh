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

export DataPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/xsec/tungsten

echo "Checking for the output data directory.."
if [  ! -d "$DataPath"/"$NuFlav" ]; then
  mkdir -p "$DataPath"/"$NuFlav"
fi

echo "Processing $Flavor flavor.."
gmkspl -p $NuCode -t 1000741830[0.90],1000280580[0.060],1000290630[0.040] -n 500 -e 400 -o "$DataPath"/"$NuFlav"/"$ClusterId"_"$ProcId".xml --seed $RandNo &&

echo "Process has finished successfully!"
