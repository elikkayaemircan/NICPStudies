#!/bin/python

import re, subprocess

belowFile = open("/eos/experiment/ship/user/eelikkaya/NICPStudies/Analysis/numu_Below100K.out","r")
aboveFile = open("/eos/experiment/ship/user/eelikkaya/NICPStudies/Analysis/numu_Above100K.out","r")

belowEff, bnmbrEff = [], []
aboveEff, anmbrEff = [], []

for lineNo, line in enumerate(belowFile):
    r = re.findall("0.[0-9][0-9][0-9][0-9][0-9]", line)
    if r:
        belowEff.append(float(r[0]))
        l = lineNo+1
    if lineNo == l:
        rl = re.findall("\d", line)
        bnmbrEff.append(str(line[:-1]))

for lineNo, line in enumerate(aboveFile):
    r = re.findall("0.[0-9][0-9][0-9][0-9][0-9]", line)
    if r:
        aboveEff.append(float(r[0]))
        l = lineNo+1
    if lineNo == l:
        rl = re.findall("\d", line)
        anmbrEff.append(str(line[:-1]))

for x in range(len(aboveEff)):
    if abs((belowEff[x] - aboveEff[x])/aboveEff[x])*100 <= 2.:
        print "OK!", anmbrEff[x]
    else:
        print "Moving file into Suspicious folder!", anmbrEff[x]
        subprocess.call(["mv", anmbrEff[x], "/eos/experiment/ship/user/eelikkaya/NICPStudies/SingleCheck/Suspicious/"])
