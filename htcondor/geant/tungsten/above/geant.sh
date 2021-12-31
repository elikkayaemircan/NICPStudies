#!/usr/bin/bash

ClusterId=$1
ProcId=$2

NuFlav=$3
NuCode=$4

NuWght=$5

RandNo=$(( 1314159 + RANDOM %9662607 ))

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /cvmfs/ship.cern.ch/SHiP-2020/latest/setUp.sh'

echo "Loading enviromental variables for the inputs.."
export MyPath=/eos/experiment/ship/user/eelikkaya/NICPStudies

RandIn=$( ls "$MyPath"/data/genie/tungsten/"$NuFlav"/*/gntp.0.gst_above.root | shuf -n 1 )

echo "Checking for the output data directory.."
if [  ! -d "$MyPath"/data/geant/tungsten/"$NuFlav"/above/"$ClusterId"_"$ProcId" ]; then
  mkdir -p "$MyPath"/data/geant/tungsten/"$NuFlav"/above/"$ClusterId"_"$ProcId"
fi

cd /afs/cern.ch/user/e/eelikkay

echo "Processing $NuFlav flavor for geant events.."
alienv setenv FairShip/latest -c python /afs/cern.ch/user/e/eelikkay/sw/slc7_x86-64/FairShip/master-1/macro/run_simScript.py --Genie -f $RandIn -n $NuWght -o "$MyPath"/data/geant/tungsten/"$NuFlav"/above/"$ClusterId"_"$ProcId"

echo "Events has been produced!"
