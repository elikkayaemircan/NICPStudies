#!/usr/bin/python

import ROOT, os
import argparse

neutrinos = '/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_10.0_withCharm_nu.root' #path of flux
flav = 'nu_e'

def init():
      ap = argparse.ArgumentParser(
          description='Run the dummy builder')
      ap.add_argument('--procId', type=str, help="Process ID", dest='procId', default=None)
      args = ap.parse_args()
      return args

args = init() #to get the options

procId = args.procId

fp = ROOT.TFile(neutrinos)

def makeNtuples():
    print procId
    os.chdir('/eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/'+flav+'/above/'+procId)
    os.system("gntpc -i gntp.0.ghep.root -f gst --message-thresholds $GENIE/config/Messenger_laconic.xml")
    # add p/pt histogram
    fn = ROOT.TFile("gntp.0.gst.root","update")
    fp.Get('1012'.replace('0','2')).Write()
    fn.Close()
    os.system("mv gntp.0.gst.root genie-"+flav+".root")

if os.path.exists('/eos/experiment/ship/user/eelikkaya/NICPStudies/GenieEvents/'+flav+'/above/'+procId+'/genie-'+flav+'.root'):
    print "ok"
else:
    makeNtuples()
