import ROOT as r
import rootUtils as ut
import elikkayalib, argparse

from physlib import *

def init():
  ap = argparse.ArgumentParser(
      description='Run the dummy builder')
  ap.add_argument('--work_dir', type=str, help="work space path", dest='work_dir', default=None)
  #ap.add_argument('-n', type=int, help="number of ROOT files to handle", dest='n_files', default=None)
  args = ap.parse_args()
  return args

args = init() #to get the options

work_dir = args.work_dir
#n_files = args.n_files

t = elikkayalib.configure()

g = r.TFile('/eos/experiment/ship/user/eelikkaya/events_geo/event_CharmCCDIS_Jul18/nu_mu/0/geofile_full.conical.Genie-TGeant4.root')
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

nEnt = t.fChain.GetEntries()

inGeo, tGS, tLS, tDSS = 0., 0., 0., 0.
d_plus, d_zero, ds_plus, lambda_c = 0., 0., 0., 0.
CCounter = [d_plus, d_zero, ds_plus, lambda_c]

'''
NOP0 = 0.
NOP1 = 0.
NOP2 = 0.
NOP3 = 0.
NOP4 = 0.
NOP5 = 0.
NOP6 = 0.
NOP7 = 0.
NOP8 = 0.
NOP9 = 0.
'''

Hadron = [-130, -211, -321, -2212, 130, 211, 321, 2212]
Lepton = [-11, -13, -15, 11, 13, 15]

CharmedHadron = [411, 421, 431, 4122]
Chargeless = [-14, 22, 111, 130, 421, 2112]

