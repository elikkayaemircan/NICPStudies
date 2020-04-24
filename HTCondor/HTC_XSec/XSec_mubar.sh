#!/usr/bin/bash

ClusterId=$1
ProcId=$2

RandNo=$(( 1314159 + RANDOM %9662607 ))

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables for genie.."
eval 'source /afs/cern.ch/user/e/eelikkay/FairCfg/setUp.sh'

# Flavor
f_name="nu_mu_bar"
f_pdg="-14"

echo "Checking for the output data directory.."
if [  ! -d /eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/XSec ]; then
  mkdir -p /eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/XSec
fi

echo "Processing $f_name flavor.."
gmkspl -p $f_pdg -t 1000822040[0.014],1000822060[0.241],1000822070[0.221],1000822080[0.524] -n 500 -e 400 -o /eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/XSec/"$f_name"-"$ClusterId"_"$ProcId".xml --seed $RandNo &&

echo "Process has finished successfully!"
