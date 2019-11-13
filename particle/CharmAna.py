import ROOT as r
import rootUtils as ut
import elikkayalib, argparse

from physlib import *

def init():
  ap = argparse.ArgumentParser(
      description='Run the dummy builder')
  ap.add_argument('--work_dir', type=str, help="work space path", dest='work_dir', default=None)
  ap.add_argument('--geo_file', type=str, help="geometry file", dest='geo_file', default=None)
  ap.add_argument('--input_file', type=str, help="input file", dest='input_file', default=None)
  args = ap.parse_args()
  return args

args = init() #to get the options

work_dir = args.work_dir
geo_file = args.geo_file
input_file = args.input_file

t = elikkayalib.configure(input_file)

g = r.TFile(geo_file)
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

#nEnt = t.fChain.GetEntries()
nEnt = 10000

inGeo, tGS, tLS, tDSS = 0., 0., 0., 0.
d_plus, d_zero, ds_plus, lambda_c = 0., 0., 0., 0.
CCounter = [d_plus, d_zero, ds_plus, lambda_c]
d_plusS, d_zeroS, ds_plusS, lambda_cS = 0., 0., 0., 0.
CCounterS = [d_plusS, d_zeroS, ds_plusS, lambda_cS]

Hadron = [-130, -211, -321, -2212, 130, 211, 321, 2212]
Lepton = [-11, -13, -15, 11, 13, 15]

CharmedHadron = [411, 421, 431, 4122]
Chargeless = [-14, 22, 111, 130, 421, 2112]

