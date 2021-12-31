#!/usr/bin/bash

ClusterId=$1
ProcId=$2

NuFlav=$3
NuCode=$4

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

export InputPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/xsec/lead
export OutputPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/data/gspl/lead

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
  gspl2root -f "$InputPath"/"$NuFlav"/"$InputId"_"$ProcId".xml -p $NuCode -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -e 400 -o "$OutputPath"/"$NuFlav"/"$InputId"_"$ProcId".root &&
  echo "Process has finished successfully!"
  exit 0;
fi
