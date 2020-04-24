#!/usr/bin/python

# This script deletes the broken ROOT files.

import ROOT as r
import os, shutil

path='/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_e_bar/above'
broken='/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/broken'
directories=os.listdir(path)

nEntries = 95854

for dir in directories:
    root = path+'/'+dir+'/ship.conical.Genie-TGeant4.root'
    f = r.TFile(root)
    #print root
    try:
      t = f.Get('cbmsim')
      nEnt = t.GetEntries()
      if nEnt != nEntries:
        print 'File is broken - Missing Event! :', root
        shutil.move(path+'/'+dir , broken)
        #shutil.rmtree(path+'/'+dir)
    except AttributeError:
      print 'File is broken: - Empty Root File! :', root
      shutil.move(path+'/'+dir , broken)
      #shutil.rmtree(path+'/'+dir)