h = {}
ut.bookHist(h, 'effPlot', 'Efficiency Plot', 60, 0, 300)
ut.bookHist(h, 'charm_fraction', 'Charm Fractions', 4, 0, 4)
ut.bookHist(h, 'charm_fractionS', 'Charm Fractions (Selected)', 4, 0, 4)
ut.bookHist(h, 'nuE', 'Incoming Neutrino Energy Spectrum ;nu_{mu};', 60, 0, 300)
ut.bookHist(h, 'nuES', 'Incoming Neutrino Energy Spectrum ;nu_{mu}; (Selected)', 60, 0, 300)
ut.bookHist(h, 'tplane', 'Neutrino Interactions at Transverse Plane', 100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'tplaneS', 'Neutrino Interactions at Transverse Plane (Selected)', 100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'dC1E', 'Charmed Hadron Energy Spectrum D+', 40, 0, 100)
ut.bookHist(h, 'dC1ES', 'Charmed Hadron Energy Spectrum D+ (Selected)', 40, 0, 100)
ut.bookHist(h, 'dC2E', 'Charmed Hadron Energy Spectrum D0', 40, 0, 100)
ut.bookHist(h, 'dC2ES', 'Charmed Hadron Energy Spectrum D0 (Selected)', 40, 0, 100)
ut.bookHist(h, 'dC3E', 'Charmed Hadron Energy Spectrum Ds+', 40, 0, 100)
ut.bookHist(h, 'dC3ES', 'Charmed Hadron Energy Spectrum Ds+ (Selected)', 40, 0, 100)
ut.bookHist(h, 'dC4E', 'Charmed Hadron Energy Spectrum Lc+', 40, 0, 100)
ut.bookHist(h, 'dC4ES', 'Charmed Hadron Energy Spectrum Lc+ (Selected)', 40, 0, 100)
ut.bookHist(h, 'dC1FL', 'Charmed Hadron Flight Length D+', 50, 0, 10)
ut.bookHist(h, 'dC1FLS', 'Charmed Hadron Flight Length D+ (Selected)', 50, 0, 10)
ut.bookHist(h, 'dC2FL', 'Charmed Hadron Flight Length D0', 50, 0, 10)
ut.bookHist(h, 'dC2FLS', 'Charmed Hadron Flight Length D0 (Selected)', 50, 0, 10)
ut.bookHist(h, 'dC3FL', 'Charmed Hadron Flight Length Ds+', 50, 0, 10)
ut.bookHist(h, 'dC3FLS', 'Charmed Hadron Flight Length Ds+ (Selected)', 50, 0, 10)
ut.bookHist(h, 'dC4FL', 'Charmed Hadron Flight Length Lc+', 50, 0, 10)
ut.bookHist(h, 'dC4FLS', 'Charmed Hadron Flight Length Lc+ (Selected)', 50, 0, 10)
ut.bookHist(h, 'dC1KA',  'Kink Angle at Charm Vertex D+',             50, 0, 1)
ut.bookHist(h, 'dC1KAS', 'Kink Angle at Charm Vertex D+ (Selected)',  50, 0, 1)
ut.bookHist(h, 'dC2OA',  'Opening Angle at Charm Vertex D0',             50, 0, 1)
ut.bookHist(h, 'dC2OAS', 'Opening Angle at Charm Vertex D0 (Selected)',  50, 0, 1)
ut.bookHist(h, 'dC3KA',  'Kink Angle at Charm Vertex Ds+',            50, 0, 1)
ut.bookHist(h, 'dC3KAS', 'Kink Angle at Charm Vertex Ds+ (Selected)', 50, 0, 1)
ut.bookHist(h, 'dC4KA',  'Kink Angle at Charm Vertex Lc+',            50, 0, 1)
ut.bookHist(h, 'dC4KAS', 'Kink Angle at Charm Vertex Lc+ (Selected)', 50, 0, 1)
ut.bookHist(h, 'dC1M', 'Charmed Hadron Multiplicity at Primary Vertex D+', 15, 0, 15)
ut.bookHist(h, 'dC1MS', 'Charmed Hadron Multiplicity at Primary Vertex D+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'dC2M', 'Charmed Hadron Multiplicity at Primary Vertex D0', 15, 0, 15)
ut.bookHist(h, 'dC2MS', 'Charmed Hadron Multiplicity at Primary Vertex D0 (Selected)', 15, 0, 15)
ut.bookHist(h, 'dC3M', 'Charmed Hadron Multiplicity at Primary Vertex Ds+', 15, 0, 15)
ut.bookHist(h, 'dC3MS', 'Charmed Hadron Multiplicity at Primary Vertex Ds+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'dC4M', 'Charmed Hadron Multiplicity at Primary Vertex Lc+', 15, 0, 15)
ut.bookHist(h, 'dC4MS', 'Charmed Hadron Multiplicity at Primary Vertex Lc+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'dC1M2', 'Charmed Hadron Multiplicity at Secondary Vertex D+', 8, 0, 8)
ut.bookHist(h, 'dC1M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'dC2M2', 'Charmed Hadron Multiplicity at Secondary Vertex D0', 8, 0, 8)
ut.bookHist(h, 'dC2M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D0 (Selected)', 8, 0, 8)
ut.bookHist(h, 'dC3M2', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+', 8, 0, 8)
ut.bookHist(h, 'dC3M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'dC4M2', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+', 8, 0, 8)
ut.bookHist(h, 'dC4M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'za', 'Interactions at z-axis', 200, -3300, -2900)
ut.bookHist(h, 'zaS', 'Interactions at z-axis', 200, -3300, -2900)

C1P0g, C1P1g, C1P2g, C1P3g, C1P4g, C1P5g, C1P6g, C1P7g, C1P8g, C1P9g = [], [], [], [], [], [], [], [], [], []
C2P0g, C2P1g, C2P2g, C2P3g, C2P4g, C2P5g, C2P6g, C2P7g, C2P8g, C2P9g = [], [], [], [], [], [], [], [], [], []
C3P0g, C3P1g, C3P2g, C3P3g, C3P4g, C3P5g, C3P6g, C3P7g, C3P8g, C3P9g = [], [], [], [], [], [], [], [], [], []
C4P0g, C4P1g, C4P2g, C4P3g, C4P4g, C4P5g, C4P6g, C4P7g, C4P8g, C4P9g = [], [], [], [], [], [], [], [], [], []

C1P0l, C1P1l, C1P2l, C1P3l, C1P4l, C1P5l, C1P6l, C1P7l, C1P8l, C1P9l = [], [], [], [], [], [], [], [], [], []
C2P0l, C2P1l, C2P2l, C2P3l, C2P4l, C2P5l, C2P6l, C2P7l, C2P8l, C2P9l = [], [], [], [], [], [], [], [], [], []
C3P0l, C3P1l, C3P2l, C3P3l, C3P4l, C3P5l, C3P6l, C3P7l, C3P8l, C3P9l = [], [], [], [], [], [], [], [], [], []
C4P0l, C4P1l, C4P2l, C4P3l, C4P4l, C4P5l, C4P6l, C4P7l, C4P8l, C4P9l = [], [], [], [], [], [], [], [], [], []

C1P0d, C1P1d, C1P2d, C1P3d, C1P4d, C1P5d, C1P6d, C1P7d, C1P8d, C1P9d = [], [], [], [], [], [], [], [], [], []
C2P0d, C2P1d, C2P2d, C2P3d, C2P4d, C2P5d, C2P6d, C2P7d, C2P8d, C2P9d = [], [], [], [], [], [], [], [], [], []
C3P0d, C3P1d, C3P2d, C3P3d, C3P4d, C3P5d, C3P6d, C3P7d, C3P8d, C3P9d = [], [], [], [], [], [], [], [], [], []
C4P0d, C4P1d, C4P2d, C4P3d, C4P4d, C4P5d, C4P6d, C4P7d, C4P8d, C4P9d = [], [], [], [], [], [], [], [], [], []

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

def CharmFraction(CharmPDG, h, CCounter):
  if CharmPDG == 411:
    h.Fill(0,1)
    CCounter[0] += 1.
  if CharmPDG == 421:
    h.Fill(1,1)
    CCounter[1] += 1.
  if CharmPDG == 431:
    h.Fill(2,1)
    CCounter[2] += 1.
  if CharmPDG == 4122:
    h.Fill(3,1)
    CCounter[3] += 1.

def makePlots():
  #Charmed Hadron Fraction Histogram
  ut.bookCanvas(h,key='FractionAnalysis',title='Produced Charmed Hadron Fractions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['FractionAnalysis'].cd(1)
  r.gStyle.SetOptStat(0)
  h['charm_fraction'].Draw()
  h['charm_fractionS'].SetFillStyle(3335)
  h['charm_fractionS'].SetFillColor(2)
  h['charm_fractionS'].Draw('same')
  h['FractionAnalysis'].Print(work_dir+'/histo/cfraction.png')
  #Charmed Hadron Energy Histograms
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
  h['dEnergyAnalysis'].Print(work_dir+'/histo/dcenergy.png')
  #Flight Length Histograms
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
  h['dFLAnalysis'].Print(work_dir+'/histo/dcfl.png')
  #Multiplicity at Neutrino Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis',title='Multiplicity at Primary Vertex',nx=1920,ny=1080,cx=2,cy=2)
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
  h['dMultAnalysis'].Print(work_dir+'/histo/dcmult.png')
  #Multiplicity at Charm Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis2',title='Multiplicity at Secondary Vertex',nx=1920,ny=1080,cx=2,cy=2)
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
  h['dMultAnalysis2'].Print(work_dir+'/histo/dcmult2.png')
  #Kink Angle Histograms
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
  h['kAngle'].Print(work_dir+'/histo/kAngle.png')
  #Opening Angle Histograms
  ut.bookCanvas(h,key='oAngle',title='Opening Angle',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['oAngle'].cd(1)
  h['dC2OA'].Draw()
  h['dC2OA'].SetXTitle('Opening Angle (rad)')
  h['dC2OAS'].SetFillStyle(3335)
  h['dC2OAS'].SetFillColor(2)
  h['dC2OAS'].Draw('same')
  h['oAngle'].Print(work_dir+'/histo/oAngle.png')
  #Neutrino Beam Energy Histogram
  ut.bookCanvas(h,key='nuEnergy',title='Incoming Neutrino Beam Energy',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['nuEnergy'].cd(1)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  h['nuES'].SetFillStyle(3335)
  h['nuES'].SetFillColor(2)
  h['nuES'].Draw('same')
  h['nuEnergy'].Print(work_dir+'/histo/nuenergy.png')
  #Neutrino Interactions at Transverse Plane Histogram
  ut.bookCanvas(h,key='nutp',title='Transverse Plane Interactions',nx=1920,ny=720,cx=2,cy=1)
  cv = h['nutp'].cd(1)
  h['tplane'].Draw('COLZ')
  cv = h['nutp'].cd(2)
  h['tplaneS'].Draw('COLZ')
  h['nutp'].Print(work_dir+'/histo/nutplane.png')
  #Efficiency plot with nu energy
  ut.bookCanvas(h,key='nuEff',title='Efficiency Plot',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['nuEff'].cd(1)
  r.gStyle.SetOptStat(0)
  h['nuE'].Draw()
  h['nuES'].Draw()
  h['nuES'].Sumw2()
  h['effPlot'].Divide(h['nuES'],h['nuE'],1.,1.,'B')
  h['effPlot'].Draw('E0')
  h['nuEff'].Print(work_dir+'/histo/nuEff.png')
  #Z-axis interactions
  ut.bookCanvas(h,key='zaxis',title='Z Axis Interactions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['zaxis'].cd(1)
  h['za'].Draw()
  h['zaS'].SetFillStyle(3335)
  h['zaS'].SetFillColor(2)
  h['zaS'].Draw('same')
  h['zaxis'].Print(work_dir+'/histo/nuZ.png')

def Eff(Arr):
  try:
    res = float(Arr.count(True))/float(len(Arr))
    res = '%.5f' %res
    return res
  except ZeroDivisionError:
    res = str('---x---')
    return res

def ProngCount(CDauPdg):
  NProng = 0
  for i in range(len(CDauPdg)):
    if CDauPdg[i] not in Chargeless:
      NProng += 1
  if NProng == 0: NOP = 0
  if NProng == 1: NOP = 1
  if NProng == 2: NOP = 2
  if NProng == 3: NOP = 3
  if NProng == 4: NOP = 4
  if NProng == 5: NOP = 5
  if NProng == 6: NOP = 6
  if NProng == 7: NOP = 7
  if NProng == 8: NOP = 8
  if NProng == 9: NOP = 9
  return NOP

def ChannelDecision(CPdg, NOP):
  if CPdg == 411  and NOP == 0: ch = 10
  if CPdg == 421  and NOP == 0: ch = 20
  if CPdg == 431  and NOP == 0: ch = 30
  if CPdg == 4122 and NOP == 0: ch = 40
  if CPdg == 411  and NOP == 1: ch = 11
  if CPdg == 421  and NOP == 1: ch = 21
  if CPdg == 431  and NOP == 1: ch = 31
  if CPdg == 4122 and NOP == 1: ch = 41
  if CPdg == 411  and NOP == 2: ch = 12
  if CPdg == 421  and NOP == 2: ch = 22
  if CPdg == 431  and NOP == 2: ch = 32
  if CPdg == 4122 and NOP == 2: ch = 42
  if CPdg == 411  and NOP == 3: ch = 13
  if CPdg == 421  and NOP == 3: ch = 23
  if CPdg == 431  and NOP == 3: ch = 33
  if CPdg == 4122 and NOP == 3: ch = 43
  if CPdg == 411  and NOP == 4: ch = 14
  if CPdg == 421  and NOP == 4: ch = 24
  if CPdg == 431  and NOP == 4: ch = 34
  if CPdg == 4122 and NOP == 4: ch = 44
  if CPdg == 411  and NOP == 5: ch = 15
  if CPdg == 421  and NOP == 5: ch = 25
  if CPdg == 431  and NOP == 5: ch = 35
  if CPdg == 4122 and NOP == 5: ch = 45
  if CPdg == 411  and NOP == 6: ch = 16
  if CPdg == 421  and NOP == 6: ch = 26
  if CPdg == 431  and NOP == 6: ch = 36
  if CPdg == 4122 and NOP == 6: ch = 46
  if CPdg == 411  and NOP == 7: ch = 17
  if CPdg == 421  and NOP == 7: ch = 27
  if CPdg == 431  and NOP == 7: ch = 37
  if CPdg == 4122 and NOP == 7: ch = 47
  if CPdg == 411  and NOP == 8: ch = 18
  if CPdg == 421  and NOP == 8: ch = 28
  if CPdg == 431  and NOP == 8: ch = 38
  if CPdg == 4122 and NOP == 8: ch = 48
  if CPdg == 411  and NOP == 9: ch = 19
  if CPdg == 421  and NOP == 9: ch = 29
  if CPdg == 431  and NOP == 9: ch = 39
  if CPdg == 4122 and NOP == 9: ch = 49
  return ch

for event in xrange(nEnt):

  t.GetEntry(event)

  if (t.IntInGeo.at(0)):

    CDauPdg = []
    CDauPos_i, CDauPos_j, CDauPos_k = [], [], []
    CDauMom_i, CDauMom_j, CDauMom_k, CDauMom_l = [], [], [], []
    Mom_i, Mom_j, Mom_k, Mom_l = [], [], [], []
    PVPdg = []  #PrimaryVertexPdg
    GS, LS, DSS = [], [], []
    nuEnergy = 0.
    delProng = False

    for vtx in xrange(t.VertexInfo.size()):

      if t.VertexInfo.at(vtx) == 0:
        nuEnergy = t.Energy.at(vtx)

      if t.VertexInfo.at(vtx) == 1:
        Pos = []
        Pos.append(t.StartX.at(vtx))
        Pos.append(t.StartY.at(vtx))
        Pos.append(t.StartZ.at(vtx))
        Mom_i.append(t.Px.at(vtx))
        Mom_j.append(t.Py.at(vtx))
        Mom_k.append(t.Pz.at(vtx))
        Mom_l.append(t.P.at(vtx))
        PVPdg.append(t.PdgCode.at(vtx))
        if PVPdg[-1] in CharmedHadron:
          CPos = Pos
          CMom = []
          CMom.append(t.Px.at(vtx))
          CMom.append(t.Py.at(vtx))
          CMom.append(t.Pz.at(vtx))
          CMom.append(t.P.at(vtx))
          CPdg = PVPdg[-1]
          CEnergy = t.Energy.at(vtx)

      if t.VertexInfo.at(vtx) == 22:
        CDauPos_i.append(t.StartX.at(vtx))
        CDauPos_j.append(t.StartY.at(vtx))
        CDauPos_k.append(t.StartZ.at(vtx))
        CDauMom_i.append(t.Px.at(vtx))
        CDauMom_j.append(t.Py.at(vtx))
        CDauMom_k.append(t.Pz.at(vtx))
        CDauMom_l.append(t.P.at(vtx))
        CDauPdg.append(t.PdgCode.at(vtx))

    CDauPos = [CDauPos_i[0],CDauPos_j[0],CDauPos_k[0]]
    NOP = ProngCount(CDauPdg)
    ch = ChannelDecision(CPdg, NOP)
    MultPri = Multiplicity(PVPdg, Chargeless)
    MultSec = Multiplicity(CDauPdg, Chargeless)
    CSX = Slope(CMom[0], CMom[2])
    CSY = Slope(CMom[1], CMom[2])
    fL = FlightLength(CDauPos, CPos)*10.0    #in mm
    iP = ImpactParameterV2(CPos, CDauPos, CSX, CSY)*1e4     #in micro-m

    #Geometry Selection Check // Checked at Each Vertex
    if GeometrySelection(Pos):
      GS.append(True)
    else: GS.append(False)
    if GeometrySelection(CDauPos):
      GS.append(True)
    else: GS.append(False)

    #Location Selection Check // Checked at Neutrino Vertex
    for b in xrange(len(Mom_i)):
      Mom = [Mom_i[b],Mom_j[b],Mom_k[b],Mom_l[b]]
      if LocationSelection(Mom,PVPdg[b]):
        LS.append(True)
      else: LS.append(False)

    #Decay Search Selection Check // Checked at Charm Vertex
    if NOP==1:
      for c in xrange(len(CDauMom_i)):
        CDauMom = [CDauMom_i[c],CDauMom_j[c],CDauMom_k[c],CDauMom_l[c]]
        CDSX = Slope(CDauMom[0], CDauMom[2])
        CDSY = Slope(CDauMom[1], CDauMom[2])
        kA = KinkAngle(CSX, CSY, CDSX, CDSY)   #in rad
        oA = 2100
        if DecaySearchSelection(fL, kA*1e3, iP, oA):
          DSS.append(True)
        else: DSS.append(False)
    elif NOP==2:
      CDSX, CDSY = [], []
      for d in xrange(len(CDauPdg)):
        if CDauPdg[d] not in Chargeless:
          CDSX.append(Slope(CDauMom_i[d],CDauMom_k[d]))
          CDSY.append(Slope(CDauMom_j[d],CDauMom_k[d]))
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

    if CPdg in [411, 431, 4122] and NOP not in [1, 3, 5, 7]:
      delProng = True
    if (CPdg == 421) and NOP not in [0, 2, 4, 6]:
      delProng = True

    if not delProng:

      CharmFraction(CPdg, h['charm_fraction'], CCounter)
      h['tplane'].Fill(Pos[0], Pos[1])
      h['nuE'].Fill(nuEnergy)
      h['za'].Fill(Pos[2])
      inGeo += 1.

      if CPdg == 411:
        h['dC1E'].Fill(CEnergy)
        h['dC1FL'].Fill(fL)
        h['dC1KA'].Fill(kA)
        h['dC1M'].Fill(MultPri)
        h['dC1M2'].Fill(MultSec)
      elif CPdg== 421:
        h['dC2E'].Fill(CEnergy)
        h['dC2FL'].Fill(fL)
        h['dC2OA'].Fill(oA)
        h['dC2M'].Fill(MultPri)
        h['dC2M2'].Fill(MultSec)
      elif CPdg == 431:
        h['dC3E'].Fill(CEnergy)
        h['dC3FL'].Fill(fL)
        h['dC3KA'].Fill(kA)
        h['dC3M'].Fill(MultPri)
        h['dC3M2'].Fill(MultSec)
      elif CPdg == 4122:
        h['dC4E'].Fill(CEnergy)
        h['dC4FL'].Fill(fL)
        h['dC4KA'].Fill(kA)
        h['dC4M'].Fill(MultPri)
        h['dC4M2'].Fill(MultSec)

      if False not in GS:
        if True in LS:
          if True in DSS:
            if CPdg == 411:
              h['dC1ES'].Fill(CEnergy)
              h['dC1FLS'].Fill(fL)
              h['dC1KAS'].Fill(kA)
              h['dC1MS'].Fill(MultPri)
              h['dC1M2S'].Fill(MultSec)
            elif CPdg==421 and ch!=20:
              h['dC2ES'].Fill(CEnergy)
              h['dC2FLS'].Fill(fL)
              h['dC2OAS'].Fill(oA)
              h['dC2MS'].Fill(MultPri)
              h['dC2M2S'].Fill(MultSec)
            elif CPdg == 431:
              h['dC3ES'].Fill(CEnergy)
              h['dC3FLS'].Fill(fL)
              h['dC3KAS'].Fill(kA)
              h['dC3MS'].Fill(MultPri)
              h['dC3M2S'].Fill(MultSec)
            elif CPdg == 4122:
              h['dC4ES'].Fill(CEnergy)
              h['dC4FLS'].Fill(fL)
              h['dC4KAS'].Fill(kA)
              h['dC4MS'].Fill(MultPri)
              h['dC4M2S'].Fill(MultSec)

            if ch!=20:
              CharmFraction(CPdg, h['charm_fractionS'], CCounterS)
              h['tplaneS'].Fill(Pos[0], Pos[1])
              h['nuES'].Fill(nuEnergy)
              h['zaS'].Fill(Pos[2])

      if ch == 10:
        if False not in GS:
          tGS += 1.
          C1P0g.append(True)
          if True in LS:
            tLS += 1.
            C1P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P0d.append(True)
            else: C1P0d.append(False)
          else: C1P0l.append(False), C1P0d.append(False)
        else: C1P0g.append(False), C1P0l.append(False), C1P0d.append(False)

      if ch == 20:
        if False not in GS:
          tGS += 0.
          C2P0g.append(False)
          if True in LS:
            tLS += 0.
            C2P0l.append(False)
            if True in DSS:
              tDSS += 0.
              C2P0d.append(False)
            else: C2P0d.append(False)
          else: C2P0l.append(False), C2P0d.append(False)
        else: C2P0g.append(False), C2P0l.append(False), C2P0d.append(False)

      if ch == 30:
        if False not in GS:
          tGS += 1.
          C3P0g.append(True)
          if True in LS:
            tLS += 1.
            C3P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P0d.append(True)
            else: C3P0d.append(False)
          else: C3P0l.append(False), C3P0d.append(False)
        else: C3P0g.append(False), C3P0l.append(False), C3P0d.append(False)

      if ch == 40:
        if False not in GS:
          tGS += 1.
          C4P0g.append(True)
          if True in LS:
            tLS += 1.
            C4P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P0d.append(True)
            else: C4P0d.append(False)
          else: C4P0l.append(False), C4P0d.append(False)
        else: C4P0g.append(False), C4P0l.append(False), C4P0d.append(False)

      if ch == 11:
        if False not in GS:
          tGS += 1.
          C1P1g.append(True)
          if True in LS:
            tLS += 1.
            C1P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P1d.append(True)
            else: C1P1d.append(False)
          else: C1P1l.append(False), C1P1d.append(False)
        else: C1P1g.append(False), C1P1l.append(False), C1P1d.append(False)

      if ch == 21:
        if False not in GS:
          tGS += 1.
          C2P1g.append(True)
          if True in LS:
            tLS += 1.
            C2P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P1d.append(True)
            else: C2P1d.append(False)
          else: C2P1l.append(False), C2P1d.append(False)
        else: C2P1g.append(False), C2P1l.append(False), C2P1d.append(False)

      if ch == 31:
        if False not in GS:
          tGS += 1.
          C3P1g.append(True)
          if True in LS:
            tLS += 1.
            C3P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P1d.append(True)
            else: C3P1d.append(False)
          else: C3P1l.append(False), C3P1d.append(False)
        else: C3P1g.append(False), C3P1l.append(False), C3P1d.append(False)

      if ch == 41:
        if False not in GS:
          tGS += 1.
          C4P1g.append(True)
          if True in LS:
            tLS += 1.
            C4P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P1d.append(True)
            else: C4P1d.append(False)
          else: C4P1l.append(False), C4P1d.append(False)
        else: C4P1g.append(False), C4P1l.append(False), C4P1d.append(False)

      if ch == 12:
        if False not in GS:
          tGS += 1.
          C1P2g.append(True)
          if True in LS:
            tLS += 1.
            C1P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P2d.append(True)
            else: C1P2d.append(False)
          else: C1P2l.append(False), C1P2d.append(False)
        else: C1P2g.append(False), C1P2l.append(False), C1P2d.append(False)

      if ch == 22:
        if False not in GS:
          tGS += 1.
          C2P2g.append(True)
          if True in LS:
            tLS += 1.
            C2P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P2d.append(True)
            else: C2P2d.append(False)
          else: C2P2l.append(False), C2P2d.append(False)
        else: C2P2g.append(False), C2P2l.append(False), C2P2d.append(False)

      if ch == 32:
        if False not in GS:
          tGS += 1.
          C3P2g.append(True)
          if True in LS:
            tLS += 1.
            C3P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P2d.append(True)
            else: C3P2d.append(False)
          else: C3P2l.append(False), C3P2d.append(False)
        else: C3P2g.append(False), C3P2l.append(False), C3P2d.append(False)

      if ch == 42:
        if False not in GS:
          tGS += 1.
          C4P2g.append(True)
          if True in LS:
            tLS += 1.
            C4P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P2d.append(True)
            else: C4P2d.append(False)
          else: C4P2l.append(False), C4P2d.append(False)
        else: C4P2g.append(False), C4P2l.append(False), C4P2d.append(False)

      if ch == 13:
        if False not in GS:
          tGS += 1.
          C1P3g.append(True)
          if True in LS:
            tLS += 1.
            C1P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P3d.append(True)
            else: C1P3d.append(False)
          else: C1P3l.append(False), C1P3d.append(False)
        else: C1P3g.append(False), C1P3l.append(False), C1P3d.append(False)

      if ch == 23:
        if False not in GS:
          tGS += 1.
          C2P3g.append(True)
          if True in LS:
            tLS += 1.
            C2P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P3d.append(True)
            else: C2P3d.append(False)
          else: C2P3l.append(False), C2P3d.append(False)
        else: C2P3g.append(False), C2P3l.append(False), C2P3d.append(False)

      if ch == 33:
        if False not in GS:
          tGS += 1.
          C3P3g.append(True)
          if True in LS:
            tLS += 1.
            C3P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P3d.append(True)
            else: C3P3d.append(False)
          else: C3P3l.append(False), C3P3d.append(False)
        else: C3P3g.append(False), C3P3l.append(False), C3P3d.append(False)

      if ch == 43:
        if False not in GS:
          tGS += 1.
          C4P3g.append(True)
          if True in LS:
            tLS += 1.
            C4P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P3d.append(True)
            else: C4P3d.append(False)
          else: C4P3l.append(False), C4P3d.append(False)
        else: C4P3g.append(False), C4P3l.append(False), C4P3d.append(False)

      if ch == 14:
        if False not in GS:
          tGS += 1.
          C1P4g.append(True)
          if True in LS:
            tLS += 1.
            C1P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P4d.append(True)
            else: C1P4d.append(False)
          else: C1P4l.append(False), C1P4d.append(False)
        else: C1P4g.append(False), C1P4l.append(False), C1P4d.append(False)

      if ch == 24:
        if False not in GS:
          tGS += 1.
          C2P4g.append(True)
          if True in LS:
            tLS += 1.
            C2P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P4d.append(True)
            else: C2P4d.append(False)
          else: C2P4l.append(False), C2P4d.append(False)
        else: C2P4g.append(False), C2P4l.append(False), C2P4d.append(False)

      if ch == 34:
        if False not in GS:
          tGS += 1.
          C3P4g.append(True)
          if True in LS:
            tLS += 1.
            C3P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P4d.append(True)
            else: C3P4d.append(False)
          else: C3P4l.append(False), C3P4d.append(False)
        else: C3P4g.append(False), C3P4l.append(False), C3P4d.append(False)

      if ch == 44:
        if False not in GS:
          tGS += 1.
          C4P4g.append(True)
          if True in LS:
            tLS += 1.
            C4P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P4d.append(True)
            else: C4P4d.append(False)
          else: C4P4l.append(False), C4P4d.append(False)
        else: C4P4g.append(False), C4P4l.append(False), C4P4d.append(False)

      if ch == 15:
        if False not in GS:
          tGS += 1.
          C1P5g.append(True)
          if True in LS:
            tLS += 1.
            C1P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P5d.append(True)
            else: C1P5d.append(False)
          else: C1P5l.append(False), C1P5d.append(False)
        else: C1P5g.append(False), C1P5l.append(False), C1P5d.append(False)

      if ch == 25:
        if False not in GS:
          tGS += 1.
          C2P5g.append(True)
          if True in LS:
            tLS += 1.
            C2P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P5d.append(True)
            else: C2P5d.append(False)
          else: C2P5l.append(False), C2P5d.append(False)
        else: C2P5g.append(False), C2P5l.append(False), C2P5d.append(False)

      if ch == 35:
        if False not in GS:
          tGS += 1.
          C3P5g.append(True)
          if True in LS:
            tLS += 1.
            C3P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P5d.append(True)
            else: C3P5d.append(False)
          else: C3P5l.append(False), C3P5d.append(False)
        else: C3P5g.append(False), C3P5l.append(False), C3P5d.append(False)

      if ch == 45:
        if False not in GS:
          tGS += 1.
          C4P5g.append(True)
          if True in LS:
            tLS += 1.
            C4P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P5d.append(True)
            else: C4P5d.append(False)
          else: C4P5l.append(False), C4P5d.append(False)
        else: C4P5g.append(False), C4P5l.append(False), C4P5d.append(False)

      if ch == 16:
        if False not in GS:
          tGS += 1.
          C1P6g.append(True)
          if True in LS:
            tLS += 1.
            C1P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P6d.append(True)
            else: C1P6d.append(False)
          else: C1P6d.append(False), C1P6d.append(False)
        else: C1P6d.append(False), C1P6d.append(False), C1P6d.append(False)

      if ch == 26:
        if False not in GS:
          tGS += 1.
          C2P6g.append(True)
          if True in LS:
            tLS += 1.
            C2P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P6d.append(True)
            else: C2P6d.append(False)
          else: C2P6d.append(False), C2P6d.append(False)
        else: C2P6d.append(False), C2P6d.append(False), C2P6d.append(False)

      if ch == 36:
        if False not in GS:
          tGS += 1.
          C3P6g.append(True)
          if True in LS:
            tLS += 1.
            C3P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P6d.append(True)
            else: C3P6d.append(False)
          else: C3P6d.append(False), C3P6d.append(False)
        else: C3P6d.append(False), C3P6d.append(False), C3P6d.append(False)

      if ch == 46:
        if False not in GS:
          tGS += 1.
          C4P6g.append(True)
          if True in LS:
            tLS += 1.
            C4P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P6d.append(True)
            else: C4P6d.append(False)
          else: C4P6d.append(False), C4P6d.append(False)
        else: C4P6d.append(False), C4P6d.append(False), C4P6d.append(False)

      if ch == 17:
        if False not in GS:
          tGS += 1.
          C1P7g.append(True)
          if True in LS:
            tLS += 1.
            C1P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P7d.append(True)
            else: C1P7d.append(False)
          else: C1P7l.append(False), C1P7d.append(False)
        else: C1P7g.append(False), C1P7l.append(False), C1P7d.append(False)

      if ch == 27:
        if False not in GS:
          tGS += 1.
          C2P7g.append(True)
          if True in LS:
            tLS += 1.
            C2P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P7d.append(True)
            else: C2P7d.append(False)
          else: C2P7l.append(False), C2P7d.append(False)
        else: C2P7g.append(False), C2P7l.append(False), C2P7d.append(False)

      if ch == 37:
        if False not in GS:
          tGS += 1.
          C3P7g.append(True)
          if True in LS:
            tLS += 1.
            C3P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P7d.append(True)
            else: C3P7d.append(False)
          else: C3P7l.append(False), C3P7d.append(False)
        else: C3P7g.append(False), C3P7l.append(False), C3P7d.append(False)

      if ch == 47:
        if False not in GS:
          tGS += 1.
          C4P7g.append(True)
          if True in LS:
            tLS += 1.
            C4P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P7d.append(True)
            else: C4P7d.append(False)
          else: C4P7l.append(False), C4P7d.append(False)
        else: C4P7g.append(False), C4P7l.append(False), C4P7d.append(False)

      if ch == 18:
        if False not in GS:
          tGS += 1.
          C1P8g.append(True)
          if True in LS:
            tLS += 1.
            C1P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P8d.append(True)
            else: C1P8d.append(False)
          else: C1P8l.append(False), C1P8d.append(False)
        else: C1P8g.append(False), C1P8l.append(False), C1P8d.append(False)

      if ch == 28:
        if False not in GS:
          tGS += 1.
          C2P8g.append(True)
          if True in LS:
            tLS += 1.
            C2P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P8d.append(True)
            else: C2P8d.append(False)
          else: C2P8l.append(False), C2P8d.append(False)
        else: C2P8g.append(False), C2P8l.append(False), C2P8d.append(False)

      if ch == 38:
        if False not in GS:
          tGS += 1.
          C3P8g.append(True)
          if True in LS:
            tLS += 1.
            C3P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P8d.append(True)
            else: C3P8d.append(False)
          else: C3P8l.append(False), C3P8d.append(False)
        else: C3P8g.append(False), C3P8l.append(False), C3P8d.append(False)

      if ch == 48:
        if False not in GS:
          tGS += 1.
          C4P8g.append(True)
          if True in LS:
            tLS += 1.
            C4P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P8d.append(True)
            else: C4P8d.append(False)
          else: C4P8l.append(False), C4P8d.append(False)
        else: C4P8g.append(False), C4P8l.append(False), C4P8d.append(False)

      if ch == 19:
        if False not in GS:
          tGS += 1.
          C1P9g.append(True)
          if True in LS:
            tLS += 1.
            C1P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P9d.append(True)
            else: C1P9d.append(False)
          else: C1P9l.append(False), C1P9d.append(False)
        else: C1P9g.append(False), C1P9l.append(False), C1P9d.append(False)

      if ch == 29:
        if False not in GS:
          tGS += 1.
          C2P9g.append(True)
          if True in LS:
            tLS += 1.
            C2P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P9d.append(True)
            else: C2P9d.append(False)
          else: C2P9l.append(False), C2P9d.append(False)
        else: C2P9g.append(False), C2P9l.append(False), C2P9d.append(False)

      if ch == 39:
        if False not in GS:
          tGS += 1.
          C3P9g.append(True)
          if True in LS:
            tLS += 1.
            C3P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P9d.append(True)
            else: C3P9d.append(False)
          else: C3P9l.append(False), C3P9d.append(False)
        else: C3P9g.append(False), C3P9l.append(False), C3P9d.append(False)

      if ch == 49:
        if False not in GS:
          tGS += 1.
          C4P9g.append(True)
          if True in LS:
            tLS += 1.
            C4P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P79.append(True)
            else: C4P9d.append(False)
          else: C4P9l.append(False), C4P9d.append(False)
        else: C4P9g.append(False), C4P9l.append(False), C4P9d.append(False)

    else:
      continue

h['charm_fraction'].GetXaxis().SetBinLabel(1, "D^{+}")
h['charm_fraction'].GetXaxis().SetBinLabel(2, "D^{0}")
h['charm_fraction'].GetXaxis().SetBinLabel(3, "D_{s}^{+}")
h['charm_fraction'].GetXaxis().SetBinLabel(4, "#Lambda_{c}^{+}")

print '********************************************************************************************************'
print '*                                                                                                      *'
print '********************************************************************************************************'

print '       0 Prong   1 Prong   2 Prong   3 Prong   4 Prong   5 Prong   6 Prong   7 Prong   8 Prong   9 Prong'

print 'D+  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C1P0g), \
  Eff(C1P1g), \
  Eff(C1P2g), \
  Eff(C1P3g), \
  Eff(C1P4g), \
  Eff(C1P5g), \
  Eff(C1P6g), \
  Eff(C1P7g), \
  Eff(C1P8g), \
  Eff(C1P9g)
)

print 'D0  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C2P0g), \
  Eff(C2P1g), \
  Eff(C2P2g), \
  Eff(C2P3g), \
  Eff(C2P4g), \
  Eff(C2P5g), \
  Eff(C2P6g), \
  Eff(C2P7g), \
  Eff(C2P8g), \
  Eff(C2P9g)
)

print 'Ds+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C3P0g), \
  Eff(C3P1g), \
  Eff(C3P2g), \
  Eff(C3P3g), \
  Eff(C3P4g), \
  Eff(C3P5g), \
  Eff(C3P6g), \
  Eff(C3P7g), \
  Eff(C3P8g), \
  Eff(C3P9g)
)

print 'Lc+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C4P0g), \
  Eff(C4P1g), \
  Eff(C4P2g), \
  Eff(C4P3g), \
  Eff(C4P4g), \
  Eff(C4P5g), \
  Eff(C4P6g), \
  Eff(C4P7g), \
  Eff(C4P8g), \
  Eff(C4P9g)
)

print '********************************************************************* Geometry Selection Success %.5f' %(tGS/inGeo)

print '********************************************************************************************************'

print '       0 Prong   1 Prong   2 Prong   3 Prong   4 Prong   5 Prong   6 Prong   7 Prong   8 Prong   9 Prong'

print 'D+  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C1P0l), \
  Eff(C1P1l), \
  Eff(C1P2l), \
  Eff(C1P3l), \
  Eff(C1P4l), \
  Eff(C1P5l), \
  Eff(C1P6l), \
  Eff(C1P7l), \
  Eff(C1P8l), \
  Eff(C1P9l)
)

print 'D0  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C2P0l), \
  Eff(C2P1l), \
  Eff(C2P2l), \
  Eff(C2P3l), \
  Eff(C2P4l), \
  Eff(C2P5l), \
  Eff(C2P6l), \
  Eff(C2P7l), \
  Eff(C2P8l), \
  Eff(C2P9l)
)

print 'Ds+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C3P0l), \
  Eff(C3P1l), \
  Eff(C3P2l), \
  Eff(C3P3l), \
  Eff(C3P4l), \
  Eff(C3P5l), \
  Eff(C3P6l), \
  Eff(C3P7l), \
  Eff(C3P8l), \
  Eff(C3P9l)
)

print 'Lc+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C4P0l), \
  Eff(C4P1l), \
  Eff(C4P2l), \
  Eff(C4P3l), \
  Eff(C4P4l), \
  Eff(C4P5l), \
  Eff(C4P6l), \
  Eff(C4P7l), \
  Eff(C4P8l), \
  Eff(C4P9l)
)

print '********************************************************************* Location Selection Success %.5f' %(tLS/inGeo)

print '********************************************************************************************************'

print '       0 Prong   1 Prong   2 Prong   3 Prong   4 Prong   5 Prong   6 Prong   7 Prong   8 Prong   9 Prong'

print 'D+  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C1P0d), \
  Eff(C1P1d), \
  Eff(C1P2d), \
  Eff(C1P3d), \
  Eff(C1P4d), \
  Eff(C1P5d), \
  Eff(C1P6d), \
  Eff(C1P7d), \
  Eff(C1P8d), \
  Eff(C1P9d)
)

print 'D0  |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C2P0d), \
  Eff(C2P1d), \
  Eff(C2P2d), \
  Eff(C2P3d), \
  Eff(C2P4d), \
  Eff(C2P5d), \
  Eff(C2P6d), \
  Eff(C2P7d), \
  Eff(C2P8d), \
  Eff(C2P9d)
)

print 'Ds+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C3P0d), \
  Eff(C3P1d), \
  Eff(C3P2d), \
  Eff(C3P3d), \
  Eff(C3P4d), \
  Eff(C3P5d), \
  Eff(C3P6d), \
  Eff(C3P7d), \
  Eff(C3P8d), \
  Eff(C3P9d)
)

