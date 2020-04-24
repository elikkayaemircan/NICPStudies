#!/usr/bin/bash

find /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/below -name "ship.conical.Genie-TGeant4.root" -type f | head -130 | xargs echo
find /eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/above -name "ship.conical.Genie-TGeant4.root" -type f | head -130 | xargs echo