h = {}
ut.bookHist(h, 'charm_fraction', 'Charm Fractions', 4, 0, 4)
ut.bookHist(h, 'gC1E', 'Charmed Hadron Energy Spectrum D+', 20, 0, 100)
ut.bookHist(h, 'gC1ES', 'Charmed Hadron Energy Spectrum D+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'gC2E', 'Charmed Hadron Energy Spectrum D0', 20, 0, 100)
ut.bookHist(h, 'gC2ES', 'Charmed Hadron Energy Spectrum D0 (Selected)', 20, 0, 100)
ut.bookHist(h, 'gC3E', 'Charmed Hadron Energy Spectrum Ds+', 20, 0, 100)
ut.bookHist(h, 'gC3ES', 'Charmed Hadron Energy Spectrum Ds+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'gC4E', 'Charmed Hadron Energy Spectrum Lc+', 20, 0, 100)
ut.bookHist(h, 'gC4ES', 'Charmed Hadron Energy Spectrum Lc+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'gC1FL', 'Charmed Hadron Flight Length D+', 100, 0, 1)
ut.bookHist(h, 'gC1FLS', 'Charmed Hadron Flight Length D+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'gC2FL', 'Charmed Hadron Flight Length D0', 100, 0, 1)
ut.bookHist(h, 'gC2FLS', 'Charmed Hadron Flight Length D0 (Selected)', 100, 0, 1)
ut.bookHist(h, 'gC3FL', 'Charmed Hadron Flight Length Ds+', 100, 0, 1)
ut.bookHist(h, 'gC3FLS', 'Charmed Hadron Flight Length Ds+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'gC4FL', 'Charmed Hadron Flight Length Lc+', 100, 0, 1)
ut.bookHist(h, 'gC4FLS', 'Charmed Hadron Flight Length Lc+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'gC1M', 'Charmed Hadron Multiplicity at Primary Vertex D+', 15, 0, 15)
ut.bookHist(h, 'gC1MS', 'Charmed Hadron Multiplicity at Primary Vertex D+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'gC2M', 'Charmed Hadron Multiplicity at Primary Vertex D0', 15, 0, 15)
ut.bookHist(h, 'gC2MS', 'Charmed Hadron Multiplicity at Primary Vertex D0 (Selected)', 15, 0, 15)
ut.bookHist(h, 'gC3M', 'Charmed Hadron Multiplicity at Primary Vertex Ds+', 15, 0, 15)
ut.bookHist(h, 'gC3MS', 'Charmed Hadron Multiplicity at Primary Vertex Ds+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'gC4M', 'Charmed Hadron Multiplicity at Primary Vertex Lc+', 15, 0, 15)
ut.bookHist(h, 'gC4MS', 'Charmed Hadron Multiplicity at Primary Vertex Lc+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'gC1M2', 'Charmed Hadron Multiplicity at Secondary Vertex D+', 8, 0, 8)
ut.bookHist(h, 'gC1M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'gC2M2', 'Charmed Hadron Multiplicity at Secondary Vertex D0', 8, 0, 8)
ut.bookHist(h, 'gC2M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D0 (Selected)', 8, 0, 8)
ut.bookHist(h, 'gC3M2', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+', 8, 0, 8)
ut.bookHist(h, 'gC3M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'gC4M2', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+', 8, 0, 8)
ut.bookHist(h, 'gC4M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'lC1E', 'Charmed Hadron Energy Spectrum D+', 20, 0, 100)
ut.bookHist(h, 'lC1ES', 'Charmed Hadron Energy Spectrum D+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'lC2E', 'Charmed Hadron Energy Spectrum D0', 20, 0, 100)
ut.bookHist(h, 'lC2ES', 'Charmed Hadron Energy Spectrum D0 (Selected)', 20, 0, 100)
ut.bookHist(h, 'lC3E', 'Charmed Hadron Energy Spectrum Ds+', 20, 0, 100)
ut.bookHist(h, 'lC3ES', 'Charmed Hadron Energy Spectrum Ds+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'lC4E', 'Charmed Hadron Energy Spectrum Lc+', 20, 0, 100)
ut.bookHist(h, 'lC4ES', 'Charmed Hadron Energy Spectrum Lc+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'lC1FL', 'Charmed Hadron Flight Length D+', 100, 0, 1)
ut.bookHist(h, 'lC1FLS', 'Charmed Hadron Flight Length D+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'lC2FL', 'Charmed Hadron Flight Length D0', 100, 0, 1)
ut.bookHist(h, 'lC2FLS', 'Charmed Hadron Flight Length D0 (Selected)', 100, 0, 1)
ut.bookHist(h, 'lC3FL', 'Charmed Hadron Flight Length Ds+', 100, 0, 1)
ut.bookHist(h, 'lC3FLS', 'Charmed Hadron Flight Length Ds+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'lC4FL', 'Charmed Hadron Flight Length Lc+', 100, 0, 1)
ut.bookHist(h, 'lC4FLS', 'Charmed Hadron Flight Length Lc+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'lC1M', 'Charmed Hadron Multiplicity at Primary Vertex D+', 15, 0, 15)
ut.bookHist(h, 'lC1MS', 'Charmed Hadron Multiplicity at Primary Vertex D+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'lC2M', 'Charmed Hadron Multiplicity at Primary Vertex D0', 15, 0, 15)
ut.bookHist(h, 'lC2MS', 'Charmed Hadron Multiplicity at Primary Vertex D0 (Selected)', 15, 0, 15)
ut.bookHist(h, 'lC3M', 'Charmed Hadron Multiplicity at Primary Vertex Ds+', 15, 0, 15)
ut.bookHist(h, 'lC3MS', 'Charmed Hadron Multiplicity at Primary Vertex Ds+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'lC4M', 'Charmed Hadron Multiplicity at Primary Vertex Lc+', 15, 0, 15)
ut.bookHist(h, 'lC4MS', 'Charmed Hadron Multiplicity at Primary Vertex Lc+ (Selected)', 15, 0, 15)
ut.bookHist(h, 'lC1M2', 'Charmed Hadron Multiplicity at Secondary Vertex D+', 8, 0, 8)
ut.bookHist(h, 'lC1M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'lC2M2', 'Charmed Hadron Multiplicity at Secondary Vertex D0', 8, 0, 8)
ut.bookHist(h, 'lC2M2S', 'Charmed Hadron Multiplicity at Secondary Vertex D0 (Selected)', 8, 0, 8)
ut.bookHist(h, 'lC3M2', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+', 8, 0, 8)
ut.bookHist(h, 'lC3M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Ds+ (Selected)', 8, 0, 8)
ut.bookHist(h, 'lC4M2', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+', 8, 0, 8)
ut.bookHist(h, 'lC4M2S', 'Charmed Hadron Multiplicity at Secondary Vertex Lc+ (Selected)', 8, 8, 8)
ut.bookHist(h, 'dC1E', 'Charmed Hadron Energy Spectrum D+', 20, 0, 100)
ut.bookHist(h, 'dC1ES', 'Charmed Hadron Energy Spectrum D+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'dC2E', 'Charmed Hadron Energy Spectrum D0', 20, 0, 100)
ut.bookHist(h, 'dC2ES', 'Charmed Hadron Energy Spectrum D0 (Selected)', 20, 0, 100)
ut.bookHist(h, 'dC3E', 'Charmed Hadron Energy Spectrum Ds+', 20, 0, 100)
ut.bookHist(h, 'dC3ES', 'Charmed Hadron Energy Spectrum Ds+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'dC4E', 'Charmed Hadron Energy Spectrum Lc+', 20, 0, 100)
ut.bookHist(h, 'dC4ES', 'Charmed Hadron Energy Spectrum Lc+ (Selected)', 20, 0, 100)
ut.bookHist(h, 'dC1FL', 'Charmed Hadron Flight Length D+', 200, 0, 1)
ut.bookHist(h, 'dC1FLS', 'Charmed Hadron Flight Length D+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'dC2FL', 'Charmed Hadron Flight Length D0', 100, 0, 1)
ut.bookHist(h, 'dC2FLS', 'Charmed Hadron Flight Length D0 (Selected)', 100, 0, 1)
ut.bookHist(h, 'dC3FL', 'Charmed Hadron Flight Length Ds+', 100, 0, 1)
ut.bookHist(h, 'dC3FLS', 'Charmed Hadron Flight Length Ds+ (Selected)', 100, 0, 1)
ut.bookHist(h, 'dC4FL', 'Charmed Hadron Flight Length Lc+', 100, 0, 1)
ut.bookHist(h, 'dC4FLS', 'Charmed Hadron Flight Length Lc+ (Selected)', 100, 0, 1)
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

h['charm_fraction'].GetXaxis().SetBinLabel(1, "D^{+}")
h['charm_fraction'].GetXaxis().SetBinLabel(2, "D^{0}")
h['charm_fraction'].GetXaxis().SetBinLabel(3, "D_{s}^{+}")
h['charm_fraction'].GetXaxis().SetBinLabel(4, "#Lambda_{c}^{+}")

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
  if CharmPDG == 411:
    h.Fill(0, 1)
    CCounter[0] += 1.
  if CharmPDG == 421:
    h.Fill(1, 1)
    CCounter[1] += 1.
  if CharmPDG == 431:
    h.Fill(2, 1)
    CCounter[2] += 1.
  if CharmPDG == 4122:
    h.Fill(3, 1)
    CCounter[3] += 1.

def makePlots():
  ut.bookCanvas(h,key='FractionAnalysis',title='Produced Charmed Hadron Fractions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['FractionAnalysis'].cd(1)
  h['charm_fraction'].Draw()
  h['FractionAnalysis'].Print(work_dir+'/histo/cfraction.pdf')
  ut.bookCanvas(h,key='gEnergyAnalysis',title='Produced Charmed Hadron Energies',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['gEnergyAnalysis'].cd(1)
  h['gC1E'].Draw()
  h['gC1ES'].SetFillStyle(3335)
  h['gC1ES'].SetFillColor(2)
  h['gC1ES'].SetXTitle('Energy (GeV)')
  h['gC1ES'].Draw('same')
  cv = h['gEnergyAnalysis'].cd(2)
  h['gC2E'].Draw()
  h['gC2ES'].SetFillStyle(3335)
  h['gC2ES'].SetFillColor(2)
  h['gC2ES'].SetXTitle('Energy (GeV)')
  h['gC2ES'].Draw('same')
  cv = h['gEnergyAnalysis'].cd(3)
  h['gC3E'].Draw()
  h['gC3ES'].SetFillStyle(3335)
  h['gC3ES'].SetFillColor(2)
  h['gC3ES'].SetXTitle('Energy (GeV)')
  h['gC3ES'].Draw('same')
  cv = h['gEnergyAnalysis'].cd(4)
  h['gC4E'].Draw()
  h['gC4ES'].SetFillStyle(3335)
  h['gC4ES'].SetFillColor(2)
  h['gC4ES'].SetXTitle('Energy (GeV)')
  h['gC4ES'].Draw('same')
  h['gEnergyAnalysis'].Print(work_dir+'/histo/gcenergy.pdf')
  ut.bookCanvas(h,key='gFLAnalysis',title='Produced Charmed Hadron Flight Lengths',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['gFLAnalysis'].cd(1)
  h['gC1FL'].Draw()
  h['gC1FLS'].SetFillStyle(3335)
  h['gC1FLS'].SetFillColor(2)
  h['gC1FLS'].Draw('same')
  cv = h['gFLAnalysis'].cd(2)
  h['gC2FL'].Draw()
  h['gC2FLS'].SetFillStyle(3335)
  h['gC2FLS'].SetFillColor(2)
  h['gC2FLS'].Draw('same')
  cv = h['gFLAnalysis'].cd(3)
  h['gC3FL'].Draw()
  h['gC3FLS'].SetFillStyle(3335)
  h['gC3FLS'].SetFillColor(2)
  h['gC3FLS'].Draw('same')
  cv = h['gFLAnalysis'].cd(4)
  h['gC4FL'].Draw()
  h['gC4FLS'].SetFillStyle(3335)
  h['gC4FLS'].SetFillColor(2)
  h['gC4FLS'].Draw('same')
  h['gFLAnalysis'].Print(work_dir+'/histo/gcfl.pdf')
  ut.bookCanvas(h,key='gMultAnalysis',title='Multiplicity at Primary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['gMultAnalysis'].cd(1)
  h['gC1M'].Draw()
  h['gC1MS'].SetFillStyle(3335)
  h['gC1MS'].SetFillColor(2)
  h['gC1MS'].Draw('same')
  cv = h['gMultAnalysis'].cd(2)
  h['gC2M'].Draw()
  h['gC2MS'].SetFillStyle(3335)
  h['gC2MS'].SetFillColor(2)
  h['gC2MS'].Draw('same')
  cv = h['gMultAnalysis'].cd(3)
  h['gC3M'].Draw()
  h['gC3MS'].SetFillStyle(3335)
  h['gC3MS'].SetFillColor(2)
  h['gC3MS'].Draw('same')
  cv = h['gMultAnalysis'].cd(4)
  h['gC4M'].Draw()
  h['gC4MS'].SetFillStyle(3335)
  h['gC4MS'].SetFillColor(2)
  h['gC4MS'].Draw('same')
  h['gMultAnalysis'].Print(work_dir+'/histo/gcmult.pdf')
  ut.bookCanvas(h,key='gMultAnalysis2',title='Multiplicity at Secondary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['gMultAnalysis2'].cd(1)
  h['gC1M2'].Draw()
  h['gC1M2S'].SetFillStyle(3335)
  h['gC1M2S'].SetFillColor(2)
  h['gC1M2S'].Draw('same')
  cv = h['gMultAnalysis2'].cd(2)
  h['gC2M2'].Draw()
  h['gC2M2S'].SetFillStyle(3335)
  h['gC2M2S'].SetFillColor(2)
  h['gC2M2S'].Draw('same')
  cv = h['gMultAnalysis2'].cd(3)
  h['gC3M2'].Draw()
  h['gC3M2S'].SetFillStyle(3335)
  h['gC3M2S'].SetFillColor(2)
  h['gC3M2S'].Draw('same')
  cv = h['gMultAnalysis2'].cd(4)
  h['gC4M2'].Draw()
  h['gC4M2S'].SetFillStyle(3335)
  h['gC4M2S'].SetFillColor(2)
  h['gC4M2S'].Draw('same')
  h['gMultAnalysis2'].Print(work_dir+'/histo/gcmult2.pdf')
  ut.bookCanvas(h,key='lEnergyAnalysis',title='Produced Charmed Hadron Energies',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['lEnergyAnalysis'].cd(1)
  h['lC1E'].Draw()
  h['lC1ES'].SetFillStyle(3335)
  h['lC1ES'].SetFillColor(2)
  h['lC1ES'].Draw('same')
  cv = h['lEnergyAnalysis'].cd(2)
  h['lC2E'].Draw()
  h['lC2ES'].SetFillStyle(3335)
  h['lC2ES'].SetFillColor(2)
  h['lC2ES'].Draw('same')
  cv = h['lEnergyAnalysis'].cd(3)
  h['lC3E'].Draw()
  h['lC3ES'].SetFillStyle(3335)
  h['lC3ES'].SetFillColor(2)
  h['lC3ES'].Draw('same')
  cv = h['lEnergyAnalysis'].cd(4)
  h['lC4E'].Draw()
  h['lC4ES'].SetFillStyle(3335)
  h['lC4ES'].SetFillColor(2)
  h['lC4ES'].Draw('same')
  h['lEnergyAnalysis'].Print(work_dir+'/histo/lcenergy.pdf')
  ut.bookCanvas(h,key='lFLAnalysis',title='Produced Charmed Hadron Flight Lengths',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['lFLAnalysis'].cd(1)
  h['lC1FL'].Draw()
  h['lC1FLS'].SetFillStyle(3335)
  h['lC1FLS'].SetFillColor(2)
  h['lC1FLS'].Draw('same')
  cv = h['lFLAnalysis'].cd(2)
  h['lC2FL'].Draw()
  h['lC2FLS'].SetFillStyle(3335)
  h['lC2FLS'].SetFillColor(2)
  h['lC2FLS'].Draw('same')
  cv = h['lFLAnalysis'].cd(3)
  h['lC3FL'].Draw()
  h['lC3FLS'].SetFillStyle(3335)
  h['lC3FLS'].SetFillColor(2)
  h['lC3FLS'].Draw('same')
  cv = h['lFLAnalysis'].cd(4)
  h['lC4FL'].Draw()
  h['lC4FLS'].SetFillStyle(3335)
  h['lC4FLS'].SetFillColor(2)
  h['lC4FLS'].Draw('same')
  h['lFLAnalysis'].Print(work_dir+'/histo/lcfl.pdf')
  ut.bookCanvas(h,key='lMultAnalysis',title='Multiplicity at Primary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['lMultAnalysis'].cd(1)
  h['lC1M'].Draw()
  h['lC1MS'].SetFillStyle(3335)
  h['lC1MS'].SetFillColor(2)
  h['lC1MS'].Draw('same')
  cv = h['lMultAnalysis'].cd(2)
  h['lC2M'].Draw()
  h['lC2MS'].SetFillStyle(3335)
  h['lC2MS'].SetFillColor(2)
  h['lC2MS'].Draw('same')
  cv = h['lMultAnalysis'].cd(3)
  h['lC3M'].Draw()
  h['lC3MS'].SetFillStyle(3335)
  h['lC3MS'].SetFillColor(2)
  h['lC3MS'].Draw('same')
  cv = h['lMultAnalysis'].cd(4)
  h['lC4M'].Draw()
  h['lC4MS'].SetFillStyle(3335)
  h['lC4MS'].SetFillColor(2)
  h['lC4MS'].Draw('same')
  h['lMultAnalysis'].Print(work_dir+'/histo/lcmult.pdf')
  ut.bookCanvas(h,key='lMultAnalysis2',title='Multiplicity at Secondary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['lMultAnalysis2'].cd(1)
  h['lC1M2'].Draw()
  h['lC1M2S'].SetFillStyle(3335)
  h['lC1M2S'].SetFillColor(2)
  h['lC1M2S'].Draw('same')
  cv = h['lMultAnalysis2'].cd(2)
  h['lC2M2'].Draw()
  h['lC2M2S'].SetFillStyle(3335)
  h['lC2M2S'].SetFillColor(2)
  h['lC2M2S'].Draw('same')
  cv = h['lMultAnalysis2'].cd(3)
  h['lC3M2'].Draw()
  h['lC3M2S'].SetFillStyle(3335)
  h['lC3M2S'].SetFillColor(2)
  h['lC3M2S'].Draw('same')
  cv = h['lMultAnalysis2'].cd(4)
  h['lC4M2'].Draw()
  h['lC4M2S'].SetFillStyle(3335)
  h['lC4M2S'].SetFillColor(2)
  h['lC4M2S'].Draw('same')
  h['lMultAnalysis2'].Print(work_dir+'/histo/lcmult2.pdf')
  ut.bookCanvas(h,key='dEnergyAnalysis',title='Produced Charmed Hadron Energies',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dEnergyAnalysis'].cd(1)
  h['dC1E'].Draw()
  h['dC1ES'].SetFillStyle(3335)
  h['dC1ES'].SetFillColor(2)
  h['dC1ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(2)
  h['dC2E'].Draw()
  h['dC2ES'].SetFillStyle(3335)
  h['dC2ES'].SetFillColor(2)
  h['dC2ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(3)
  h['dC3E'].Draw()
  h['dC3ES'].SetFillStyle(3335)
  h['dC3ES'].SetFillColor(2)
  h['dC3ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(4)
  h['dC4E'].Draw()
  h['dC4ES'].SetFillStyle(3335)
  h['dC4ES'].SetFillColor(2)
  h['dC4ES'].Draw('same')
  h['dEnergyAnalysis'].Print(work_dir+'/histo/dcenergy.pdf')
  ut.bookCanvas(h,key='dFLAnalysis',title='Produced Charmed Hadron Flight Lengths',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dFLAnalysis'].cd(1)
  h['dC1FL'].Draw()
  h['dC1FLS'].SetFillStyle(3335)
  h['dC1FLS'].SetFillColor(2)
  h['dC1FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(2)
  h['dC2FL'].Draw()
  h['dC2FLS'].SetFillStyle(3335)
  h['dC2FLS'].SetFillColor(2)
  h['dC2FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(3)
  h['dC3FL'].Draw()
  h['dC3FLS'].SetFillStyle(3335)
  h['dC3FLS'].SetFillColor(2)
  h['dC3FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(4)
  h['dC4FL'].Draw()
  h['dC4FLS'].SetFillStyle(3335)
  h['dC4FLS'].SetFillColor(2)
  h['dC4FLS'].Draw('same')
  h['dFLAnalysis'].Print(work_dir+'/histo/dcfl.pdf')
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
  h['dMultAnalysis'].Print(work_dir+'/histo/dcmult.pdf')
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
  h['dMultAnalysis2'].Print(work_dir+'/histo/dcmult2.pdf')

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
  if NProng == 0:
    NOP = 0
  if NProng == 1:
    NOP = 1
  if NProng == 2:
    NOP = 2
  if NProng == 3:
    NOP = 3
  if NProng == 4:
    NOP = 4
  if NProng == 5:
    NOP = 5
  if NProng == 6:
    NOP = 6
  if NProng == 7:
    NOP = 7
  if NProng == 8:
    NOP = 8
  if NProng == 9:
    NOP = 9
  return NOP

def ChannelDecision(CPdg, NOP):
  if CPdg == 411  and NOP == 0:
    ch = 10
  if CPdg == 421  and NOP == 0:
    ch = 20
  if CPdg == 431  and NOP == 0:
    ch = 30
  if CPdg == 4122 and NOP == 0:
    ch = 40
  if CPdg == 411  and NOP == 1:
    ch = 11
  if CPdg == 421  and NOP == 1:
    ch = 21
  if CPdg == 431  and NOP == 1:
    ch = 31
  if CPdg == 4122 and NOP == 1:
    ch = 41
  if CPdg == 411  and NOP == 2:
    ch = 12
  if CPdg == 421  and NOP == 2:
    ch = 22
  if CPdg == 431  and NOP == 2:
    ch = 32
  if CPdg == 4122 and NOP == 2:
    ch = 42
  if CPdg == 411  and NOP == 3:
    ch = 13
  if CPdg == 421  and NOP == 3:
    ch = 23
  if CPdg == 431  and NOP == 3:
    ch = 33
  if CPdg == 4122 and NOP == 3:
    ch = 43
  if CPdg == 411  and NOP == 4:
    ch = 14
  if CPdg == 421  and NOP == 4:
    ch = 24
  if CPdg == 431  and NOP == 4:
    ch = 34
  if CPdg == 4122 and NOP == 4:
    ch = 44
  if CPdg == 411  and NOP == 5:
    ch = 15
  if CPdg == 421  and NOP == 5:
    ch = 25
  if CPdg == 431  and NOP == 5:
    ch = 35
  if CPdg == 4122 and NOP == 5:
    ch = 45
  if CPdg == 411  and NOP == 6:
    ch = 16
  if CPdg == 421  and NOP == 6:
    ch = 26
  if CPdg == 431  and NOP == 6:
    ch = 36
  if CPdg == 4122 and NOP == 6:
    ch = 46
  if CPdg == 411  and NOP == 7:
    ch = 17
  if CPdg == 421  and NOP == 7:
    ch = 27
  if CPdg == 431  and NOP == 7:
    ch = 37
  if CPdg == 4122 and NOP == 7:
    ch = 47
  if CPdg == 411  and NOP == 8:
    ch = 18
  if CPdg == 421  and NOP == 8:
    ch = 28
  if CPdg == 431  and NOP == 8:
    ch = 38
  if CPdg == 4122 and NOP == 8:
    ch = 48
  if CPdg == 411  and NOP == 9:
    ch = 19
  if CPdg == 421  and NOP == 9:
    ch = 29
  if CPdg == 431  and NOP == 9:
    ch = 39
  if CPdg == 4122 and NOP == 9:
    ch = 49
  return ch

for event in xrange(nEnt):

  t.GetEntry(event)

  if (t.IntInGeo.at(0)):

    CDauPdg = []
    PriVertexPdg = []
    LS = []
    DSS = []
    delProng = False

    for vtx in xrange(t.VertexInfo.size()):

      if t.VertexInfo.at(vtx) == 1:
        Pos = []
        Pos.append(t.StartX.at(vtx))
        Pos.append(t.StartY.at(vtx))
        Pos.append(t.StartZ.at(vtx))
        Mom = []
        Mom.append(t.Px.at(vtx))
        Mom.append(t.Py.at(vtx))
        Mom.append(t.Pz.at(vtx))
        Mom.append(t.P.at(vtx))
        Pdg = t.PdgCode.at(vtx)
        PriVertexPdg.append(Pdg)
        if Pdg in CharmedHadron:
          CMom = []
          CMom.append(t.Px.at(vtx))
          CMom.append(t.Py.at(vtx))
          CMom.append(t.Pz.at(vtx))
          CMom.append(t.P.at(vtx))
          CPdg = Pdg
          #CharmFraction(CPdg, h['charm_fraction'], CCounter)
          CEnergy = t.Energy.at(vtx)
        if LocationSelection(Mom, Pdg):
          LS.append(True)
        else: LS.append(False)

      if t.VertexInfo.at(vtx) == 22:
        CDauPos = []
        CDauPos.append(t.StartX.at(vtx))
        CDauPos.append(t.StartY.at(vtx))
        CDauPos.append(t.StartZ.at(vtx))
        CDauMom = []
        CDauMom.append(t.Px.at(vtx))
        CDauMom.append(t.Py.at(vtx))
        CDauMom.append(t.Pz.at(vtx))
        CDauMom.append(t.P.at(vtx))
        CDauPdg.append(t.PdgCode.at(vtx))

      try: Pos, CMom, CDauPos, CDauMom
      except NameError: continue
      else:
        fl = FlightLength(CDauPos, Pos)
        if DecaySearchSelection(Pos, CMom, CDauPos, CDauMom):
          DSS.append(True)
          del CDauPos, CDauMom
        else:
          DSS.append(False)

    NOP = ProngCount(CDauPdg)
    ch = ChannelDecision(CPdg, NOP)
    MultPri = Multiplicity(PriVertexPdg, Chargeless)
    MultSec = Multiplicity(CDauPdg, Chargeless)

    if CPdg in [411, 431, 4122] and NOP not in [1, 3, 5, 7]:
      delProng = True
    if CPdg == 421 and NOP not in [0, 2, 4, 6]:
      delProng = True

      '''
      if NOP == 0:
        NOP0 += 1
      if NOP == 1:
        NOP1 += 1
      if NOP == 2:
        NOP2 += 1
      if NOP == 3:
        NOP3 += 1
      if NOP == 4:
        NOP4 += 1
      if NOP == 5:
        NOP5 += 1
      if NOP == 6:
        NOP6 += 1
      if NOP == 7:
        NOP7 += 1
      if NOP == 8:
        NOP8 += 1
      if NOP == 9:
        NOP9 += 1
      '''

    if not delProng:

      CharmFraction(CPdg, h['charm_fraction'], CCounter)
      inGeo += 1.

      if CPdg == 411:
        h['gC1E'].Fill(CEnergy)
        h['lC1E'].Fill(CEnergy)
        h['dC1E'].Fill(CEnergy)
        h['gC1FL'].Fill(fl)
        h['dC1FL'].Fill(fl)
        h['lC1FL'].Fill(fl)
        h['gC1M'].Fill(MultPri)
        h['dC1M'].Fill(MultPri)
        h['lC1M'].Fill(MultPri)
        h['gC1M2'].Fill(MultSec)
        h['dC1M2'].Fill(MultSec)
        h['lC1M2'].Fill(MultSec)
      elif CPdg == 421:
        h['gC2E'].Fill(CEnergy)
        h['lC2E'].Fill(CEnergy)
        h['dC2E'].Fill(CEnergy)
        h['gC2FL'].Fill(fl)
        h['dC2FL'].Fill(fl)
        h['lC2FL'].Fill(fl)
        h['gC2M'].Fill(MultPri)
        h['dC2M'].Fill(MultPri)
        h['lC2M'].Fill(MultPri)
        h['gC2M2'].Fill(MultSec)
        h['dC2M2'].Fill(MultSec)
        h['lC2M2'].Fill(MultSec)
      elif CPdg == 431:
        h['gC3E'].Fill(CEnergy)
        h['lC3E'].Fill(CEnergy)
        h['dC3E'].Fill(CEnergy)
        h['gC3FL'].Fill(fl)
        h['dC3FL'].Fill(fl)
        h['lC3FL'].Fill(fl)
        h['gC3M'].Fill(MultPri)
        h['dC3M'].Fill(MultPri)
        h['lC3M'].Fill(MultPri)
        h['gC3M2'].Fill(MultSec)
        h['dC3M2'].Fill(MultSec)
        h['lC3M2'].Fill(MultSec)
      elif CPdg == 4122:
        h['gC4E'].Fill(CEnergy)
        h['lC4E'].Fill(CEnergy)
        h['dC4E'].Fill(CEnergy)
        h['gC4FL'].Fill(fl)
        h['dC4FL'].Fill(fl)
        h['lC4FL'].Fill(fl)
        h['gC4M'].Fill(MultPri)
        h['dC4M'].Fill(MultPri)
        h['lC4M'].Fill(MultPri)
        h['gC4M2'].Fill(MultSec)
        h['dC4M2'].Fill(MultSec)
        h['lC4M2'].Fill(MultSec)

      if GeometrySelection(Pos):

        if CPdg == 411:
          h['gC1ES'].Fill(CEnergy)
          h['gC1FLS'].Fill(fl)
          h['gC1MS'].Fill(MultPri)
          h['gC1M2S'].Fill(MultSec)
        elif CPdg == 421:
          h['gC2ES'].Fill(CEnergy)
          h['gC2FLS'].Fill(fl)
          h['gC2MS'].Fill(MultPri)
          h['gC2M2S'].Fill(MultSec)
        elif CPdg == 431:
          h['gC3ES'].Fill(CEnergy)
          h['gC3FLS'].Fill(fl)
          h['gC3MS'].Fill(MultPri)
          h['gC3M2S'].Fill(MultSec)
        elif CPdg == 4122:
          h['gC4ES'].Fill(CEnergy)
          h['gC4FLS'].Fill(fl)
          h['gC4MS'].Fill(MultPri)
          h['gC4M2S'].Fill(MultSec)

        if True in LS:
          if CPdg == 411:
            h['lC1ES'].Fill(CEnergy)
            h['lC1FLS'].Fill(fl)
            h['lC1MS'].Fill(MultPri)
            h['lC1M2S'].Fill(MultSec)
          elif CPdg == 421:
            h['lC2ES'].Fill(CEnergy)
            h['lC2FLS'].Fill(fl)
            h['lC2MS'].Fill(MultPri)
            h['lC2M2S'].Fill(MultSec)
          elif CPdg == 431:
            h['lC3ES'].Fill(CEnergy)
            h['lC3FLS'].Fill(fl)
            h['lC3MS'].Fill(MultPri)
            h['lC3M2S'].Fill(MultSec)
          elif CPdg == 4122:
            h['lC4ES'].Fill(CEnergy)
            h['lC4FLS'].Fill(fl)
            h['lC4MS'].Fill(MultPri)
            h['lC4M2S'].Fill(MultSec)

          if True in DSS:
            if CPdg == 411:
              h['dC1ES'].Fill(CEnergy)
              h['dC1FLS'].Fill(fl)
              h['dC1MS'].Fill(MultPri)
              h['dC1M2S'].Fill(MultSec)
            elif CPdg == 421:
              h['dC2ES'].Fill(CEnergy)
              h['dC2FLS'].Fill(fl)
              h['dC2MS'].Fill(MultPri)
              h['dC2M2S'].Fill(MultSec)
            elif CPdg == 431:
              h['dC3ES'].Fill(CEnergy)
              h['dC3FLS'].Fill(fl)
              h['dC3MS'].Fill(MultPri)
              h['dC3M2S'].Fill(MultSec)
            elif CPdg == 4122:
              h['dC4ES'].Fill(CEnergy)
              h['dC4FLS'].Fill(fl)
              h['dC4MS'].Fill(MultPri)
              h['dC4M2S'].Fill(MultSec)

      if ch == 10:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P0g.append(True)
          if True in LS:
            tLS += 1.
            C1P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P0d.append(True)
            else: C1P0d.append(False)
          else: C1P0l.append(False)
        else: C1P0g.append(False)

      if ch == 20:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P0g.append(True)
          if True in LS:
            tLS += 1.
            C2P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P0d.append(True)
            else: C2P0d.append(False)
          else: C2P0l.append(False)
        else: C2P0g.append(False)

      if ch == 30:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P0g.append(True)
          if True in LS:
            tLS += 1.
            C3P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P0d.append(True)
            else: C3P0d.append(False)
          else: C3P0l.append(False)
        else: C3P0g.append(False)

      if ch == 40:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P0g.append(True)
          if True in LS:
            tLS += 1.
            C4P0l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P0d.append(True)
            else: C4P0d.append(False)
          else: C4P0l.append(False)
        else: C4P0g.append(False)

      if ch == 11:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P1g.append(True)
          if True in LS:
            tLS += 1.
            C1P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P1d.append(True)
            else: C1P1d.append(False)
          else: C1P1l.append(False)
        else: C1P1g.append(False)

      if ch == 21:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P1g.append(True)
          if True in LS:
            tLS += 1.
            C2P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P1d.append(True)
            else: C2P1d.append(False)
          else: C2P1l.append(False)
        else: C2P1g.append(False)

      if ch == 31:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P1g.append(True)
          if True in LS:
            tLS += 1.
            C3P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P1d.append(True)
            else: C3P1d.append(False)
          else: C3P1l.append(False)
        else: C3P1g.append(False)

      if ch == 41:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P1g.append(True)
          if True in LS:
            tLS += 1.
            C4P1l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P1d.append(True)
            else: C4P1d.append(False)
          else: C4P1l.append(False)
        else: C4P1g.append(False)

      if ch == 12:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P2g.append(True)
          if True in LS:
            tLS += 1.
            C1P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P2d.append(True)
            else: C1P2d.append(False)
          else: C1P2l.append(False)
        else: C1P2g.append(False)

      if ch == 22:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P2g.append(True)
          if True in LS:
            tLS += 1.
            C2P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P2d.append(True)
            else: C2P2d.append(False)
          else: C2P2l.append(False)
        else: C2P2g.append(False)

      if ch == 32:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P2g.append(True)
          if True in LS:
            tLS += 1.
            C3P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P2d.append(True)
            else: C3P2d.append(False)
          else: C3P2l.append(False)
        else: C3P2g.append(False)

      if ch == 42:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P2g.append(True)
          if True in LS:
            tLS += 1.
            C4P2l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P2d.append(True)
            else: C4P2d.append(False)
          else: C4P2l.append(False)
        else: C4P2g.append(False)

      if ch == 13:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P3g.append(True)
          if True in LS:
            tLS += 1.
            C1P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P3d.append(True)
            else: C1P3d.append(False)
          else: C1P3l.append(False)
        else: C1P3g.append(False)

      if ch == 23:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P3g.append(True)
          if True in LS:
            tLS += 1.
            C2P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P3d.append(True)
            else: C2P3d.append(False)
          else: C2P3l.append(False)
        else: C2P3g.append(False)

      if ch == 33:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P3g.append(True)
          if True in LS:
            tLS += 1.
            C3P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P3d.append(True)
            else: C3P3d.append(False)
          else: C3P3l.append(False)
        else: C3P3g.append(False)

      if ch == 43:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P3g.append(True)
          if True in LS:
            tLS += 1.
            C4P3l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P3d.append(True)
            else: C4P3d.append(False)
          else: C4P3l.append(False)
        else: C4P3g.append(False)

      if ch == 14:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P4g.append(True)
          if True in LS:
            tLS += 1.
            C1P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P4d.append(True)
            else: C1P4d.append(False)
          else: C1P4l.append(False)
        else: C1P4g.append(False)

      if ch == 24:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P4g.append(True)
          if True in LS:
            tLS += 1.
            C2P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P4d.append(True)
            else: C2P4d.append(False)
          else: C2P4l.append(False)
        else: C2P4g.append(False)

      if ch == 34:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P4g.append(True)
          if True in LS:
            tLS += 1.
            C3P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P4d.append(True)
            else: C3P4d.append(False)
          else: C3P4l.append(False)
        else: C3P4g.append(False)

      if ch == 44:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P4g.append(True)
          if True in LS:
            tLS += 1.
            C4P4l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P4d.append(True)
            else: C4P4d.append(False)
          else: C4P4l.append(False)
        else: C4P4g.append(False)

      if ch == 15:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P5g.append(True)
          if True in LS:
            tLS += 1.
            C1P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P5d.append(True)
            else: C1P5d.append(False)
          else: C1P5l.append(False)
        else: C1P5g.append(False)

      if ch == 25:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P5g.append(True)
          if True in LS:
            tLS += 1.
            C2P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P5d.append(True)
            else: C2P5d.append(False)
          else: C2P5l.append(False)
        else: C2P5g.append(False)

      if ch == 35:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P5g.append(True)
          if True in LS:
            tLS += 1.
            C3P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P5d.append(True)
            else: C3P5d.append(False)
          else: C3P5l.append(False)
        else: C3P5g.append(False)

      if ch == 45:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P5g.append(True)
          if True in LS:
            tLS += 1.
            C4P5l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P5d.append(True)
            else: C4P5d.append(False)
          else: C4P5l.append(False)
        else: C4P5g.append(False)

      if ch == 16:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P6g.append(True)
          if True in LS:
            tLS += 1.
            C1P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P6d.append(True)
            else: C1P6d.append(False)
          else: C1P6d.append(False)
        else: C1P6d.append(False)

      if ch == 26:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P6g.append(True)
          if True in LS:
            tLS += 1.
            C2P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P6d.append(True)
            else: C2P6d.append(False)
          else: C2P6d.append(False)
        else: C2P6d.append(False)

      if ch == 36:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P6g.append(True)
          if True in LS:
            tLS += 1.
            C3P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P6d.append(True)
            else: C3P6d.append(False)
          else: C3P6d.append(False)
        else: C3P6d.append(False)

      if ch == 46:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P6g.append(True)
          if True in LS:
            tLS += 1.
            C4P6l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P6d.append(True)
            else: C4P6d.append(False)
          else: C4P6d.append(False)
        else: C4P6d.append(False)

      if ch == 17:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P7g.append(True)
          if True in LS:
            tLS += 1.
            C1P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P7d.append(True)
            else: C1P7d.append(False)
          else: C1P7l.append(False)
        else: C1P7g.append(False)

      if ch == 27:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P7g.append(True)
          if True in LS:
            tLS += 1.
            C2P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P7d.append(True)
            else: C2P7d.append(False)
          else: C2P7l.append(False)
        else: C2P7g.append(False)

      if ch == 37:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P7g.append(True)
          if True in LS:
            tLS += 1.
            C3P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P7d.append(True)
            else: C3P7d.append(False)
          else: C3P7l.append(False)
        else: C3P7g.append(False)

      if ch == 47:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P7g.append(True)
          if True in LS:
            tLS += 1.
            C4P7l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P7d.append(True)
            else: C4P7d.append(False)
          else: C4P7l.append(False)
        else: C4P7g.append(False)

      if ch == 18:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P8g.append(True)
          if True in LS:
            tLS += 1.
            C1P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P8d.append(True)
            else: C1P8d.append(False)
          else: C1P8l.append(False)
        else: C1P8g.append(False)

      if ch == 28:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P8g.append(True)
          if True in LS:
            tLS += 1.
            C2P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P8d.append(True)
            else: C2P8d.append(False)
          else: C2P8l.append(False)
        else: C2P8g.append(False)

      if ch == 38:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P8g.append(True)
          if True in LS:
            tLS += 1.
            C3P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P8d.append(True)
            else: C3P8d.append(False)
          else: C3P8l.append(False)
        else: C3P8g.append(False)

      if ch == 48:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P8g.append(True)
          if True in LS:
            tLS += 1.
            C4P8l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P8d.append(True)
            else: C4P8d.append(False)
          else: C4P8l.append(False)
        else: C4P8g.append(False)

      if ch == 19:
        if GeometrySelection(Pos):
          tGS += 1.
          C1P9g.append(True)
          if True in LS:
            tLS += 1.
            C1P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C1P9d.append(True)
            else: C1P9d.append(False)
          else: C1P9l.append(False)
        else: C1P9g.append(False)

      if ch == 29:
        if GeometrySelection(Pos):
          tGS += 1.
          C2P9g.append(True)
          if True in LS:
            tLS += 1.
            C2P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C2P9d.append(True)
            else: C2P9d.append(False)
          else: C2P9l.append(False)
        else: C2P9g.append(False)

      if ch == 39:
        if GeometrySelection(Pos):
          tGS += 1.
          C3P9g.append(True)
          if True in LS:
            tLS += 1.
            C3P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C3P9d.append(True)
            else: C3P9d.append(False)
          else: C3P9l.append(False)
        else: C3P9g.append(False)

      if ch == 49:
        if GeometrySelection(Pos):
          tGS += 1.
          C4P9g.append(True)
          if True in LS:
            tLS += 1.
            C4P9l.append(True)
            if True in DSS:
              tDSS += 1.
              C4P79.append(True)
            else: C4P9d.append(False)
          else: C4P9l.append(False)
        else: C4P9g.append(False)

    else:
      continue

print '*********************************************************************************************************'
print '*                                                                                                       *'
print '*********************************************************************************************************'

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

print '********************************************************************** Geometry Selection Success %.5f' %(tGS/inGeo)

print '*********************************************************************************************************'

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

print '*********************************************************************************************************'

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

print '****************************************************************** Decay Search Selection Success %.5f' %(tDSS/inGeo)

print '*********************************************************************************************************'

C1Fr = CCounter[0]/sum(CCounter)
C2Fr = CCounter[1]/sum(CCounter)
C3Fr = CCounter[2]/sum(CCounter)
C4Fr = CCounter[3]/sum(CCounter)

print '       Fraction'
print 'D+  |  %.4f' %C1Fr
print 'D0  |  %.4f' %C2Fr
print 'Ds+ |  %.4f' %C3Fr
print 'Lc+ |  %.4f' %C4Fr
print '********************************************************************* Associated Charmed Hadron Fractions'

print '*********************************************************************************************************'
print '*                                                                                                       *'
print '*********************************************************************************************************'

'''
testtot = float(NOP0 + NOP1 + NOP2 + NOP3 + NOP4 + NOP5 + NOP6 + NOP7 + NOP8 + NOP9)

print '0 Prong', NOP0/testtot
print '1 Prong', NOP1/testtot
print '2 Prong', NOP2/testtot
print '3 Prong', NOP3/testtot
print '4 Prong', NOP4/testtot
print '5 Prong', NOP5/testtot
print '6 Prong', NOP6/testtot
print '7 Prong', NOP7/testtot
print '8 Prong', NOP8/testtot
print '9 Prong', NOP9/testtot
'''

#makePlots()
elikkayalib.finish()

'''
h['slope'].Draw()
h['slope_acc'].Draw("same")
h['slope_acc'].Sumw2

h['test'].Divide(h['slope_acc'], h['slope'], 1., 1., "B")
h['test'].Draw()

total = h['slope'].Integral()
selected = h['slope_acc'].Integral()
print selected/total*100

note1 = r.TLatex(0.25, 2000, "~23.42%")
note2 = r.TLatex(1.25, 2000, "~50.86%")
note3 = r.TLatex(2.25, 2000, "~12.37%")
note4 = r.TLatex(3.25, 2000, "~13.36%")

note1.Draw("Same")
note2.Draw("Same")
note3.Draw("Same")
note4.Draw("Same")
'''
