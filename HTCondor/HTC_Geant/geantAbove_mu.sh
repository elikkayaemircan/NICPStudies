#!/usr/bin/bash

ClusterId=$1
ProcId=$2

echo "Loading enviromental variables for eelikkay.."
source /afs/cern.ch/user/e/eelikkay/.bashrc

echo "Loading enviromental variables from cvmfs.."
source /cvmfs/ship.cern.ch/SHiP-2018/latest/setUp.sh

cd /afs/cern.ch/user/e/eelikkay

RandIn=$( ls /eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/nu_mu/above/*/genie-nu* | shuf -n 1 )

# Flavor
f_name="nu_mu"
f_wght="89228"

echo "Checking for the output data directory.."
if [  ! -d /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/"$f_name"/above/"$ClusterId"."$ProcId" ]; then
  mkdir -p /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/"$f_name"/above/"$ClusterId"."$ProcId"
fi

echo "Processing $f_name flavor in between energy range 10GeV to 350GeV.."
alienv setenv FairShip/latest -c python /afs/cern.ch/user/e/eelikkay/sw/slc7_x86-64/FairShip/master-1/macro/run_simScript.py --Genie -f $RandIn -n $f_wght -o /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/"$f_name"/above/"$ClusterId"."$ProcId"
