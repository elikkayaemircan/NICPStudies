#!/usr/bin/bash

ClusterId=$1
ProcId=$2

NuFlav=$3
NuCode=$4

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

export InputPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/xsec/tungsten
export OutputPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/gspl/tungsten

PickAny=$( ls "$InputPath"/"$NuFlav" | shuf -n 1 )
InputId="${PickAny/_*/}"

echo "Checking for the output data directory.."
if [  ! -d "$OutputPath"/"$NuFlav" ]; then
  mkdir -p "$OutputPath"/"$NuFlav"
fi

echo "Checking for the input data file.."
if [  ! -f "$InputPath"/"$NuFlav"/"$InputId"_"$ProcId".xml ]; then
  echo "Input with specified parameters does not exist!"
  exit 1;
else
  echo "Processing $Flavor flavor.."
  gspl2root -f "$InputPath"/"$NuFlav"/"$InputId"_"$ProcId".xml -p $NuCode -t 1000741830[0.90],1000280580[0.060],1000290630[0.040] -e 400 -o "$OutputPath"/"$NuFlav"/"$InputId"_"$ProcId".root &&
  echo "Process has finished successfully!"
  exit 0;
fi
