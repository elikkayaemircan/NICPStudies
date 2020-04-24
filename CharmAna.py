import ROOT as r
import rootUtils as ut
import elikkayalib, argparse
from histAll import *

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

#fSquark = open(work_dir+'/sQuark_mu.out', 'w')

t = elikkayalib.configure(input_file)

g = r.TFile(geo_file)
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

nEnt = t.fChain.GetEntries()

inGeo, tGS, tLS, tDSS = 0., 0., 0., 0.
d_plus, d_zero, ds_plus, lambda_c = 0., 0., 0., 0.
CCounter = [d_plus, d_zero, ds_plus, lambda_c]
d_plusS, d_zeroS, ds_plusS, lambda_cS = 0., 0., 0., 0.
CCounterS = [d_plusS, d_zeroS, ds_plusS, lambda_cS]

Hadron = [-130, -211, -321, -2212, 130, 211, 321, 2212]
Lepton = [-11, -13, -15, 11, 13, 15]

CharmedHadron = [411, 421, 431, 4122]
Chargeless = [-14, 22, 111, 130, 421, 2112]

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

def CharmFraction(CharmPDG, CCounter):
  if CharmPDG == 411:
    CCounter[0] += 1.
  if CharmPDG == 421:
    CCounter[1] += 1.
  if CharmPDG == 431:
    CCounter[2] += 1.
  if CharmPDG == 4122:
    CCounter[3] += 1.

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

mom4_nucl = r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2)        #Global Variable

lYES = 0.
lNO = 0.

