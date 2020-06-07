import ROOT as r
import rootUtils as ut
import time

from physlib import *
from tabulate import tabulate
from progress.bar import Bar

#start_time = time.time()

work_dir="/eos/experiment/ship/user/eelikkaya/dev"
geo_file="/eos/experiment/ship/user/eelikkaya/dev/geofile_full.conical.Genie-TGeant4.root"
flavor={ 'mu' : ['nu_mu', '#nu_#mu'] }

""" Selection rules are defined here. """
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
  fGeo.SetCurrentPoint(Pos[0], Pos[1], Pos[2]+0.5)
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

def DecaySearchSelection(fL, kA, iP, oA): #FlightLength, KinkAngle, ImpactParameter
  dsCheck = []
  if fL < 4.:
    dsCheck.append(True)
  if iP > 10.0:
    dsCheck.append(True)
  if kA>20.0:   #in mrad
    dsCheck.append(True)
  if oA>10.0:   #in mrad
    dsCheck.append(True)
  if sum(dsCheck) != 4: return False
  return True


""" Histograms and plots are defined here. """
h = {}

# Incoming Neutrino Beam Energy After Selections
ut.bookHist(h, 'nuE',    'Neutrino Beam Energy #nu_{#mu}',                         60, 0, 300)
ut.bookHist(h, 'g-nuEs', 'Neutrino Beam Energy #nu_{#mu}: Geometric Selection',    60, 0, 300)
ut.bookHist(h, 'l-nuEs', 'Neutrino Beam Energy #nu_{#mu}: Location Selection',     60, 0, 300)
ut.bookHist(h, 'd-nuEs', 'Neutrino Beam Energy #nu_{#mu}: Decay Search Selection', 60, 0, 300)
# Efficiencies Respect to Selections with Neutrino Energy
ut.bookHist(h, 'g-nuEff', 'Efficiency Plot #nu_{#mu}: Geometric Selection',    60, 0, 300)
ut.bookHist(h, 'l-nuEff', 'Efficiency Plot #nu_{#mu}: Location Selection',     60, 0, 300)
ut.bookHist(h, 'd-nuEff', 'Efficiency Plot #nu_{#mu}: Decay Search Selection', 60, 0, 300)
# Incoming Neutrino Beam Energy Respect to Induced Charm Flavor
ut.bookHist(h, 'nuE1',    'Neutrino Beam Energy #nu_{#mu}: Induces D{+}',                         60, 0, 300)
ut.bookHist(h, 'nuE2',    'Neutrino Beam Energy #nu_{#mu}: Induces D{0}',                         60, 0, 300)
ut.bookHist(h, 'nuE3',    'Neutrino Beam Energy #nu_{#mu}: Induces D_{s}^{0}',                    60, 0, 300)
ut.bookHist(h, 'nuE4',    'Neutrino Beam Energy #nu_{#mu}: Induces L_{c}^{+}',                    60, 0, 300)
ut.bookHist(h, 'd-nuEs1',    'Neutrino Beam Energy #nu_{#mu}: Decay Search Selection Induces D{+}',                         60, 0, 300)
ut.bookHist(h, 'd-nuEs2',    'Neutrino Beam Energy #nu_{#mu}: Decay Search Selection Induces D{0}',                         60, 0, 300)
ut.bookHist(h, 'd-nuEs3',    'Neutrino Beam Energy #nu_{#mu}: Decay Search Selection Induces D_{s}^{0}',                    60, 0, 300)
ut.bookHist(h, 'd-nuEs4',    'Neutrino Beam Energy #nu_{#mu}: Decay Search Selection Induces L_{c}^{+}',                    60, 0, 300)
# DSS Efficiencies Respect Charm Flavor with Neutrino Energy
ut.bookHist(h, 'd-nuEff1', 'Efficiency Plot #nu_{#mu}: Decay Search Selection', 60, 0, 300)
ut.bookHist(h, 'd-nuEff2', 'Efficiency Plot #nu_{#mu}: Decay Search Selection', 60, 0, 300)
ut.bookHist(h, 'd-nuEff3', 'Efficiency Plot #nu_{#mu}: Decay Search Selection', 60, 0, 300)
ut.bookHist(h, 'd-nuEff4', 'Efficiency Plot #nu_{#mu}: Decay Search Selection', 60, 0, 300)
# Multiplicity at Neutrino Vertex
ut.bookHist(h, 'dC1M',      'Charmed Hadron Multiplicity at Primary Vertex D+',                 15, 0, 15)
ut.bookHist(h, 'dC1MS',     'Charmed Hadron Multiplicity at Primary Vertex D+ (Selected)',      15, 0, 15)
ut.bookHist(h, 'dC2M',      'Charmed Hadron Multiplicity at Primary Vertex D0',                 15, 0, 15)
ut.bookHist(h, 'dC2MS',     'Charmed Hadron Multiplicity at Primary Vertex D0 (Selected)',      15, 0, 15)
ut.bookHist(h, 'dC3M',      'Charmed Hadron Multiplicity at Primary Vertex Ds+',                15, 0, 15)
ut.bookHist(h, 'dC3MS',     'Charmed Hadron Multiplicity at Primary Vertex Ds+ (Selected)',     15, 0, 15)
ut.bookHist(h, 'dC4M',      'Charmed Hadron Multiplicity at Primary Vertex Lc+',                15, 0, 15)
ut.bookHist(h, 'dC4MS',     'Charmed Hadron Multiplicity at Primary Vertex Lc+ (Selected)',     15, 0, 15)
# Multiplicity at Charm Vertex
ut.bookHist(h, 'dC1M2',     'Charmed Hadron Multiplicity at Secondary Vertex D+',               8, 0, 8)
ut.bookHist(h, 'dC1M2S',    'Charmed Hadron Multiplicity at Secondary Vertex D+ (Selected)',    8, 0, 8)
ut.bookHist(h, 'dC2M2',     'Charmed Hadron Multiplicity at Secondary Vertex D0',               8, 0, 8)
ut.bookHist(h, 'dC2M2S',    'Charmed Hadron Multiplicity at Secondary Vertex D0 (Selected)',    8, 0, 8)
ut.bookHist(h, 'dC3M2',     'Charmed Hadron Multiplicity at Secondary Vertex Ds+',              8, 0, 8)
ut.bookHist(h, 'dC3M2S',    'Charmed Hadron Multiplicity at Secondary Vertex Ds+ (Selected)',   8, 0, 8)
ut.bookHist(h, 'dC4M2',     'Charmed Hadron Multiplicity at Secondary Vertex Lc+',              8, 0, 8)
ut.bookHist(h, 'dC4M2S',    'Charmed Hadron Multiplicity at Secondary Vertex Lc+ (Selected)',   8, 0, 8)
# Bjorken X and Inelasticity Y Distributions
ut.bookHist(h, 'BjorX',     'Bjorken X Distribution',                 100, 0, 1)
ut.bookHist(h, 'BjorXs',    'Bjorken X Distribution (Selected)',      100, 0, 1)
ut.bookHist(h, 'InelY',     'Inelasticity Y Distribution',            100, 0, 1)
ut.bookHist(h, 'InelYs',    'Inelasticity Y Distribution (Selected)', 100, 0, 1)
# Neutrino Interaction Points in X-Y-Z
ut.bookHist(h, 'tp',  'Neutrino Interactions at Transverse Plane',            100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'tpS', 'Neutrino Interactions at Transverse Plane (Selected)', 100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'za',  'Interactions at z-axis',            400, -3300, -2900)
ut.bookHist(h, 'zaS', 'Interactions at z-axis (Selected)', 400, -3300, -2900)
# Angular Distribution of Neutrinos in X and Y axis
ut.bookHist(h, 'nuAngDistXF',    'Angular Distribution: Full Spectrum in X-axis',            240, -12, 12)
ut.bookHist(h, 'nuAngDistYF',    'Angular Distribution: Full Spectrum in Y-axis',            240, -12, 12)
ut.bookHist(h, 'd-nuAngDistXFs', 'Angular Distribution: Full Spectrum in X-axis (Selected)', 240, -12, 12)
ut.bookHist(h, 'd-nuAngDistYFs', 'Angular Distribution: Full Spectrum in Y-axis (Selected)', 240, -12, 12)
ut.bookHist(h, 'nuAng2DF',       'Angular Distribution: Full Spectrum in X-Y',               240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'd-nuAng2DFs',    'Angular Distribution: Full Spectrum in X-Y (Selected)',    240, -12, 12, 240, -12, 12)
# Charmed Hadron Energy Spectrum
ut.bookHist(h, 'dC1E',      'Charmed Hadron Energy Spectrum D+',                40, 0, 100)
ut.bookHist(h, 'dC1ES',     'Charmed Hadron Energy Spectrum D+ (Selected)',     40, 0, 100)
ut.bookHist(h, 'dC2E',      'Charmed Hadron Energy Spectrum D0',                40, 0, 100)
ut.bookHist(h, 'dC2ES',     'Charmed Hadron Energy Spectrum D0 (Selected)',     40, 0, 100)
ut.bookHist(h, 'dC3E',      'Charmed Hadron Energy Spectrum Ds+',               40, 0, 100)
ut.bookHist(h, 'dC3ES',     'Charmed Hadron Energy Spectrum Ds+ (Selected)',    40, 0, 100)
ut.bookHist(h, 'dC4E',      'Charmed Hadron Energy Spectrum Lc+',               40, 0, 100)
ut.bookHist(h, 'dC4ES',     'Charmed Hadron Energy Spectrum Lc+ (Selected)',    40, 0, 100)
# Charmed Hadron Flight Length
ut.bookHist(h, 'dC1FL',     'Charmed Hadron Flight Length D+',                  50, 0, 10)
ut.bookHist(h, 'dC1FLS',    'Charmed Hadron Flight Length D+ (Selected)',       50, 0, 10)
ut.bookHist(h, 'dC2FL',     'Charmed Hadron Flight Length D0',                  50, 0, 10)
ut.bookHist(h, 'dC2FLS',    'Charmed Hadron Flight Length D0 (Selected)',       50, 0, 10)
ut.bookHist(h, 'dC3FL',     'Charmed Hadron Flight Length Ds+',                 50, 0, 10)
ut.bookHist(h, 'dC3FLS',    'Charmed Hadron Flight Length Ds+ (Selected)',      50, 0, 10)
ut.bookHist(h, 'dC4FL',     'Charmed Hadron Flight Length Lc+',                 50, 0, 10)
ut.bookHist(h, 'dC4FLS',    'Charmed Hadron Flight Length Lc+ (Selected)',      50, 0, 10)
# Charmed Hadron Impact Parameter
ut.bookHist(h, 'dC1IP',     'Charmed Hadron Impact Parameter D+',                  100, 0, 500)
ut.bookHist(h, 'dC1IPS',    'Charmed Hadron Impact Parameter D+ (Selected)',       100, 0, 500)
ut.bookHist(h, 'dC2IP',     'Charmed Hadron Impact Parameter D0',                  100, 0, 500)
ut.bookHist(h, 'dC2IPS',    'Charmed Hadron Impact Parameter D0 (Selected)',       100, 0, 500)
ut.bookHist(h, 'dC3IP',     'Charmed Hadron Impact Parameter Ds+',                 100, 0, 500)
ut.bookHist(h, 'dC3IPS',    'Charmed Hadron Impact Parameter Ds+ (Selected)',      100, 0, 500)
ut.bookHist(h, 'dC4IP',     'Charmed Hadron Impact Parameter Lc+',                 100, 0, 500)
ut.bookHist(h, 'dC4IPS',    'Charmed Hadron Impact Parameter Lc+ (Selected)',      100, 0, 500)
# Charmed Hadron Kink and Opening Angle
ut.bookHist(h, 'dC1KA',     'Kink Angle at Charm Vertex D+',                    50, 0, 1)
ut.bookHist(h, 'dC1KAS',    'Kink Angle at Charm Vertex D+ (Selected)',         50, 0, 1)
ut.bookHist(h, 'dC3KA',     'Kink Angle at Charm Vertex Ds+',                   50, 0, 1)
ut.bookHist(h, 'dC3KAS',    'Kink Angle at Charm Vertex Ds+ (Selected)',        50, 0, 1)
ut.bookHist(h, 'dC4KA',     'Kink Angle at Charm Vertex Lc+',                   50, 0, 1)
ut.bookHist(h, 'dC4KAS',    'Kink Angle at Charm Vertex Lc+ (Selected)',        50, 0, 1)
ut.bookHist(h, 'dC2OA',     'Opening Angle at Charm Vertex D0',                 50, 0, 1)
ut.bookHist(h, 'dC2OAS',    'Opening Angle at Charm Vertex D0 (Selected)',      50, 0, 1)

