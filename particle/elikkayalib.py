import ROOT as r
import os

def configure(input_file):
  f = r.TFile(input_file)
  t = f.cret
  t.MakeClass()
  r.gROOT.ProcessLine('.L cret.C')
  cret_ch = r.TChain('cret', 'cret')
  cret_ch.Add(input_file)
  cret = r.cret(cret_ch)
  return cret

def finish():
  os.system('rm cret.C cret.h')
