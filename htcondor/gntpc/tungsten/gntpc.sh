#!/usr/bin/bash

ClusterId=$1
ProcId=$2

NuFlav=$3
NuCode=$4

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

echo "Loading enviromental variables for the inputs and Genie confs.."
export MyPath=/eos/experiment/ship/user/eelikkaya/NICPStudies
export GXMLPATH=$MyPath/inputs

echo "Checking for the input data directory.."
if [  ! -d "$MyPath"/data/genie/tungsten/"$NuFlav"/"$ClusterId"_"$ProcId" ]; then
  echo "No input found!" ;
  exit 1 ;
fi

echo "Processing $NuFlav flavor for gntpc.."
python /afs/cern.ch/user/e/eelikkay/NICPStudies/htcondor/gntpc/tungsten/add_PvsPt.py --ClusterId $ClusterId --ProcId $ProcId --NuFlav $NuFlav --NuCode $NuCode

echo "Events has been produced!"
