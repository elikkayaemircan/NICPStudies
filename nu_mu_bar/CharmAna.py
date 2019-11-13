import ROOT as r
import rootUtils as ut

from numpy import arctan, sqrt
from physlib import *

r.gROOT.ProcessLine('.L cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('nu_mu_bar.root')
cret = r.cret(cret_ch)

g = r.TFile('/eos/experiment/ship/user/eelikkaya/events_geo/event_CharmCCDIS_Jul18/nu_mu_bar/0/geofile_full.conical.Genie-TGeant4.root')      
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

nEnt = cret.fChain.GetEntries()

a, b, c, d = 0., 0., 0., 0.
d_minus, d_zero, ds_minus, lambda_c = 0., 0., 0., 0.
CCounter = [d_minus, d_zero, ds_minus, lambda_c]

Hadron = [-130, -211, -321, -2212, 130, 211, 321, 2212]
Lepton = [-11, -13, -15, 11, 13, 15]

CharmedHadron = [-411, -421, -431, -4122]
Chargeless = [-14, 22, 111, 130, 421, 2112]

h = {}
ut.bookHist(h, 'charm_fraction', 'Charm Fractions', 4, 0, 4)
ut.bookHist(h, 'charm_fraction_selected', 'Charm Fractions (Selected)', 4, 0, 4)

h['charm_fraction'].GetXaxis().SetBinLabel(1, "D^{-}")
h['charm_fraction'].GetXaxis().SetBinLabel(2, "#bar{D^{0}}")
h['charm_fraction'].GetXaxis().SetBinLabel(3, "D_{s}^{-}")
h['charm_fraction'].GetXaxis().SetBinLabel(4, "#Lambda_{c}^{-}")

#h['slope_acc'].SetFillStyle(3335)
#h['slope_acc'].SetFillColor(2)
#ut.bookHist(h, 'test')

h0l0_g, h0l0_l, h0l0_ds= [], [], []
h1l0_g, h1l0_l, h1l0_ds= [], [], []
h2l0_g, h2l0_l, h2l0_ds= [], [], []
h3l0_g, h3l0_l, h3l0_ds= [], [], []
h4l0_g, h4l0_l, h4l0_ds= [], [], []
h5l0_g, h5l0_l, h5l0_ds= [], [], []
h0l1_g, h0l1_l, h0l1_ds= [], [], []
h1l1_g, h1l1_l, h1l1_ds= [], [], []
h2l1_g, h2l1_l, h2l1_ds= [], [], []
h3l1_g, h3l1_l, h3l1_ds= [], [], []
h4l1_g, h4l1_l, h4l1_ds= [], [], []
h5l1_g, h5l1_l, h5l1_ds= [], [], []
h0l2_g, h0l2_l, h0l2_ds= [], [], []
h1l2_g, h1l2_l, h1l2_ds= [], [], []
h2l2_g, h2l2_l, h2l2_ds= [], [], []
h3l2_g, h3l2_l, h3l2_ds= [], [], []
h4l2_g, h4l2_l, h4l2_ds= [], [], []
h5l2_g, h5l2_l, h5l2_ds= [], [], []
h0l3_g, h0l3_l, h0l3_ds= [], [], []
h1l3_g, h1l3_l, h1l3_ds= [], [], []
h2l3_g, h2l3_l, h2l3_ds= [], [], []
h3l3_g, h3l3_l, h3l3_ds= [], [], []
h4l3_g, h4l3_l, h4l3_ds= [], [], []
h5l3_g, h5l3_l, h5l3_ds= [], [], []
h6l0_g, h6l0_l, h6l0_ds= [], [], []

def GeometrySelection(Pos):
  gCheck = []
  fGeo.SetCurrentPoint(Pos[0], Pos[1], Pos[2])
  init = fGeo.FindNode()
  for i in [-1, 1]:
    for j in [-1, 1]:
      fGeo.SetCurrentDirection(i, j, 0)
      fGeo.FindNextBoundary()
      if fGeo.GetStep() > 0.1:
        gCheck.append(True)
  fGeo.SetCurrentPoint(Pos[0], Pos[1], Pos[2]-0.5)
  finl = fGeo.FindNode()
  if init.GetMotherVolume() == finl.GetMotherVolume():
    gCheck.append(True)
  if sum(gCheck) != 5: return False
  return True

def LocationSelection(Mom, Pdg):
  lCheck = []
  SlopeX = Slope(Mom[0], Mom[2])
  SlopeY = Slope(Mom[1], Mom[2])
  if Mom[3] > 1.:
    lCheck.append(True)
  if Pdg not in Chargeless:
    lCheck.append(True)
  if (SlopeX < 1. or SlopeY < 1.):
    lCheck.append(True)
  if sum(lCheck) != 3: return False
  return True

def DecaySearchSelection(Pos, CMom, CDauPos, CDauMom):
  dsCheck = []
  MSlopeX = Slope(Mom[0], Mom[2])
  MSlopeY = Slope(Mom[1], Mom[2])
  DSlopeX = Slope(CDauMom[0], CDauMom[2])
  DSlopeY = Slope(CDauMom[1], CDauMom[2])
  if FlightLength(CDauPos, Pos) < 0.4:
    dsCheck.append(True)
  if KinkAngle(MSlopeX, MSlopeY, DSlopeX, DSlopeY) > 2.0e-2:
    dsCheck.append(True)
  if ImpactParameter(Pos, Mom, CDauPos) > 1.0e-3:
    dsCheck.append(True)
  if sum(dsCheck) != 3: return False
  return True

def CharmFraction(CharmPDG, h, CCounter):
  if CharmPDG == -411:
    h.Fill(0, 1)
    CCounter[0] += 1.
  if CharmPDG == -421:
    h.Fill(1, 1)
    CCounter[1] += 1.
  if CharmPDG == -431:
    h.Fill(2, 1)
    CCounter[2] += 1.
  if CharmPDG == -4122:
    h.Fill(3, 1)
    CCounter[3] += 1.

def makePlots():
  ut.bookCanvas(h,key='FractionAnalysis',title='Produced Charmed Hadron Fractions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['FractionAnalysis'].cd(1)
  h['charm_fraction'].Draw()
  h['FractionAnalysis'].Print('~/analysis_v2/nu_mu_bar/cfraction.pdf')

def ChannelDecision(CDauPdg): #CharmDaughterPDG
  HadronCount = 0
  LeptonCount = 0
  for i in range(len(CDauPdg)):
    if CDauPdg[i] in Hadron:
      HadronCount += 1
    if CDauPdg[i] in Lepton:
      LeptonCount += 1
  if HadronCount == 0 and LeptonCount == 0:
    ch = 0
  if HadronCount == 1 and LeptonCount == 0:
    ch = 10
  if HadronCount == 2 and LeptonCount == 0:
    ch = 20
  if HadronCount == 3 and LeptonCount == 0:
    ch = 30
  if HadronCount == 4 and LeptonCount == 0:
    ch = 40
  if HadronCount == 5 and LeptonCount == 0:
    ch = 50
  if HadronCount == 6 and LeptonCount == 0:
    ch = 60
  if HadronCount == 0 and LeptonCount == 1:
    ch = 1
  if HadronCount == 1 and LeptonCount == 1:
    ch = 11
  if HadronCount == 2 and LeptonCount == 1:
    ch = 21
  if HadronCount == 3 and LeptonCount == 1:
    ch = 31
  if HadronCount == 4 and LeptonCount == 1:
    ch = 41
  if HadronCount == 5 and LeptonCount == 1:
    ch = 51
  if HadronCount == 0 and LeptonCount == 2:
    ch = 2
  if HadronCount == 1 and LeptonCount == 2:
    ch = 12
  if HadronCount == 2 and LeptonCount == 2:
    ch = 22
  if HadronCount == 3 and LeptonCount == 2:
    ch = 32
  if HadronCount == 4 and LeptonCount == 2:
    ch = 42
  if HadronCount == 5 and LeptonCount == 2:
    ch = 52
  if HadronCount == 0 and LeptonCount == 3:
    ch = 3
  if HadronCount == 1 and LeptonCount == 3:
    ch = 13
  if HadronCount == 2 and LeptonCount == 3:
    ch = 23
  if HadronCount == 3 and LeptonCount == 3:
    ch = 33
  if HadronCount == 4 and LeptonCount == 3:
    ch = 43
  if HadronCount == 5 and LeptonCount == 3:
    ch = 53
  return ch

for event in xrange(nEnt):

  cret.GetEntry(event)

  if (cret.IntInGeo.at(0)):

    CDauPdg = []
    LS = []
    DSS = []

    for vtx in xrange(cret.VertexInfo.size()):

      if cret.VertexInfo.at(vtx) == 1:
        Pos = []
        Pos.append(cret.StartX.at(vtx))
        Pos.append(cret.StartY.at(vtx))
        Pos.append(cret.StartZ.at(vtx))
        Mom = []
        Mom.append(cret.Px.at(vtx))
        Mom.append(cret.Py.at(vtx))
        Mom.append(cret.Pz.at(vtx))
        Mom.append(cret.P.at(vtx))
        Pdg = cret.PdgCode.at(vtx)
        if Pdg in CharmedHadron:
          CMom = []
          CMom.append(cret.Px.at(vtx))
          CMom.append(cret.Py.at(vtx))
          CMom.append(cret.Pz.at(vtx))
          CMom.append(cret.P.at(vtx))
          CharmFraction(Pdg, h['charm_fraction'], CCounter)
        if LocationSelection(Mom, Pdg):
          LS.append(True)
        else: LS.append(False)

      if cret.VertexInfo.at(vtx) == 22:
        CDauPos = []
        CDauPos.append(cret.StartX.at(vtx))
        CDauPos.append(cret.StartY.at(vtx))
        CDauPos.append(cret.StartZ.at(vtx))
        CDauMom = []
        CDauMom.append(cret.Px.at(vtx))
        CDauMom.append(cret.Py.at(vtx))
        CDauMom.append(cret.Pz.at(vtx))
        CDauMom.append(cret.P.at(vtx))
        CDauPdg.append(cret.PdgCode.at(vtx))

      try: Pos, CMom, CDauPos, CDauMom
      except NameError: continue
      else:
        if DecaySearchSelection(Pos, CMom, CDauPos, CDauMom):
          DSS.append(True)
          del CDauPos, CDauMom
        else:
          DSS.append(False)

    a += 1.

    dc = ChannelDecision(CDauPdg)

    if dc == 0:
      if GeometrySelection(Pos):
        b += 1.
        h0l0_g.append(True)
      else: h0l0_g.append(False)
      if True in LS:
        c += 1.
        h0l0_l.append(True)
      else: h0l0_l.append(False)
      if True in DSS:
        d += 1.
        h0l0_ds.append(True)
      else: h0l0_ds.append(False)

    if dc == 1:
      if GeometrySelection(Pos):
        b += 1.
        h0l1_g.append(True)
      else: h0l1_g.append(False)
      if True in LS:
        c += 1.
        h0l1_l.append(True)
      else: h0l1_l.append(False)
      if True in DSS:
        d += 1.
        h0l1_ds.append(True)
      else: h0l1_ds.append(False)

    if dc == 2:
      if GeometrySelection(Pos):
        b += 1.
        h0l2_g.append(True)
      else: h0l2_g.append(False)
      if True in LS:
        c += 1.
        h0l2_l.append(True)
      else: h0l2_l.append(False)
      if True in DSS:
        d += 1.
        h0l2_ds.append(True)
      else: h0l2_ds.append(False)

    if dc == 3:
      if GeometrySelection(Pos):
        b += 1.
        h0l2_g.append(True)
      else: h0l2_g.append(False)
      if True in LS:
        c += 1.
        h0l2_l.append(True)
      else: h0l2_l.append(False)
      if True in DSS:
        d += 1.
        h0l2_ds.append(True)
      else: h0l2_ds.append(False)

    if dc == 10:
      if GeometrySelection(Pos):
        b += 1.
        h1l0_g.append(True)
      else: h1l0_g.append(False)
      if True in LS:
        c += 1.
        h1l0_l.append(True)
      else: h1l0_l.append(False)
      if True in DSS:
        d += 1.
        h1l0_ds.append(True)
      else: h1l0_ds.append(False)

    if dc == 11:
      if GeometrySelection(Pos):
        b += 1.
        h1l1_g.append(True)
      else: h1l1_g.append(False)
      if True in LS:
        c += 1.
        h1l1_l.append(True)
      else: h1l1_l.append(False)
      if True in DSS:
        d += 1.
        h1l1_ds.append(True)
      else: h1l1_ds.append(False)

    if dc == 12:
      if GeometrySelection(Pos):
        b += 1.
        h1l2_g.append(True)
      else: h1l2_g.append(False)
      if True in LS:
        c += 1.
        h1l2_l.append(True)
      else: h1l2_l.append(False)
      if True in DSS:
        d += 1.
        h1l2_ds.append(True)
      else: h1l2_ds.append(False)

    if dc == 13:
      if GeometrySelection(Pos):
        b += 1.
        h1l3_g.append(True)
      else: h1l3_g.append(False)
      if True in LS:
        c += 1.
        h1l3_l.append(True)
      else: h1l3_l.append(False)
      if True in DSS:
        d += 1.
        h1l3_ds.append(True)
      else: h1l3_ds.append(False)

    if dc == 20:
      if GeometrySelection(Pos):
        b += 1.
        h2l0_g.append(True)
      else: h2l0_g.append(False)
      if True in LS:
        c += 1.
        h2l0_l.append(True)
      else: h2l0_l.append(False)
      if True in DSS:
        d += 1.
        h2l0_ds.append(True)
      else: h2l0_ds.append(False)

    if dc == 21:
      if GeometrySelection(Pos):
        b += 1.
        h2l1_g.append(True)
      else: h2l1_g.append(False)
      if True in LS:
        c += 1.
        h2l1_l.append(True)
      else: h2l1_l.append(False)
      if True in DSS:
        d += 1.
        h2l1_ds.append(True)
      else: h2l1_ds.append(False)

    if dc == 22:
      if GeometrySelection(Pos):
        b += 1.
        h2l2_g.append(True)
      else: h2l2_g.append(False)
      if True in LS:
        c += 1.
        h2l2_l.append(True)
      else: h2l2_l.append(False)
      if True in DSS:
        d += 1.
        h2l2_ds.append(True)
      else: h2l2_ds.append(False)

    if dc == 23:
      if GeometrySelection(Pos):
        b += 1.
        h2l3_g.append(True)
      else: h2l3_g.append(False)
      if True in LS:
        c += 1.
        h2l3_l.append(True)
      else: h2l3_l.append(False)
      if True in DSS:
        d += 1.
        h2l3_ds.append(True)
      else: h2l3_ds.append(False)

    if dc == 30:
      if GeometrySelection(Pos):
        b += 1.
        h3l0_g.append(True)
      else: h3l0_g.append(False)
      if True in LS:
        c += 1.
        h3l0_l.append(True)
      else: h3l0_l.append(False)
      if True in DSS:
        d += 1.
        h3l0_ds.append(True)
      else: h3l0_ds.append(False)

    if dc == 31:
      if GeometrySelection(Pos):
        b += 1.
        h3l1_g.append(True)
      else: h3l1_g.append(False)
      if True in LS:
        c += 1.
        h3l1_l.append(True)
      else: h3l1_l.append(False)
      if True in DSS:
        d += 1.
        h3l1_ds.append(True)
      else: h3l1_ds.append(False)

    if dc == 32:
      if GeometrySelection(Pos):
        b += 1.
        h3l2_g.append(True)
      else: h3l2_g.append(False)
      if True in LS:
        c += 1.
        h3l2_l.append(True)
      else: h3l2_l.append(False)
      if True in DSS:
        d += 1.
        h3l2_ds.append(True)
      else: h3l2_ds.append(False)

    if dc == 33:
      if GeometrySelection(Pos):
        b += 1.
        h3l3_g.append(True)
      else: h3l3_g.append(False)
      if True in LS:
        c += 1.
        h3l3_l.append(True)
      else: h3l3_l.append(False)
      if True in DSS:
        d += 1.
        h3l3_ds.append(True)
      else: h3l3_ds.append(False)

    if dc == 40:
      if GeometrySelection(Pos):
        b += 1.
        h4l0_g.append(True)
      else: h4l0_g.append(False)
      if True in LS:
        c += 1.
        h4l0_l.append(True)
      else: h4l0_l.append(False)
      if True in DSS:
        d += 1.
        h4l0_ds.append(True)
      else: h4l0_ds.append(False)

    if dc == 41:
      if GeometrySelection(Pos):
        b += 1.
        h4l1_g.append(True)
      else: h4l1_g.append(False)
      if True in LS:
        c += 1.
        h4l1_l.append(True)
      else: h4l1_l.append(False)
      if True in DSS:
        d += 1.
        h4l1_ds.append(True)
      else: h4l1_ds.append(False)

    if dc == 42:
      if GeometrySelection(Pos):
        b += 1.
        h4l2_g.append(True)
      else: h4l2_g.append(False)
      if True in LS:
        c += 1.
        h4l2_l.append(True)
      else: h4l2_l.append(False)
      if True in DSS:
        d += 1.
        h4l2_ds.append(True)
      else: h4l2_ds.append(False)

    if dc == 43:
      if GeometrySelection(Pos):
        b += 1.
        h4l3.append(True)
      else: h4l3.append(False)
      if True in LS:
        c += 1.
        h4l3_l.append(True)
      else: h4l3_l.append(False)
      if True in DSS:
        d += 1.
        h4l3_ds.append(True)
      else: h4l3_ds.append(False)

    if dc == 50:
      if GeometrySelection(Pos):
        b += 1.
        h5l0_g.append(True)
      else: h5l0_g.append(False)
      if True in LS:
        c += 1.
        h5l0_l.append(True)
      else: h5l0_l.append(False)
      if True in DSS:
        d += 1.
        h5l0_ds.append(True)
      else: h5l0_ds.append(False)

    if dc == 51:
      if GeometrySelection(Pos):
        b += 1.
        h5l1_g.append(True)
      else: h5l1_g.append(False)
      if True in LS:
        c += 1.
        h5l1_l.append(True)
      else: h5l1_l.append(False)
      if True in DSS:
        d += 1.
        h5l1_ds.append(True)
      else: h5l1_ds.append(False)

    if dc == 52:
      if GeometrySelection(Pos):
        b += 1.
        h5l2_g.append(True)
      else: h5l2_g.append(False)
      if True in LS:
        c += 1.
        h5l2_l.append(True)
      else: h5l2_l.append(False)
      if True in DSS:
        d += 1.
        h5l2_ds.append(True)
      else: h5l2_ds.append(False)

    if dc == 53:
      if GeometrySelection(Pos):
        b += 1.
        h5l3_g.append(True)
      else: h5l3_g.append(False)
      if True in LS:
        c += 1.
        h5l3_l.append(True)
      else: h5l3_l.append(False)
      if True in DSS:
        d += 1.
        h5l3_ds.append(True)
      else: h5l3_ds.append(False)

    if dc == 60:
      if GeometrySelection(Pos):
        b += 1.
        h6l0_g.append(True)
      else: h6l0_g.append(False)
      if True in LS:
        c += 1.
        h6l0_l.append(True)
      else: h6l0_l.append(False)
      if True in DSS:
        d += 1.
        h6l0_ds.append(True)
      else: h6l0_ds.append(False)

print 'h0l0_g', float(h0l0_g.count(True))/float(len(h0l0_g))*100
print 'h0l1_g', float(h0l1_g.count(True))/float(len(h0l1_g))*100
print 'h0l2_g', float(h0l2_g.count(True))/float(len(h0l2_g))*100
#print 'h0l3_g', float(h0l3_g.count(True))/float(len(h0l3_g))*100
print 'h1l0_g', float(h1l0_g.count(True))/float(len(h1l0_g))*100
print 'h1l1_g', float(h1l1_g.count(True))/float(len(h1l1_g))*100
print 'h1l2_g', float(h1l2_g.count(True))/float(len(h1l2_g))*100
#print 'h1l3_g', float(h1l3_g.count(True))/float(len(h1l3_g))*100
print 'h2l0_g', float(h2l0_g.count(True))/float(len(h2l0_g))*100
print 'h2l1_g', float(h2l1_g.count(True))/float(len(h2l1_g))*100
print 'h2l2_g', float(h2l2_g.count(True))/float(len(h2l2_g))*100
#print 'h2l3_g', float(h2l3_g.count(True))/float(len(h2l3_g))*100
print 'h3l0_g', float(h3l0_g.count(True))/float(len(h3l0_g))*100
print 'h3l1_g', float(h3l1_g.count(True))/float(len(h3l1_g))*100
print 'h3l2_g', float(h3l2_g.count(True))/float(len(h3l2_g))*100
#print 'h3l3_g', float(h3l3_g.count(True))/float(len(h3l3_g))*100
print 'h4l0_g', float(h4l0_g.count(True))/float(len(h4l0_g))*100
print 'h4l1_g', float(h4l1_g.count(True))/float(len(h4l1_g))*100
print 'h4l2_g', float(h4l2_g.count(True))/float(len(h4l2_g))*100
#print 'h4l3_g', float(h4l3_g.count(True))/float(len(h4l3_g))*100
print 'h5l0_g', float(h5l0_g.count(True))/float(len(h5l0_g))*100
#print 'h5l1_g', float(h5l1_g.count(True))/float(len(h5l1_g))*100
#print 'h5l2_g', float(h5l2_g.count(True))/float(len(h5l2_g))*100
#print 'h5l3_g', float(h5l3_g.count(True))/float(len(h5l3_g))*100
print 'h6l0_g', float(h6l0_g.count(True))/float(len(h6l0_g))*100

print '********************************************************'

print 'h0l0_l', float(h0l0_l.count(True))/float(len(h0l0_l))*100
print 'h0l1_l', float(h0l1_l.count(True))/float(len(h0l1_l))*100
print 'h0l2_l', float(h0l2_l.count(True))/float(len(h0l2_l))*100
#print 'h0l3_l', float(h0l3_l.count(True))/float(len(h0l3_l))*100
print 'h1l0_l', float(h1l0_l.count(True))/float(len(h1l0_l))*100
print 'h1l1_l', float(h1l1_l.count(True))/float(len(h1l1_l))*100
print 'h1l2_l', float(h1l2_l.count(True))/float(len(h1l2_l))*100
#print 'h1l3_l', float(h1l3_l.count(True))/float(len(h1l3_l))*100
print 'h2l0_l', float(h2l0_l.count(True))/float(len(h2l0_l))*100
print 'h2l1_l', float(h2l1_l.count(True))/float(len(h2l1_l))*100
print 'h2l2_l', float(h2l2_l.count(True))/float(len(h2l2_l))*100
#print 'h2l3_l', float(h2l3_l.count(True))/float(len(h2l3_l))*100
print 'h3l0_l', float(h3l0_l.count(True))/float(len(h3l0_l))*100
print 'h3l1_l', float(h3l1_l.count(True))/float(len(h3l1_l))*100
print 'h3l2_l', float(h3l2_l.count(True))/float(len(h3l2_l))*100
#print 'h3l3_l', float(h3l3_l.count(True))/float(len(h3l3_l))*100
print 'h4l0_l', float(h4l0_l.count(True))/float(len(h4l0_l))*100
print 'h4l1_l', float(h4l1_l.count(True))/float(len(h4l1_l))*100
print 'h4l2_l', float(h4l2_l.count(True))/float(len(h4l2_l))*100
#print 'h4l3_l', float(h4l3_l.count(True))/float(len(h4l3_l))*100
print 'h5l0_l', float(h5l0_l.count(True))/float(len(h5l0_l))*100
#print 'h5l1_l', float(h5l1_l.count(True))/float(len(h5l1_l))*100
#print 'h5l2_l', float(h5l2_l.count(True))/float(len(h5l2_l))*100
#print 'h5l3_l', float(h5l3_l.count(True))/float(len(h5l3_l))*100
print 'h6l0_l', float(h6l0_l.count(True))/float(len(h6l0_l))*100

print '********************************************************'

print 'h0l0_ds', float(h0l0_ds.count(True))/float(len(h0l0_ds))*100
print 'h0l1_ds', float(h0l1_ds.count(True))/float(len(h0l1_ds))*100
print 'h0l2_ds', float(h0l2_ds.count(True))/float(len(h0l2_ds))*100
#print 'h0l3_ds', float(h0l3_ds.count(True))/float(len(h0l3_ds))*100
print 'h1l0_ds', float(h1l0_ds.count(True))/float(len(h1l0_ds))*100
print 'h1l1_ds', float(h1l1_ds.count(True))/float(len(h1l1_ds))*100
print 'h1l2_ds', float(h1l2_ds.count(True))/float(len(h1l2_ds))*100
#print 'h1l3_ds', float(h1l3_ds.count(True))/float(len(h1l3_ds))*100
print 'h2l0_ds', float(h2l0_ds.count(True))/float(len(h2l0_ds))*100
print 'h2l1_ds', float(h2l1_ds.count(True))/float(len(h2l1_ds))*100
print 'h2l2_ds', float(h2l2_ds.count(True))/float(len(h2l2_ds))*100
#print 'h2l3_ds', float(h2l3_ds.count(True))/float(len(h2l3_ds))*100
print 'h3l0_ds', float(h3l0_ds.count(True))/float(len(h3l0_ds))*100
print 'h3l1_ds', float(h3l1_ds.count(True))/float(len(h3l1_ds))*100
print 'h3l2_ds', float(h3l2_ds.count(True))/float(len(h3l2_ds))*100
#print 'h3l3_ds', float(h3l3_ds.count(True))/float(len(h3l3_ds))*100
print 'h4l0_ds', float(h4l0_ds.count(True))/float(len(h4l0_ds))*100
print 'h4l1_ds', float(h4l1_ds.count(True))/float(len(h4l1_ds))*100
print 'h4l2_ds', float(h4l2_ds.count(True))/float(len(h4l2_ds))*100
#print 'h4l3_ds', float(h4l3_ds.count(True))/float(len(h4l3_ds))*100
print 'h5l0_ds', float(h5l0_ds.count(True))/float(len(h5l0_ds))*100
#print 'h5l1_ds', float(h5l1_ds.count(True))/float(len(h5l1_ds))*100
#print 'h5l2_ds', float(h5l2_ds.count(True))/float(len(h5l2_ds))*100
#print 'h5l3_ds', float(h5l3_ds.count(True))/float(len(h5l3_ds))*100
print 'h6l0_ds', float(h6l0_ds.count(True))/float(len(h6l0_ds))*100

print '********************************************************'

print 'Geometry Selection Success', b/a*100
print 'Location Selection Success', c/a*100
print 'Decay Search Selection Success', d/a*100

print '********************************************************'

print 'D_minus Fraction', CCounter[0]/sum(CCounter)*100
print 'D_zero Fraction', CCounter[1]/sum(CCounter)*100
print 'Ds_minus Fraction', CCounter[2]/sum(CCounter)*100
print 'Lambda_c Fraction', CCounter[3]/sum(CCounter)*100

print '====END OF THE RESULTS===='

makePlots()

#h['slope'].Draw()
#h['slope_acc'].Draw("same")
#h['slope_acc'].Sumw2

#h['test'].Divide(h['slope_acc'], h['slope'], 1., 1., "B")
#h['test'].Draw()

#total = h['slope'].Integral()
#selected = h['slope_acc'].Integral()
#print selected/total*100

'''
note1 = r.TLatex(0.25, 2000, "~23.42%")
note2 = r.TLatex(1.25, 2000, "~50.86%")
note3 = r.TLatex(2.25, 2000, "~12.37%")
note4 = r.TLatex(3.25, 2000, "~13.36%")

note1.Draw("Same")
note2.Draw("Same")
note3.Draw("Same")
note4.Draw("Same")

c.Print('cratio_nu_mu.pdf')

tot = d_plus + d_zero + ds_plus + lambda_c
print 'D_+', d_plus/tot*100
print 'D_0', d_zero/tot*100
print 'Ds_+', ds_plus/tot*100
print 'Lambda_c+', lambda_c/tot*100
'''