for event in xrange(nEnt):

  t.GetEntry(event)

  if (t.IntInGeo.at(0)):

    PVPdg = []  #PrimaryVertexPdg
    Mom_i, Mom_j, Mom_k, Mom_l = [], [], [], []         #Primary Vertex Momentum
    CDauPdg, CDauPos_i, CDauPos_j, CDauPos_k = [], [], [], []       #Charm PDG and Charm Vertex Position
    CDauMom_i, CDauMom_j, CDauMom_k, CDauMom_l = [], [], [], []         #Charm Daughter Momentum

    GS, LS, DSS = [], [], []        #Selection Counter Arrays
    mom4_nu, mom4_lept = r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.)        #X-Y Calculators
    nuEnergy, lEnergy = 0., 0.      #Primary Vertex Neutrino and Lepton Energies
    delProng = False        #Prong Selector Parameter Default with False

    for vtx in xrange(t.VertexInfo.size()):

      if t.VertexInfo.at(vtx) == 0:
        nuEnergy = t.Energy.at(vtx)
        mom4_nu += r.TLorentzVector(t.Px.at(vtx), t.Py.at(vtx), t.Pz.at(vtx), nuEnergy)
        angNuX = Slope(t.Px.at(vtx), t.Pz.at(vtx))*1000       #in mrad
        angNuY = Slope(t.Py.at(vtx), t.Pz.at(vtx))*1000       #in mrad

      if t.VertexInfo.at(vtx) == 1:
        Pos = []
        Pos.append(t.StartX.at(vtx))
        Pos.append(t.StartY.at(vtx))
        Pos.append(t.StartZ.at(vtx))
        Mom_i.append(t.Px.at(vtx))
        Mom_j.append(t.Py.at(vtx))
        Mom_k.append(t.Pz.at(vtx))
        Mom_l.append(t.P.at(vtx))
        PVPdg.append(int(t.PdgCode.at(vtx)))
        if PVPdg[-1] in CharmedHadron:
          CPos = Pos
          CMom = []
          CMom.append(t.Px.at(vtx))
          CMom.append(t.Py.at(vtx))
          CMom.append(t.Pz.at(vtx))
          CMom.append(t.P.at(vtx))
          CPdg = PVPdg[-1]
          CEnergy = t.Energy.at(vtx)
        if PVPdg[-1] in Lepton:
          lEnergy = t.Energy.at(vtx)
          mom4_lept += r.TLorentzVector(t.Px.at(vtx), t.Py.at(vtx), t.Pz.at(vtx), t.Energy.at(vtx))

      if t.VertexInfo.at(vtx) == 22:
        CDauPos_i.append(t.StartX.at(vtx))
        CDauPos_j.append(t.StartY.at(vtx))
        CDauPos_k.append(t.StartZ.at(vtx))
        CDauMom_i.append(t.Px.at(vtx))
        CDauMom_j.append(t.Py.at(vtx))
        CDauMom_k.append(t.Pz.at(vtx))
        CDauMom_l.append(t.P.at(vtx))
        CDauPdg.append(t.PdgCode.at(vtx))

    CDauPos = [CDauPos_i[0],CDauPos_j[0],CDauPos_k[0]]      #Charm Decay Position

    NOP = ProngCount(CDauPdg)
    ch = ChannelDecision(CPdg, NOP)

    MultPri = Multiplicity(PVPdg, Chargeless)       #Multiplicity at Primary Vertex
    MultSec = Multiplicity(CDauPdg, Chargeless)         #Multiplicity at Charm Vertex

    CSX = Slope(CMom[0], CMom[2])           #Charm Slope in X-axis
    CSY = Slope(CMom[1], CMom[2])
    angSpc = (angNuX**2 + angNuY**2)**0.5       #Space Angle of Neutrino

    fL = FlightLength(CDauPos, CPos)*10.0    #in mm
    iP = ImpactParameterV2(CPos, CDauPos, CSX, CSY)*1e4     #in micro-m

    BjorX = Bjorken(mom4_nu, mom4_lept, mom4_nucl)
    InelY = Inelasticity(mom4_nu, mom4_lept, mom4_nucl)

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

    #if CPdg in [411, 431, 4122] and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted

    if (CPdg == 411) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (CPdg == 411):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (CPdg == 431) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (CPdg == 431):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (CPdg == 4122) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (CPdg == 4122):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (CPdg == 421) and NOP not in [0, 2, 4]:      # 6 Prong has been deleted
    #if (CPdg == 421):      # 6 Prong has been deleted
      delProng = True
    if lEnergy == 0:
      delProng == True

    if not delProng:

      h['nuE'].Fill(nuEnergy)
      h['eCorr'].Fill(nuEnergy,lEnergy)
      h['fCorr'].Fill(nuEnergy,fL)
      h['iCorr'].Fill(nuEnergy,iP)
      if NOP == 0:
        h['okCorr'].Fill(nuEnergy,oA)
      if NOP == 1:
        h['okCorr'].Fill(nuEnergy,kA)
      h['nuAngDistXF'].Fill(angNuX)
      h['nuAngDistYF'].Fill(angNuY)
      h['nuAngSpcF'].Fill(angSpc)
      h['nuAng2DF'].Fill(angNuX,angNuY)

      if nuEnergy <= 100.:
          h['nuAngDistXB'].Fill(angNuX)
          h['nuAngDistYB'].Fill(angNuY)
          h['nuAng2DB'].Fill(angNuX,angNuY)
      else:
          h['nuAngDistXA'].Fill(angNuX)
          h['nuAngDistYA'].Fill(angNuY)
          h['nuAng2DA'].Fill(angNuX,angNuY)

      CharmFraction(CPdg, CCounter)
      h['tplane'].Fill(Pos[0], Pos[1])
      h['za'].Fill(Pos[2])
      h['BjorX'].Fill(BjorX)
      h['InelY'].Fill(InelY)

      inGeo += 1.

      if CPdg == 411:
        h['dC1E'].Fill(CEnergy)
        h['dC1FL'].Fill(fL)
        h['dC1IP'].Fill(iP)
        h['dC1KA'].Fill(kA)
        h['dC1M'].Fill(MultPri)
        h['dC1M2'].Fill(MultSec)
      elif CPdg== 421:
        h['dC2E'].Fill(CEnergy)
        h['dC2FL'].Fill(fL)
        h['dC2IP'].Fill(iP)
        h['dC2OA'].Fill(oA)
        h['dC2M'].Fill(MultPri)
        h['dC2M2'].Fill(MultSec)
      elif CPdg == 431:
        h['dC3E'].Fill(CEnergy)
        h['dC3FL'].Fill(fL)
        h['dC3IP'].Fill(iP)
        h['dC3KA'].Fill(kA)
        h['dC3M'].Fill(MultPri)
        h['dC3M2'].Fill(MultSec)
      elif CPdg == 4122:
        h['dC4E'].Fill(CEnergy)
        h['dC4FL'].Fill(fL)
        h['dC4IP'].Fill(iP)
        h['dC4KA'].Fill(kA)
        h['dC4M'].Fill(MultPri)
        h['dC4M2'].Fill(MultSec)

      if False not in GS:
        if ch != 20:
          h['g-nuEs'].Fill(nuEnergy)
          h['g-eCorrs'].Fill(nuEnergy,lEnergy)
        if True in LS:
          if ch!= 20:
            h['l-nuEs'].Fill(nuEnergy)
            h['l-eCorrs'].Fill(nuEnergy,lEnergy)
            if fL < 4.:
                h['d-nuEsFL'].Fill(nuEnergy)
            if iP > 10.:
                h['d-nuEsIP'].Fill(nuEnergy)
            if (kA*1e3 > 10. and oA*1e3 > 20.):
                h['d-nuEsOKA'].Fill(nuEnergy)
          if True in DSS:
            if CPdg == 411:
              h['d-nuEs1'].Fill(nuEnergy)
              h['dC1ES'].Fill(CEnergy)
              h['dC1FLS'].Fill(fL)
              h['dC1IPS'].Fill(iP)
              h['dC1KAS'].Fill(kA)
              h['dC1MS'].Fill(MultPri)
              h['dC1M2S'].Fill(MultSec)
            elif CPdg==421 and ch!=20:
              h['d-nuEs2'].Fill(nuEnergy)
              h['dC2ES'].Fill(CEnergy)
              h['dC2FLS'].Fill(fL)
              h['dC2IPS'].Fill(iP)
              h['dC2OAS'].Fill(oA)
              h['dC2MS'].Fill(MultPri)
              h['dC2M2S'].Fill(MultSec)
            elif CPdg == 431:
              h['d-nuEs3'].Fill(nuEnergy)
              h['dC3ES'].Fill(CEnergy)
              h['dC3FLS'].Fill(fL)
              h['dC3IPS'].Fill(iP)
              h['dC3KAS'].Fill(kA)
              h['dC3MS'].Fill(MultPri)
              h['dC3M2S'].Fill(MultSec)
            elif CPdg == 4122:
              h['d-nuEs4'].Fill(nuEnergy)
              h['dC4ES'].Fill(CEnergy)
              h['dC4FLS'].Fill(fL)
              h['dC4IPS'].Fill(iP)
              h['dC4KAS'].Fill(kA)
              h['dC4MS'].Fill(MultPri)
              h['dC4M2S'].Fill(MultSec)

            if ch!=20:
              h['d-nuEs'].Fill(nuEnergy)
              h['d-eCorrs'].Fill(nuEnergy,lEnergy)
              h['d-fCorrs'].Fill(nuEnergy,fL)
              h['d-iCorrs'].Fill(nuEnergy,iP)
              if NOP == 0:
                h['d-okCorrs'].Fill(nuEnergy,oA)
              if NOP == 1:
                h['d-okCorrs'].Fill(nuEnergy,kA)
              h['d-nuAngDistXFs'].Fill(angNuX)
              h['d-nuAngDistYFs'].Fill(angNuY)
              h['d-nuAngSpcFs'].Fill(angSpc)
              h['d-nuAng2DFs'].Fill(angNuX,angNuY)

              if nuEnergy <= 100.:
                  h['d-nuAngDistXBs'].Fill(angNuX)
                  h['d-nuAngDistYBs'].Fill(angNuY)
                  h['d-nuAng2DBs'].Fill(angNuX,angNuY)
              else:         
                  h['d-nuAngDistXAs'].Fill(angNuX)
                  h['d-nuAngDistYAs'].Fill(angNuY)
                  h['d-nuAng2DAs'].Fill(angNuX,angNuY)

              CharmFraction(CPdg, CCounterS)
              h['tplaneS'].Fill(Pos[0], Pos[1])
              h['zaS'].Fill(Pos[2])
              h['BjorXs'].Fill(BjorX)
              h['InelYs'].Fill(InelY)
              #fSquark.write("%s,%s,%s,%s\n" %(event,nuEnergy, BjorX, InelY))

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

