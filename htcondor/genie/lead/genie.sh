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

echo "Loading enviromental variables for the inputs and Genie confs.."
export MyPath=/eos/experiment/ship/user/eelikkaya/NICPStudies
export GXMLPATH=$MyPath/inputs

RandIn=$( ls "$MyPath"/data/xsec/lead/"$NuFlav"/* | shuf -n 1 )

echo "Checking for the output data directory.."
if [  ! -d "$MyPath"/data/genie/"$NuFlav"/"$ClusterId"_"$ProcId" ]; then
  mkdir -p "$MyPath"/data/genie/"$NuFlav"/"$ClusterId"_"$ProcId"
fi

cd "$MyPath"/data/genie/"$NuFlav"/"$ClusterId"_"$ProcId"

if [[ `echo $NuCode | grep '-' | wc -l` -eq 1 ]]; then
  hCode=20$( echo $NuCode | sed -e 's/-//' ) ;
else
  hCode=10$NuCode ;
fi

echo "Processing $NuFlav flavor for genie events.."
gevgen -n 100000 -p $NuCode -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -e 0.0,350.0 --run $hCode -f $MyPath/inputs/pythia8_Geant4_wo2d_withCharm_nu.root,$hCode --cross-sections $RandIn --event-generator-list CharmCCDIS --message-thresholds $GENIE/config/Messenger_laconic.xml --seed $RandNo &&

echo "Events has been produced!"
