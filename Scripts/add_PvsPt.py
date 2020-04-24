#!/usr/bin/python

import ROOT, os

neutrinos = '/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_10.0_withCharm_nu.root' #path of flux
flav = 'nu_e'

fp = ROOT.TFile(neutrinos)

def makeNtuples():
  for eachd in os.listdir('/eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/'+flav+'/above'):
    # reproduce file in gst format
    print eachd
    os.chdir('/eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/'+flav+'/above/'+eachd)
    os.system("gntpc -i gntp.0.ghep.root -f gst --message-thresholds $GENIE/config/Messenger_laconic.xml")
    # add p/pt histogram
    fn = ROOT.TFile("gntp.0.gst.root","update")
    fp.Get('1212'.replace('0','2')).Write()
    fn.Close()
    os.system("mv gntp.0.gst.root genie-"+flav+".root")

makeNtuples()