def makePlots():

  # Incoming Neutrino Beam Energy After Selections
  ut.bookCanvas(h,key='CnuE',title='Incoming Neutrino Beam Energy',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat('mr')
  cv = h['CnuE'].cd(1)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  r.gPad.Update()
  sBox_nuE = h['nuE'].FindObject('stats')
  sBox_nuE.SetY1NDC(0.8)
  sBox_nuE.SetY2NDC(0.7)
  h['g-nuEs'].SetFillStyle(3335)
  h['g-nuEs'].SetFillColor(2)
  h['g-nuEs'].Draw('SAMES')
  cv = h['CnuE'].cd(2)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  h['l-nuEs'].SetFillStyle(3335)
  h['l-nuEs'].SetFillColor(2)
  h['l-nuEs'].Draw('SAMES')
  cv = h['CnuE'].cd(3)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  h['d-nuEs'].SetFillStyle(3335)
  h['d-nuEs'].SetFillColor(2)
  h['d-nuEs'].Draw('SAMES')
  h['CnuE'].Print(work_dir+'/Histograms/CnuE.pdf')

  # Efficiencies Respect to Selections with Neutrino Energy
  ut.bookCanvas(h,key='CnuEff',title='Efficiency Plot',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEff'].cd(1)
  h['nuE'].Draw()
  h['g-nuEs'].Draw()
  h['g-nuEs'].Sumw2()
  h['g-nuEff'].Divide(h['g-nuEs'],h['nuE'],1.,1.,'B')
  h['g-nuEff'].Draw('E0')
  h['g-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(2)
  h['nuE'].Draw()
  h['l-nuEs'].Draw()
  h['l-nuEs'].Sumw2()
  h['l-nuEff'].Divide(h['l-nuEs'],h['nuE'],1.,1.,'B')
  h['l-nuEff'].Draw('E0')
  h['l-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(3)
  h['nuE'].Draw()
  h['d-nuEs'].Draw()
  h['d-nuEs'].Sumw2()
  h['d-nuEff'].Divide(h['d-nuEs'],h['nuE'],1.,1.,'B')
  h['d-nuEff'].Draw('E0')
  h['d-nuEff'].SetXTitle('Energy (GeV)')
  h['CnuEff'].Print(work_dir+'/Histograms/CnuEff.pdf')

  # Incoming Neutrino Beam Energy Respect to Induced Charm Flavor
  ut.bookCanvas(h,key='CnuEX',title='Incoming Neutrino Beam Energy',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat('mr')
  cv = h['CnuEX'].cd(1)
  h['nuE1'].Draw()
  h['nuE1'].SetXTitle('Energy (GeV)')
  r.gPad.Update()
  sBox_nuE = h['nuE1'].FindObject('stats')
  sBox_nuE.SetY1NDC(0.8)
  sBox_nuE.SetY2NDC(0.7)
  h['d-nuEs1'].SetFillStyle(3335)
  h['d-nuEs1'].SetFillColor(2)
  h['d-nuEs1'].Draw('SAMES')
  cv = h['CnuEX'].cd(2)
  h['nuE2'].Draw()
  h['nuE2'].SetXTitle('Energy (GeV)')
  h['d-nuEs2'].SetFillStyle(3335)
  h['d-nuEs2'].SetFillColor(2)
  h['d-nuEs2'].Draw('SAMES')
  cv = h['CnuEX'].cd(3)
  h['nuE3'].Draw()
  h['nuE3'].SetXTitle('Energy (GeV)')
  h['d-nuEs3'].SetFillStyle(3335)
  h['d-nuEs3'].SetFillColor(2)
  h['d-nuEs3'].Draw('SAMES')
  cv = h['CnuEX'].cd(4)
  h['nuE4'].Draw()
  h['nuE4'].SetXTitle('Energy (GeV)')
  h['d-nuEs4'].SetFillStyle(3335)
  h['d-nuEs4'].SetFillColor(2)
  h['d-nuEs4'].Draw('SAMES')
  h['CnuEX'].Print(work_dir+'/Histograms/CnuEX.pdf')

  # DSS Efficiencies Respect Charm Flavor with Neutrino Energy
  ut.bookCanvas(h,key='CnuEffCF',title='Efficiency Plot',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEffCF'].cd(1)
  h['nuE1'].Draw()
  h['d-nuEs1'].Draw()
  h['d-nuEs1'].Sumw2()
  h['d-nuEff1'].Divide(h['d-nuEs1'],h['nuE1'],1.,1.,'B')
  h['d-nuEff1'].Draw('E0')
  h['d-nuEff1'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(2)
  h['nuE2'].Draw()
  h['d-nuEs2'].Draw()
  h['d-nuEs2'].Sumw2()
  h['d-nuEff2'].Divide(h['d-nuEs2'],h['nuE2'],1.,1.,'B')
  h['d-nuEff2'].Draw('E0')
  h['d-nuEff2'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(3)
  h['nuE3'].Draw()
  h['d-nuEs3'].Draw()
  h['d-nuEs3'].Sumw2()
  h['d-nuEff3'].Divide(h['d-nuEs3'],h['nuE3'],1.,1.,'B')
  h['d-nuEff3'].Draw('E0')
  h['d-nuEff3'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(4)
  h['nuE4'].Draw()
  h['d-nuEs4'].Draw()
  h['d-nuEs4'].Sumw2()
  h['d-nuEff4'].Divide(h['d-nuEs4'],h['nuE4'],1.,1.,'B')
  h['d-nuEff4'].Draw('E0')
  h['d-nuEff4'].SetXTitle('Energy (GeV)')
  h['CnuEffCF'].Print(work_dir+'/Histograms/CnuEffCF.pdf')

  #Multiplicity at Neutrino Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis',title='Multiplicity at Neutrino Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dMultAnalysis'].cd(1)
  h['dC1M'].Draw()
  h['dC1MS'].SetFillStyle(3335)
  h['dC1MS'].SetFillColor(2)
  h['dC1MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(2)
  h['dC2M'].Draw()
  h['dC2MS'].SetFillStyle(3335)
  h['dC2MS'].SetFillColor(2)
  h['dC2MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(3)
  h['dC3M'].Draw()
  h['dC3MS'].SetFillStyle(3335)
  h['dC3MS'].SetFillColor(2)
  h['dC3MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(4)
  h['dC4M'].Draw()
  h['dC4MS'].SetFillStyle(3335)
  h['dC4MS'].SetFillColor(2)
  h['dC4MS'].Draw('same')
  h['dMultAnalysis'].Print(work_dir+'/Histograms/dcmult.pdf')

  #Multiplicity at Charm Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis2',title='Multiplicity at Charm Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dMultAnalysis2'].cd(1)
  h['dC1M2'].Draw()
  h['dC1M2S'].SetFillStyle(3335)
  h['dC1M2S'].SetFillColor(2)
  h['dC1M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(2)
  h['dC2M2'].Draw()
  h['dC2M2S'].SetFillStyle(3335)
  h['dC2M2S'].SetFillColor(2)
  h['dC2M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(3)
  h['dC3M2'].Draw()
  h['dC3M2S'].SetFillStyle(3335)
  h['dC3M2S'].SetFillColor(2)
  h['dC3M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(4)
  h['dC4M2'].Draw()
  h['dC4M2S'].SetFillStyle(3335)
  h['dC4M2S'].SetFillColor(2)
  h['dC4M2S'].Draw('same')
  h['dMultAnalysis2'].Print(work_dir+'/Histograms/dcmult2.pdf')

  #Bjorken X distribution
  ut.bookCanvas(h,key='bjor',title='Bjorken X Distribution',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['bjor'].cd(1)
  h['BjorX'].Draw()
  h['BjorXs'].SetFillStyle(3335)
  h['BjorXs'].SetFillColor(2)
  h['BjorXs'].Draw('same')
  h['bjor'].Print(work_dir+'/Histograms/bjorkenX.pdf')

  #Inelasticity Y distribution
  ut.bookCanvas(h,key='inel',title='Inelasticity Y Distribution',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['inel'].cd(1)
  h['InelY'].Draw()
  h['InelYs'].SetFillStyle(3335)
  h['InelYs'].SetFillColor(2)
  h['InelYs'].Draw('same')
  h['inel'].Print(work_dir+'/Histograms/inelasticityY.pdf')

  # Neutrino Interaction Points in X-Y-Z
  ut.bookCanvas(h,key='nutp',title='Transverse Plane Interactions',nx=1920,ny=720,cx=2,cy=1)
  cv = h['nutp'].cd(1)
  h['tp'].Draw('COLZ')
  cv = h['nutp'].cd(2)
  h['tpS'].Draw('COLZ')
  h['nutp'].Print(work_dir+'/Histograms/nutplane.pdf')
  ut.bookCanvas(h,key='zaxis',title='Z Axis Interactions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['zaxis'].cd(1)
  h['za'].Draw()
  h['zaS'].SetFillStyle(3335)
  h['zaS'].SetFillColor(2)
  h['zaS'].Draw('same')
  h['zaxis'].Print(work_dir+'/Histograms/nuZ.pdf')

  #Angular Distribution of Neutrinos X-Y Scatter Plot
  ut.bookCanvas(h,key='CnuAng2D',title='Angular Distribution X-Y Scatter Plot',nx=1920,ny=1080,cx=2,cy=1)
  r.gStyle.SetOptStat(1111)
  cv = h['CnuAng2D'].cd(1)
  h['nuAng2DF'].Draw('COLZ')
  h['nuAng2DF'].SetXTitle('mrad')
  h['nuAng2DF'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(2)
  h['d-nuAng2DFs'].Draw('COLZ')
  h['d-nuAng2DFs'].SetXTitle('mrad')
  h['d-nuAng2DFs'].SetYTitle('mrad')
  h['CnuAng2D'].Print(work_dir+'/Histograms/CnuAng2D.pdf')

  # Charmed Hadron Energy Spectrum
  ut.bookCanvas(h,key='dEnergyAnalysis',title='Produced Charmed Hadron Energies',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dEnergyAnalysis'].cd(1)
  r.gStyle.SetOptStat(1111)
  h['dC1E'].Draw()
  h['dC1E'].SetXTitle('Energy (GeV)')
  h['dC1ES'].SetFillStyle(3335)
  h['dC1ES'].SetFillColor(2)
  h['dC1ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(2)
  h['dC2E'].Draw()
  h['dC2E'].SetXTitle('Energy (GeV)')
  h['dC2ES'].SetFillStyle(3335)
  h['dC2ES'].SetFillColor(2)
  h['dC2ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(3)
  h['dC3E'].Draw()
  h['dC3E'].SetXTitle('Energy (GeV)')
  h['dC3ES'].SetFillStyle(3335)
  h['dC3ES'].SetFillColor(2)
  h['dC3ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(4)
  h['dC4E'].Draw()
  h['dC4E'].SetXTitle('Energy (GeV)')
  h['dC4ES'].SetFillStyle(3335)
  h['dC4ES'].SetFillColor(2)
  h['dC4ES'].Draw('same')
  h['dEnergyAnalysis'].Print(work_dir+'/Histograms/dcenergy.pdf')

  # Charmed Hadron Flight Length
  ut.bookCanvas(h,key='dFLAnalysis',title='Produced Charmed Hadron Flight Lengths',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dFLAnalysis'].cd(1)
  h['dC1FL'].Draw()
  h['dC1FL'].SetXTitle('Decay Length (mm)')
  h['dC1FLS'].SetFillStyle(3335)
  h['dC1FLS'].SetFillColor(2)
  h['dC1FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(2)
  h['dC2FL'].Draw()
  h['dC2FL'].SetXTitle('Decay Length (mm)')
  h['dC2FLS'].SetFillStyle(3335)
  h['dC2FLS'].SetFillColor(2)
  h['dC2FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(3)
  h['dC3FL'].Draw()
  h['dC3FL'].SetXTitle('Decay Length (mm)')
  h['dC3FLS'].SetFillStyle(3335)
  h['dC3FLS'].SetFillColor(2)
  h['dC3FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(4)
  h['dC4FL'].Draw()
  h['dC4FL'].SetXTitle('Decay Length (mm)')
  h['dC4FLS'].SetFillStyle(3335)
  h['dC4FLS'].SetFillColor(2)
  h['dC4FLS'].Draw('same')
  h['dFLAnalysis'].Print(work_dir+'/Histograms/dcfl.pdf')

  # Charmed Hadron Impact Parameter
  ut.bookCanvas(h,key='dIPAnalysis',title='Produced Charmed Hadron Impact Parameters',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dIPAnalysis'].cd(1)
  h['dC1IP'].Draw()
  h['dC1IP'].SetXTitle('Decay Length (#mum)')
  h['dC1IPS'].SetFillStyle(3335)
  h['dC1IPS'].SetFillColor(2)
  h['dC1IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(2)
  h['dC2IP'].Draw()
  h['dC2IP'].SetXTitle('Decay Length (#mum)')
  h['dC2IPS'].SetFillStyle(3335)
  h['dC2IPS'].SetFillColor(2)
  h['dC2IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(3)
  h['dC3IP'].Draw()
  h['dC3IP'].SetXTitle('Decay Length (#mum)')
  h['dC3IPS'].SetFillStyle(3335)
  h['dC3IPS'].SetFillColor(2)
  h['dC3IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(4)
  h['dC4IP'].Draw()
  h['dC4IP'].SetXTitle('Decay Length (#mum)')
  h['dC4IPS'].SetFillStyle(3335)
  h['dC4IPS'].SetFillColor(2)
  h['dC4IPS'].Draw('same')
  h['dIPAnalysis'].Print(work_dir+'/Histograms/dcip.pdf')

  # Charmed Hadron Kink and Opening Angle
  ut.bookCanvas(h,key='kAngle',title='Kink Angle',nx=1920,ny=540,cx=3,cy=1)
  cv = h['kAngle'].cd(1)
  h['dC1KA'].Draw()
  h['dC1KA'].SetXTitle('Kink Angle (rad)')
  h['dC1KAS'].SetFillStyle(3335)
  h['dC1KAS'].SetFillColor(2)
  h['dC1KAS'].Draw('same')
  cv = h['kAngle'].cd(2)
  h['dC3KA'].Draw()
  h['dC3KA'].SetXTitle('Kink Angle (rad)')
  h['dC3KAS'].SetFillStyle(3335)
  h['dC3KAS'].SetFillColor(2)
  h['dC3KAS'].Draw('same')
  cv = h['kAngle'].cd(3)
  h['dC4KA'].Draw()
  h['dC4KA'].SetXTitle('Kink Angle (rad)')
  h['dC4KAS'].SetFillStyle(3335)
  h['dC4KAS'].SetFillColor(2)
  h['dC4KAS'].Draw('same')
  h['kAngle'].Print(work_dir+'/Histograms/kAngle.pdf')
  ut.bookCanvas(h,key='oAngle',title='Opening Angle',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['oAngle'].cd(1)
  h['dC2OA'].Draw()
  h['dC2OA'].SetXTitle('Opening Angle (rad)')
  h['dC2OAS'].SetFillStyle(3335)
  h['dC2OAS'].SetFillColor(2)
  h['dC2OAS'].Draw('same')
  h['oAngle'].Print(work_dir+'/Histograms/oAngle.pdf')


""" Counters and inventories defined here. """
CounterDict = { 'd1' :       ( [0,0,0,0 ] ), 'd3' :       [0,0,0,0], 'd5' :       [0,0,0,0],
                'd00' :      ( [0,0,0,0 ] ), 'd02' :      [0,0,0,0], 'd04' :      [0,0,0,0], 'd06' : [0,0,0,0],
                'dS1' :      ( [0,0,0,0 ] ), 'dS3' :      [0,0,0,0], 'dS5' :      [0,0,0,0],
                'lambdaC1' : ( [0,0,0,0 ] ), 'lambdaC3' : [0,0,0,0], 'lambdaC5' : [0,0,0,0] }

def CalculateEff(tDSS,tIN):
  try:
    eff = float(tDSS)/float(tIN)
    eff = '%.5f' %eff
    return eff
  except ZeroDivisionError:
    eff = str('---x---')
    return eff

PVLepton = { -15, -13, -11, 11, 13, 15 }
Chargeless = { -14, 22, 111, 130, 421, 2112 }
CharmedHadron = { -431, -421, -431, 411, 421, 431, 4122 }


""" Starting to load input files. """
#f = r.TFile(work_dir+'/ship.conical.Genie-TGeant4.root')
f = r.TFile('/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/above/7294896.11/ship.conical.Genie-TGeant4.root')
t = f.cbmsim

g = r.TFile(geo_file)
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

t.GetEntry(0)
mcT = t.MCTrack

#nEnt = t.GetEntries()
nEnt = 2500

bar = Bar('Processing Events', max = nEnt)

for event in xrange(nEnt):

    t.GetEntry(event)
    nTrck = mcT.GetEntries()

    Neutrino = {}
    NeutrinoDaughter = { 'Px' : (), 'Py' : (), 'Pz' : (), 'P' : (),        # Define Neutrino Daughter Dictionary which Contains Tuples
                         'PosX' : (), 'PosY' : (), 'PosZ' : (), 'Pos' : (),
                         'PDG' : () }
    Charm = {}
    CharmDaughter = { 'Px' : (), 'Py' : (), 'Pz' : (), 'P' : (),        # Define Charm Daughter Dictionary which Contains Tuples
                      'PosX' : (), 'PosY' : (), 'PosZ' : (), 'Pos' : (),
                      'PDG' : () }
    Lepton = {}

    GS, LS, DSS = [], [], []        #Selection Counter Arrays
    delEvent = ()        #Prong Selector Parameter Default with False

    if mcT[0].GetPdgCode() == 14:
        Neutrino = { 'E' : mcT[0].GetEnergy(),
                     'Px' : mcT[0].GetPx(),
                     'Py' : mcT[0].GetPy(),
                     'Pz' : mcT[0].GetPz(),
                     'P' : mcT[0].GetP(),
                     'Pos' : () }
    else: print("Neutrino cannot be found!")

    for track in xrange(nTrck):

        if mcT[track].GetMotherId() == 0:
            NeutrinoDaughter['Px'] += mcT[track].GetPx(),
            NeutrinoDaughter['Py'] += mcT[track].GetPy(),
            NeutrinoDaughter['Pz'] += mcT[track].GetPz(),
            NeutrinoDaughter['P'] += mcT[track].GetP(),
            NeutrinoDaughter['PosX'] += mcT[track].GetStartX(),
            NeutrinoDaughter['PosY'] += mcT[track].GetStartY(),
            NeutrinoDaughter['PosZ'] += mcT[track].GetStartZ(),
            NeutrinoDaughter['PDG'] += mcT[track].GetPdgCode(),
            if NeutrinoDaughter['PDG'][-1] in CharmedHadron:
                Charm = { 'E' : mcT[track].GetEnergy(),
                          'Px' : mcT[track].GetPx(),
                          'Py' : mcT[track].GetPy(),
                          'Pz' : mcT[track].GetPz(),
                          'P' : mcT[track].GetP(),
                          'Pos' : (),
                          'PDG' : NeutrinoDaughter['PDG'][-1] }
                CharmTrack = track
            if NeutrinoDaughter['PDG'][-1] in PVLepton:
                Lepton = { 'E' :  mcT[track].GetEnergy(),
                           'Px' : mcT[track].GetPx(),
                           'Py' : mcT[track].GetPy(),
                           'Pz' : mcT[track].GetPz() }

        try: CharmTrack
        except NameError: pass
        else:
            if mcT[track].GetMotherId() == CharmTrack:
                CharmDaughter['Px'] += mcT[track].GetPx(),
                CharmDaughter['Py'] += mcT[track].GetPy(),
                CharmDaughter['Pz'] += mcT[track].GetPz(),
                CharmDaughter['P'] += mcT[track].GetP(),
                CharmDaughter['PosX'] += mcT[track].GetStartX(),
                CharmDaughter['PosY'] += mcT[track].GetStartY(),
                CharmDaughter['PosZ'] += mcT[track].GetStartZ(),
                CharmDaughter['PDG'] += mcT[track].GetPdgCode(),

    Neutrino['Pos'] += NeutrinoDaughter['PosX'][0], NeutrinoDaughter['PosY'][0], NeutrinoDaughter['PosZ'][0],        ## Anyway the neutrino decays at one of its daughters start point and Charm is one of them
    Charm['Pos'] += CharmDaughter['PosX'][0], CharmDaughter['PosY'][0], CharmDaughter['PosZ'][0],        ## Anyway the charm decays at one of its daughters start point and so on..

    """ Check if the event is usable. """
    # Neutrino interaction should be inside the Nu Target
    fGeo.SetCurrentPoint( Neutrino['Pos'][0],
                          Neutrino['Pos'][1],
                          Neutrino['Pos'][2], )
    fGeo.FindNode()
    if fGeo.GetCurrentVolume().GetName() != ( "Lead" or "Emulsion" ):
        delEvent += True,

    # Corresponding Lepton should be exist
    if Lepton == {}:
        delEvent += True,

    # Number of Prong should be valid
    NProng = len(tuple( particle for particle in CharmDaughter['PDG'] if particle not in Chargeless ))
    if Charm['PDG'] in { -421, 421 } and NProng not in { 0, 2, 4, 6 }:
        delEvent += True,
    elif Charm['PDG'] in { -431, -411, 411, 431, 4122 } and NProng not in { 1, 3, 5 }:
        delEvent += True,

    if True not in delEvent:

      """ Some physics calculation. """
      # They are needed for s-quark content search
      BjorX = Bjorken( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                       r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                       r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2) )
      InelY = Inelasticity( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                       r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                       r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2) )

      # Slope and angle calculations
      CSX = Slope(Charm['Px'], Charm['Pz'])           #Charm Slope in X-axis
      CSY = Slope(Charm['Py'], Charm['Pz'])           #Charm Slope in X-axis
      angNuX = Slope(Neutrino['Px'], Neutrino['Pz'])*1000     #in mrad
      angNuY = Slope(Neutrino['Py'], Neutrino['Pz'])*1000     #in mrad
      angSpc = (angNuX**2 + angNuY**2)**0.5       #Space Angle of Neutrino

      # Flight length and impact parameter calculations
      fL = FlightLength(Charm['Pos'], Neutrino['Pos'])*10.0    #in mm
      iP = ImpactParameterV2(Neutrino['Pos'], Charm['Pos'], CSX, CSY)*1e4     #in micro-m

      # Multiplicity calculations
      MultPri = Multiplicity(NeutrinoDaughter['PDG'], Chargeless)       #Multiplicity at Neutrino Vertex
      MultSec = Multiplicity(CharmDaughter['PDG'], Chargeless)         #Multiplicity at Charm Vertex

      """ At this point, selection rules are started to be applied! """
      #Geometry Selection Check // Checked at Each Vertex
      if GeometrySelection(Neutrino['Pos']):
        GS.append(True)
      else: GS.append(False)
      if GeometrySelection(Charm['Pos']):
        GS.append(True)
      else: GS.append(False)

      #Location Selection Check // Checked at Neutrino Vertex
      for b in xrange(len(NeutrinoDaughter['P'])):
        #Mom = ( NeutrinoDaughter['Px'][b],NeutrinoDaughter['Py'][b],NeutrinoDaughter['Pz'][b],NeutrinoDaughter['P'][b] )
        #if LocationSelection(Mom,NeutrinoDaughter['PDG'][b]):
        if LocationSelection( (NeutrinoDaughter['Px'][b],NeutrinoDaughter['Py'][b],NeutrinoDaughter['Pz'][b],NeutrinoDaughter['P'][b]),
                              NeutrinoDaughter['PDG'][b] ):
          LS.append(True)
        else: LS.append(False)

      #Decay Search Selection Check // Checked at Charm Vertex
      if NProng == 1:
        for c in xrange(len(CharmDaughter['P'])):
          CDSX = Slope( CharmDaughter['Px'][c], CharmDaughter['Pz'][c] )
          CDSY = Slope( CharmDaughter['Py'][c], CharmDaughter['Pz'][c] )
          kA = KinkAngle(CSX, CSY, CDSX, CDSY)   #in rad
          oA = 2100
          if DecaySearchSelection(fL, kA*1e3, iP, oA):
            DSS.append(True)
          else: DSS.append(False)
      elif NProng == 2:
        CDSX, CDSY = (), ()
        for d in xrange(len(CharmDaughter['PDG'])):
          if CharmDaughter['PDG'][d] not in Chargeless:
            CDSX += Slope(CharmDaughter['Px'][d],CharmDaughter['Pz'][d]),
            CDSY += Slope(CharmDaughter['Py'][d],CharmDaughter['Pz'][d]),
        oA = OpeningAngle(CDSX[0], CDSY[0], CDSX[1], CDSY[1])   #in rad
        kA = 2100
        if DecaySearchSelection(fL, kA, iP, oA*1e3):
          DSS.append(True)
        else: DSS.append(False)
      else:
        kA = 2100
        oA = 2100
        if DecaySearchSelection(fL, kA, iP, oA):
          DSS.append(True)
        else: DSS.append(False)

      """ Fill unselected histograms here. """
      h['nuE'].Fill(Neutrino['E'])
      h['nuAngDistXF'].Fill(angNuX)
      h['nuAngDistYF'].Fill(angNuY)
      h['nuAng2DF'].Fill(angNuX,angNuY)
      h['tp'].Fill(Neutrino['Pos'][0], Neutrino['Pos'][1])
      h['za'].Fill(Neutrino['Pos'][2])
      h['BjorX'].Fill(BjorX)
      h['InelY'].Fill(InelY)

      """ Decide the channel here and fill Charm Flavor related Histograms. """
      if Charm['PDG'] in { -411, 411 }:
          ch = "d"+str(NProng)
          h['nuE1'].Fill(Neutrino['E'])
          h['dC1E'].Fill(Charm['E'])
          h['dC1FL'].Fill(fL)
          h['dC1IP'].Fill(iP)
          h['dC1KA'].Fill(kA)
          h['dC1M'].Fill(MultPri)
          h['dC1M2'].Fill(MultSec)
      elif Charm['PDG'] in { -421, 421 }:
          ch = "d0"+str(NProng)
          h['nuE2'].Fill(Neutrino['E'])
          h['dC2E'].Fill(Charm['E'])
          h['dC2FL'].Fill(fL)
          h['dC2IP'].Fill(iP)
          h['dC2OA'].Fill(oA)
          h['dC2M'].Fill(MultPri)
          h['dC2M2'].Fill(MultSec)
      elif Charm['PDG'] in { -431, 431 }:
          ch = "dS"+str(NProng)
          h['nuE3'].Fill(Neutrino['E'])
          h['dC3E'].Fill(Charm['E'])
          h['dC3FL'].Fill(fL)
          h['dC3IP'].Fill(iP)
          h['dC3KA'].Fill(kA)
          h['dC3M'].Fill(MultPri)
          h['dC3M2'].Fill(MultSec)
      elif Charm['PDG'] in { 4122 }:
          ch = "lambdaC"+str(NProng)
          h['nuE4'].Fill(Neutrino['E'])
          h['dC4E'].Fill(Charm['E'])
          h['dC4FL'].Fill(fL)
          h['dC4IP'].Fill(iP)
          h['dC4KA'].Fill(kA)
          h['dC4M'].Fill(MultPri)
          h['dC4M2'].Fill(MultSec)

      """ Counter in progress. """
      CounterDict[ch][0] += 1
      if ch != 'd00':       # 0 Prong channel of D0 must be eliminated
          if False not in GS:
              h['g-nuEs'].Fill(Neutrino['E'])
              CounterDict[ch][1] += 1
              if True in LS:
                  h['l-nuEs'].Fill(Neutrino['E'])
                  CounterDict[ch][2] += 1
                  if True in DSS:
                      h['d-nuEs'].Fill(Neutrino['E'])
                      CounterDict[ch][3] += 1
                      if Charm['PDG'] in { -411, 411 }:
                          h['d-nuEs1'].Fill(Neutrino['E'])
                          h['dC1ES'].Fill(Charm['E'])
                          h['dC1FLS'].Fill(fL)
                          h['dC1IPS'].Fill(iP)
                          h['dC1KAS'].Fill(kA)
                          h['dC1MS'].Fill(MultPri)
                          h['dC1M2S'].Fill(MultSec)
                      elif Charm['PDG'] in { -421, 421 }:
                          h['d-nuEs2'].Fill(Neutrino['E'])
                          h['dC2ES'].Fill(Charm['E'])
                          h['dC2FLS'].Fill(fL)
                          h['dC2IPS'].Fill(iP)
                          h['dC2OAS'].Fill(oA)
                          h['dC2MS'].Fill(MultPri)
                          h['dC2M2S'].Fill(MultSec)
                      elif Charm['PDG'] in { -431, 431 }:
                          h['d-nuEs3'].Fill(Neutrino['E'])
                          h['dC3ES'].Fill(Charm['E'])
                          h['dC3FLS'].Fill(fL)
                          h['dC3IPS'].Fill(iP)
                          h['dC3KAS'].Fill(kA)
                          h['dC3MS'].Fill(MultPri)
                          h['dC3M2S'].Fill(MultSec)
                      elif Charm['PDG'] in { 4122 }:
                          h['d-nuEs4'].Fill(Neutrino['E'])
                          h['dC4ES'].Fill(Charm['E'])
                          h['dC4FLS'].Fill(fL)
                          h['dC4IPS'].Fill(iP)
                          h['dC4KAS'].Fill(kA)
                          h['dC4MS'].Fill(MultPri)
                          h['dC4M2S'].Fill(MultSec)

    bar.next()

bar.finish()

makePlots()

print "\nNumber of Monte Carlo Events ****************"

tableSelection = [ [nEnt, "Before Any Cut or Selection."],
                   [sum([ CounterDict[x][0] for x in CounterDict.keys() ]), "After Selecting Nu Tau Target."],
                   [sum([ CounterDict[x][2] for x in CounterDict.keys() ]), "After Geometry Selection."],
                   [sum([ CounterDict[x][2] for x in CounterDict.keys() ]), "After Location Selection."],
                   [sum([ CounterDict[x][3] for x in CounterDict.keys() ]), "After Decay Search Selection."] ]
print(tabulate(tableSelection, headers=["# of Events", "Remaining"], tablefmt="simple" ))

print "\nEfficiency Stats Respect to Number of Prong ****************"

tableProng = [ ['D+', '--N/A--', CalculateEff(CounterDict['d1'][3], CounterDict['d1'][0]), '--N/A--', CalculateEff(CounterDict['d3'][3], CounterDict['d3'][0]), '--N/A--', CalculateEff(CounterDict['d5'][3], CounterDict['d5'][0]), '--N/A--'],
          ['D0', CalculateEff(CounterDict['d00'][3], CounterDict['d00'][0]), '--N/A--', CalculateEff(CounterDict['d02'][3], CounterDict['d02'][0]), '--N/A--', CalculateEff(CounterDict['d04'][3], CounterDict['d04'][0]), '--N/A--', CalculateEff(CounterDict['d06'][3], CounterDict['d06'][0])],
          ['Ds+', '--N/A--', CalculateEff(CounterDict['dS1'][3], CounterDict['dS1'][0]), '--N/A--', CalculateEff(CounterDict['dS3'][3], CounterDict['dS3'][0]), '--N/A--', CalculateEff(CounterDict['dS5'][3], CounterDict['dS5'][0]), '--N/A--'],
          ['LambdaC+', '--N/A--', CalculateEff(CounterDict['lambdaC1'][3], CounterDict['lambdaC1'][0]), '--N/A--', CalculateEff(CounterDict['lambdaC3'][3], CounterDict['lambdaC3'][0]), '--N/A--', CalculateEff(CounterDict['lambdaC5'][3], CounterDict['lambdaC5'][0]), '--N/A--'] ]
print(tabulate(tableProng, headers=['0 Prong', '1 Prong', '2 Prong', '3 Prong', '4 Prong', '5 Prong', '6 Prong'], tablefmt="grid" ))

#print("--- %s seconds ---" % (time.time() - start_time))