CharmSum = sum(CCounter)
C1FrProd = CCounter[0]/CharmSum
C2FrProd = CCounter[1]/CharmSum
C3FrProd = CCounter[2]/CharmSum
C4FrProd = CCounter[3]/CharmSum

h['cFracProd'].Fill(0,C1FrProd)
h['cFracProd'].Fill(1,C2FrProd)
h['cFracProd'].Fill(2,C3FrProd)
h['cFracProd'].Fill(3,C4FrProd)

C1FrSelc = CCounterS[0]/CCounter[0]
C2FrSelc = CCounterS[1]/CCounter[1]
C3FrSelc = CCounterS[2]/CCounter[2]
C4FrSelc = CCounterS[3]/CCounter[3]

h['cFracSelc'].Fill(0,C1FrSelc)
h['cFracSelc'].Fill(1,C2FrSelc)
h['cFracSelc'].Fill(2,C3FrSelc)
h['cFracSelc'].Fill(3,C4FrSelc)

print '    | Production |                            Selection '
print '    |  Fraction  |  Produced     Selected       Ratio   '
print '    |  --------  |  --------     --------      -------  '
print 'D+  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C1FrProd, CCounter[0], CCounterS[0], C1FrSelc)
print 'D0  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C2FrProd, CCounter[1], CCounterS[1], C2FrSelc)
print 'Ds+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C3FrProd, CCounter[2], CCounterS[2], C3FrSelc)
print 'Lc+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C4FrProd, CCounter[3], CCounterS[3], C4FrSelc)
print '******************************************************************** Associated Charmed Hadron Fractions'

print '********************************************************************************************************'
print 'Total #of Events | After Geometrical Selection | After Location Selection | After Decay Search Selection'
print '     %6.0f                 %6.0f                       %6.0f                     %6.0f' %(inGeo, tGS, tLS, tDSS)

print '********************************************************************************************************'
print '*                                                                                                      *'
print '********************************************************************************************************'

#fSquark.close()
makePlots(work_dir)

elikkayalib.finish()

#end of the script