print 'Lc+ |  %s   %s   %s   %s   %s   %s   %s   %s   %s   %s' %(   \
  Eff(C4P0d), \
  Eff(C4P1d), \
  Eff(C4P2d), \
  Eff(C4P3d), \
  Eff(C4P4d), \
  Eff(C4P5d), \
  Eff(C4P6d), \
  Eff(C4P7d), \
  Eff(C4P8d), \
  Eff(C4P9d)
)

print '***************************************************************** Decay Search Selection Success %.5f' %(tDSS/inGeo)

print '********************************************************************************************************'

C1Fr = CCounter[0]/sum(CCounter)
C2Fr = CCounter[1]/sum(CCounter)
C3Fr = CCounter[2]/sum(CCounter)
C4Fr = CCounter[3]/sum(CCounter)

#print '      Fraction     Number    Selected'
print '    | Production |                            Selection '
print '    |  Fraction  |  Produced     Selected       Ratio   '
print '    |  --------  |  --------     --------      -------  '
print 'D+  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C1Fr, CCounter[0], CCounterS[0], CCounterS[0]/CCounter[0])
print 'D0  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C2Fr, CCounter[1], CCounterS[1], CCounterS[1]/CCounter[1])
print 'Ds+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C3Fr, CCounter[2], CCounterS[2], CCounterS[2]/CCounter[2])
print 'Lc+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C4Fr, CCounter[3], CCounterS[3], CCounterS[3]/CCounter[3])
print '******************************************************************** Associated Charmed Hadron Fractions'

print '********************************************************************************************************'
print 'Total #of Events | After Geometrical Selection | After Location Selection | After Decay Search Selection'
print '     %6.0f                 %6.0f                       %6.0f                     %6.0f' %(inGeo, tGS, tLS, tDSS)

print '********************************************************************************************************'
print '*                                                                                                      *'
print '********************************************************************************************************'

#makePlots()
elikkayalib.finish()

#end of the script
