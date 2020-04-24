#!/usr/bin/bash

ClusterId=$1
ProcId=$2

RandNo=$(( 1314159 + RANDOM %9662607 ))

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

echo "Loading enviromental variables for the inputs and Genie confs.."
export INPUTPATH=/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs
export GXMLPATH=$INPUTPATH

RandIn=$( ls /eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/XSec/nu_mu_bar-* | shuf -n 1 )

# Flavor
f_name="nu_mu_bar"
f_pdg="-14"

echo "Checking for the output data directory.."
if [  ! -d /eos/experiment/ship/user/eelikkaya/NICPStudies/WeightEvents/"$f_name"/"$ClusterId"."$ProcId" ]; then
  mkdir -p /eos/experiment/ship/user/eelikkaya/NICPStudies/WeightEvents/"$f_name"/"$ClusterId"."$ProcId"
fi

cd /eos/experiment/ship/user/eelikkaya/NICPStudies/WeightEvents/"$f_name"/"$ClusterId"."$ProcId"

echo "Processing $f_name flavor for weight calculations.."
gevgen -n 100000 -p $f_pdg -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -e 0.0,350.0 --run 2014 -f $INPUTPATH/pythia8_Geant4_wo2d_withCharm_nu.root,2014 --cross-sections $RandIn --event-generator-list CharmCCDIS --message-thresholds $GENIE/config/Messenger_laconic.xml --seed $RandNo &&

echo "Events for weight calculations has been produced!"
