import ROOT as r
import os

def configure():
  f = r.TFile('nu_mu.root')
  t = f.cret
  t.MakeClass()
  r.gROOT.ProcessLine('.L cret.C')
  cret_ch = r.TChain('cret', 'cret')
  cret_ch.Add('nu_mu.root')
  cret = r.cret(cret_ch)
  return cret

def finish():
  os.system('rm cret.C cret.h')
