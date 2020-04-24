#!/usr/bin/bash

# This script removes the empty and the broken directories.

#inPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents
inPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents

flav=nu_mu

find "$inPath"/"$flav"/below/ -type d -empty -delete

for eachFold in "$inPath"/"$flav"/below/* ; do
    #if [[ ! -f "$eachFold"/gntp.0.ghep.root ]]; then
    if [[ ! -f "$eachFold"/ship.conical.Genie-TGeant4.root ]]; then
        echo "$eachFold is missing";
        rm -r $eachFold
    fi
done

find "$inPath"/"$flav"/above/ -type d -empty -delete

for eachFold in "$inPath"/"$flav"/above/* ; do
    #if [[ ! -f "$eachFold"/gntp.0.ghep.root ]]; then
    if [[ ! -f "$eachFold"/ship.conical.Genie-TGeant4.root ]]; then
        echo "$eachFold is missing";
        rm -r $eachFold
    fi
done

