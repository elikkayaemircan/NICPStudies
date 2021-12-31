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

RandIn=$( ls "$MyPath"/data/xsec/tungsten/"$NuFlav"/* | shuf -n 1 )

echo "Checking for the output data directory.."
if [  ! -d "$MyPath"/data/genie/tungsten/"$NuFlav"/"$ClusterId"_"$ProcId" ]; then
  mkdir -p "$MyPath"/data/genie/tungsten/"$NuFlav"/"$ClusterId"_"$ProcId"
fi

cd "$MyPath"/data/genie/tungsten/"$NuFlav"/"$ClusterId"_"$ProcId"

if [[ `echo $NuCode | grep '-' | wc -l` -eq 1 ]]; then
  hCode=20$( echo $NuCode | sed -e 's/-//' ) ;
else
  hCode=10$NuCode ;
fi

echo "Processing $NuFlav flavor for genie events.."
gevgen -n 100000 -p $NuCode -t 1000741830[0.90],1000280580[0.060],1000290630[0.040] -e 0.0,350.0 --run $hCode -f $MyPath/inputs/pythia8_Geant4_wo2d_withCharm_nu.root,$hCode --cross-sections $RandIn --event-generator-list CharmCCDIS --message-thresholds $GENIE/config/Messenger_laconic.xml --seed $RandNo &&

echo "Events has been produced!"
