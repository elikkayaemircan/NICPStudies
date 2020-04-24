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

RandIn=$( ls /eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/XSec/nu_mu-* | shuf -n 1 )

# Flavor
f_name="nu_mu"
f_pdg="14"

echo "Checking for the output data directory.."
if [  ! -d /eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/"$f_name"/below/"$ClusterId"."$ProcId" ]; then
  mkdir -p /eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/"$f_name"/below/"$ClusterId"."$ProcId"
fi

cd /eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/"$f_name"/below/"$ClusterId"."$ProcId"

echo "Processing $f_name flavor in between energy range 0GeV - 10GeV.."
gevgen -n 10772 -p $f_pdg -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -e 0.0,10.0 --run 1014 -f $INPUTPATH/pythia8_Geant4_1.0_withCharm_nu.root,1014 --cross-sections $RandIn --event-generator-list CharmCCDIS --message-thresholds $GENIE/config/Messenger_laconic.xml --seed $RandNo &&

echo "Events in this range has been produced!"
