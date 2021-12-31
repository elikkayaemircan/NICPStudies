#!/usr/bin/python

import ROOT, os, shutil, argparse

def init():
  ap = argparse.ArgumentParser(
      description='Run the gntpc')
  ap.add_argument('--ClusterId', type=str, help="ClusterId", dest='ClusterId', default=None)
  ap.add_argument('--ProcId', type=str, help="ProcId", dest='ProcId', default=None)
  ap.add_argument('--NuFlav', type=str, help="NuFlav", dest='NuFlav', default=None)
  ap.add_argument('--NuCode', type=str, help="NuCode", dest='NuCode', default=None)
  args = ap.parse_args()
  return args

args = init() #to get the options

ClusterId=args.ClusterId
ProcId=args.ProcId
NuFlav=args.NuFlav
NuCode=args.NuCode

if 'bar' in NuFlav:
    hCode='20'+NuCode.replace('-','')
else:
    hCode='10'+NuCode

fB = "/eos/experiment/ship/data/Mbias/background-prod-2018/pythia8_Geant4_1.0_withCharm_nu.root" #path of flux
fA = "/eos/experiment/ship/data/Mbias/background-prod-2018/pythia8_Geant4_10.0_withCharm_nu.root" #path of flux

fp = ROOT.TFile(fB)
fl = ROOT.TFile(fA)

def makeNtuples():

    # reproduce file in gst format
    os.chdir('/eos/experiment/ship/user/eelikkaya/NICPStudies/data/genie/'+NuFlav+'/'+ClusterId+'_'+ProcId)
    #os.system("gntpc -i gntp.0.ghep.root -f gst --message-thresholds $GENIE/config/Messenger_laconic.xml")

    # create a backup of the file
    shutil.copyfile('./gntp.0.gst.root', './gntp.0.gst_below.root')
    shutil.copyfile('./gntp.0.gst.root', './gntp.0.gst_above.root')

    # add p/pt histogram for below 10 GeV
    fn = ROOT.TFile("gntp.0.gst_below.root","update")
    fp.Get(hCode.replace('0','2')).Write()
    fn.Close()

    # add p/pt histogram for above 10 GeV
    fn = ROOT.TFile("gntp.0.gst_above.root","update")
    fl.Get(hCode.replace('0','2')).Write()
    fn.Close()

makeNtuples()
