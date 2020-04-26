import ROOT as r
import rootUtils as ut
import elikkayalib, argparse, time

from histAll import *
from physlib import *

start_time = time.time()

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

""" Some stat counters defined here. """
# With this Dictionary, I will stat the selections
CountSelection = { 'inGeo' : 0,
                   'tGS' : 0,
                   'tLS' : 0,
                   'tDSS' : 0 }
# Do not get confused here. 0th entry in the list is selected, 1th entry is the total!
CountCharmFlavor = { 'd' : [0,0],
                     'd0' : [0,0],
                     'dS' : [0,0],
                     'lambdaC' : [0,0] }

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

""" Start the event loop! """
for event in xrange(nEnt):

  t.GetEntry(event)

  if (t.IntInGeo.at(0)):

    GS, LS, DSS = [], [], []        #Selection Counter Arrays
    delProng = False        #Prong Selector Parameter Default with False

    Neutrino = {}      # Define Neutrino Dictionary
    NeutrinoDaughter = { 'Px' : (), 'Py' : (), 'Pz' : (), 'P' : (),        # Define Neutrino Daughter Dictionary which Contains Tuples
                      'PosX' : (), 'PosY' : (), 'PosZ' : (), 'Pos' : (),
                      'PDG' : () }
    Charm = {}      # Define Charm Dictionary
    CharmDaughter = { 'Px' : (), 'Py' : (), 'Pz' : (), 'P' : (),        # Define Charm Daughter Dictionary which Contains Tuples
                      'PosX' : (), 'PosY' : (), 'PosZ' : (), 'Pos' : (),
                      'PDG' : () }
    Lepton = {}       # Define Lepton Dictionary

    for vtx in xrange(t.VertexInfo.size()):

      if t.VertexInfo.at(vtx) == 0:
        Neutrino = { 'E' : t.Energy.at(vtx),
                     'Px' : t.Px.at(vtx),
                     'Py' : t.Py.at(vtx),
                     'Pz' : t.Pz.at(vtx),
                     'P' : t.P.at(vtx),
                     'Pos' : () }

      if t.VertexInfo.at(vtx) == 1:
        NeutrinoDaughter['Px'] += t.Px.at(vtx),
        NeutrinoDaughter['Py'] += t.Py.at(vtx),
        NeutrinoDaughter['Pz'] += t.Pz.at(vtx),
        NeutrinoDaughter['P'] += t.P.at(vtx),
        NeutrinoDaughter['PosX'] += t.StartX.at(vtx),
        NeutrinoDaughter['PosY'] += t.StartY.at(vtx),
        NeutrinoDaughter['PosZ'] += t.StartZ.at(vtx),
        NeutrinoDaughter['PDG'] += t.PdgCode.at(vtx),
        if NeutrinoDaughter['PDG'][-1] in CharmedHadron:
          Charm = { 'E' : t.Energy.at(vtx),
                    'Px' : t.Px.at(vtx),
                    'Py' : t.Py.at(vtx),
                    'Pz' : t.Pz.at(vtx),
                    'P' : t.P.at(vtx),
                    'Pos' : (),
                    'PDG' : NeutrinoDaughter['PDG'][-1] }
        if NeutrinoDaughter['PDG'][-1] in Lepton:
          Lepton = { 'E' : t.Energy.at(vtx),
                     'Px' : t.Px.at(vtx),
                     'Py' : t.Py.at(vtx),
                     'Pz' : t.Pz.at(vtx) }

      if t.VertexInfo.at(vtx) == 22:
        CharmDaughter['Px'] += t.Px.at(vtx),
        CharmDaughter['Py'] += t.Py.at(vtx),
        CharmDaughter['Pz'] += t.Pz.at(vtx),
        CharmDaughter['P'] += t.P.at(vtx),
        CharmDaughter['PosX'] += t.StartX.at(vtx),
        CharmDaughter['PosY'] += t.StartY.at(vtx),
        CharmDaughter['PosZ'] += t.StartZ.at(vtx),
        CharmDaughter['PDG'] += t.PdgCode.at(vtx),


    """ Here I will declare my new model of position. Neutrino and Charm Positions here refers to the point that they decay! """
    Neutrino['Pos'] += NeutrinoDaughter['PosX'][0], NeutrinoDaughter['PosY'][0], NeutrinoDaughter['PosZ'][0],        ## Anyway the neutrino decays at one of its daughters start point and Charm is one of them
    Charm['Pos'] += CharmDaughter['PosX'][0], CharmDaughter['PosY'][0], CharmDaughter['PosZ'][0],        ## Anyway the charm decays at one of its daughters start point and so on..

    """ Here I will do some physics calculations! """
    NOP = ProngCount(CharmDaughter['PDG'])
    ch = ChannelDecision(Charm['PDG'], NOP)

    MultPri = Multiplicity(NeutrinoDaughter['PDG'], Chargeless)       #Multiplicity at Primary Vertex
    MultSec = Multiplicity(CharmDaughter['PDG'], Chargeless)         #Multiplicity at Charm Vertex

    CSX = Slope(Charm['Px'], Charm['Pz'])           #Charm Slope in X-axis
    CSY = Slope(Charm['Py'], Charm['Pz'])           #Charm Slope in X-axis
    angNuX = Slope(t.Px.at(vtx), t.Pz.at(vtx))*1000     #in mrad
    angNuY = Slope(t.Py.at(vtx), t.Pz.at(vtx))*1000     #in mrad
    angSpc = (angNuX**2 + angNuY**2)**0.5       #Space Angle of Neutrino

    fL = FlightLength(Charm['Pos'], Neutrino['Pos'])*10.0    #in mm
    iP = ImpactParameterV2(Neutrino['Pos'], Charm['Pos'], CSX, CSY)*1e4     #in micro-m

    """
    # They are needed for s-quark content search
    #BjorX = Bjorken(mom4_nu, mom4_lept, mom4_nucl)
    BjorX = Bjorken( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                     r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                     mom4_nucl )
    #InelY = Inelasticity(mom4_nu, mom4_lept, mom4_nucl)
    InelY = Inelasticity( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                     r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                     mom4_nucl )
    """

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
    if NOP==1:
      for c in xrange(len(CharmDaughter['P'])):
        CDSX = Slope( CharmDaughter['Px'][c], CharmDaughter['Pz'][c] )
        CDSY = Slope( CharmDaughter['Py'][c], CharmDaughter['Pz'][c] )
        kA = KinkAngle(CSX, CSY, CDSX, CDSY)   #in rad
        oA = 2100
        if DecaySearchSelection(fL, kA*1e3, iP, oA):
          DSS.append(True)
        else: DSS.append(False)
    elif NOP==2:
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

    """ Some events include more than expected prongs. They should be removed! """
    #if Charm['PDG'] in [411, 431, 4122] and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted

    if (Charm['PDG'] == 411) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (Charm['PDG'] == 411):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (Charm['PDG'] == 431) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (Charm['PDG'] == 431):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (Charm['PDG'] == 4122) and NOP not in [1, 3]:    # 5 and 7 Prongs have been deleted
    #if (Charm['PDG'] == 4122):    # 5 and 7 Prongs have been deleted
      delProng = True
    if (Charm['PDG'] == 421) and NOP not in [0, 2, 4]:      # 6 Prong has been deleted
    #if (Charm['PDG'] == 421):      # 6 Prong has been deleted
      delProng = True
    if Lepton == {}:
      delProng = True

    if not delProng:

      # They are needed for s-quark content search
      BjorX = Bjorken( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                       r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                       r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2) )
      InelY = Inelasticity( r.TLorentzVector(Neutrino['Px'], Neutrino['Py'], Neutrino['Pz'], Neutrino['E']),
                       r.TLorentzVector(Lepton['Px'], Lepton['Py'], Lepton['Pz'], Lepton['E']),
                       r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2) )

      h['nuE'].Fill(Neutrino['E'])
      h['eCorr'].Fill(Neutrino['E'],Lepton['E'])
      h['fCorr'].Fill(Neutrino['E'],fL)
      h['iCorr'].Fill(Neutrino['E'],iP)
      if NOP == 0:
        h['okCorr'].Fill(Neutrino['E'],oA)
      if NOP == 1:
        h['okCorr'].Fill(Neutrino['E'],kA)
      h['nuAngDistXF'].Fill(angNuX)
      h['nuAngDistYF'].Fill(angNuY)
      h['nuAngSpcF'].Fill(angSpc)
      h['nuAng2DF'].Fill(angNuX,angNuY)

      if Neutrino['E'] <= 100.:
          h['nuAngDistXB'].Fill(angNuX)
          h['nuAngDistYB'].Fill(angNuY)
          h['nuAng2DB'].Fill(angNuX,angNuY)
      else:
          h['nuAngDistXA'].Fill(angNuX)
          h['nuAngDistYA'].Fill(angNuY)
          h['nuAng2DA'].Fill(angNuX,angNuY)

      h['tplane'].Fill(Neutrino['Pos'][0], Neutrino['Pos'][1])
      h['za'].Fill(Neutrino['Pos'][2])
      h['BjorX'].Fill(BjorX)
      h['InelY'].Fill(InelY)

      CountSelection['inGeo'] += 1.

      if Charm['PDG'] == 411:
        CountCharmFlavor['d'][1] += 1
        h['dC1E'].Fill(Charm['E'])
        h['dC1FL'].Fill(fL)
        h['dC1IP'].Fill(iP)
        h['dC1KA'].Fill(kA)
        h['dC1M'].Fill(MultPri)
        h['dC1M2'].Fill(MultSec)
      elif Charm['PDG']== 421:
        CountCharmFlavor['d0'][1] += 1
        h['dC2E'].Fill(Charm['E'])
        h['dC2FL'].Fill(fL)
        h['dC2IP'].Fill(iP)
        h['dC2OA'].Fill(oA)
        h['dC2M'].Fill(MultPri)
        h['dC2M2'].Fill(MultSec)
      elif Charm['PDG'] == 431:
        CountCharmFlavor['dS'][1] += 1
        h['dC3E'].Fill(Charm['E'])
        h['dC3FL'].Fill(fL)
        h['dC3IP'].Fill(iP)
        h['dC3KA'].Fill(kA)
        h['dC3M'].Fill(MultPri)
        h['dC3M2'].Fill(MultSec)
      elif Charm['PDG'] == 4122:
        CountCharmFlavor['lambdaC'][1] += 1
        h['dC4E'].Fill(Charm['E'])
        h['dC4FL'].Fill(fL)
        h['dC4IP'].Fill(iP)
        h['dC4KA'].Fill(kA)
        h['dC4M'].Fill(MultPri)
        h['dC4M2'].Fill(MultSec)

      if False not in GS:
        if ch != 20:
          h['g-nuEs'].Fill(Neutrino['E'])
          h['g-eCorrs'].Fill(Neutrino['E'],Lepton['E'])
        if True in LS:
          if ch!= 20:
            h['l-nuEs'].Fill(Neutrino['E'])
            h['l-eCorrs'].Fill(Neutrino['E'],Lepton['E'])
            if fL < 4.:
                h['d-nuEsFL'].Fill(Neutrino['E'])
            if iP > 10.:
                h['d-nuEsIP'].Fill(Neutrino['E'])
            if (kA*1e3 > 10. and oA*1e3 > 20.):
                h['d-nuEsOKA'].Fill(Neutrino['E'])
          if True in DSS:
            if Charm['PDG'] == 411:
              CountCharmFlavor['d'][0] += 1
              h['d-nuEs1'].Fill(Neutrino['E'])
              h['dC1ES'].Fill(Charm['E'])
              h['dC1FLS'].Fill(fL)
              h['dC1IPS'].Fill(iP)
              h['dC1KAS'].Fill(kA)
              h['dC1MS'].Fill(MultPri)
              h['dC1M2S'].Fill(MultSec)
            elif Charm['PDG']==421 and ch!=20:
              CountCharmFlavor['d0'][0] += 1
              h['d-nuEs2'].Fill(Neutrino['E'])
              h['dC2ES'].Fill(Charm['E'])
              h['dC2FLS'].Fill(fL)
              h['dC2IPS'].Fill(iP)
              h['dC2OAS'].Fill(oA)
              h['dC2MS'].Fill(MultPri)
              h['dC2M2S'].Fill(MultSec)
            elif Charm['PDG'] == 431:
              CountCharmFlavor['dS'][0] += 1
              h['d-nuEs3'].Fill(Neutrino['E'])
              h['dC3ES'].Fill(Charm['E'])
              h['dC3FLS'].Fill(fL)
              h['dC3IPS'].Fill(iP)
              h['dC3KAS'].Fill(kA)
              h['dC3MS'].Fill(MultPri)
              h['dC3M2S'].Fill(MultSec)
            elif Charm['PDG'] == 4122:
              CountCharmFlavor['lambdaC'][0] += 1
              h['d-nuEs4'].Fill(Neutrino['E'])
              h['dC4ES'].Fill(Charm['E'])
              h['dC4FLS'].Fill(fL)
              h['dC4IPS'].Fill(iP)
              h['dC4KAS'].Fill(kA)
              h['dC4MS'].Fill(MultPri)
              h['dC4M2S'].Fill(MultSec)

            if ch!=20:
              h['d-nuEs'].Fill(Neutrino['E'])
              h['d-eCorrs'].Fill(Neutrino['E'],Lepton['E'])
              h['d-fCorrs'].Fill(Neutrino['E'],fL)
              h['d-iCorrs'].Fill(Neutrino['E'],iP)
              if NOP == 0:
                h['d-okCorrs'].Fill(Neutrino['E'],oA)
              if NOP == 1:
                h['d-okCorrs'].Fill(Neutrino['E'],kA)
              h['d-nuAngDistXFs'].Fill(angNuX)
              h['d-nuAngDistYFs'].Fill(angNuY)
              h['d-nuAngSpcFs'].Fill(angSpc)
              h['d-nuAng2DFs'].Fill(angNuX,angNuY)

              if Neutrino['E'] <= 100.:
                  h['d-nuAngDistXBs'].Fill(angNuX)
                  h['d-nuAngDistYBs'].Fill(angNuY)
                  h['d-nuAng2DBs'].Fill(angNuX,angNuY)
              else:
                  h['d-nuAngDistXAs'].Fill(angNuX)
                  h['d-nuAngDistYAs'].Fill(angNuY)
                  h['d-nuAng2DAs'].Fill(angNuX,angNuY)

              h['tplaneS'].Fill(NeutrinoDaughter['PosX'][0], NeutrinoDaughter['PosY'][0])
              h['zaS'].Fill(NeutrinoDaughter['PosZ'][0])
              h['BjorXs'].Fill(BjorX)
              h['InelYs'].Fill(InelY)
              #fSquark.write("%s,%s,%s,%s\n" %(event,Neutrino['E'], BjorX, InelY))

      if ch == 10:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P0g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P0l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P0d.append(True)
            else: C1P0d.append(False)
          else: C1P0l.append(False), C1P0d.append(False)
        else: C1P0g.append(False), C1P0l.append(False), C1P0d.append(False)

      if ch == 20:
        if False not in GS:
          CountSelection['tGS'] += 0.
          C2P0g.append(False)
          if True in LS:
            CountSelection['tLS'] += 0.
            C2P0l.append(False)
            if True in DSS:
              CountSelection['tDSS'] += 0.
              C2P0d.append(False)
            else: C2P0d.append(False)
          else: C2P0l.append(False), C2P0d.append(False)
        else: C2P0g.append(False), C2P0l.append(False), C2P0d.append(False)

      if ch == 30:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P0g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P0l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P0d.append(True)
            else: C3P0d.append(False)
          else: C3P0l.append(False), C3P0d.append(False)
        else: C3P0g.append(False), C3P0l.append(False), C3P0d.append(False)

      if ch == 40:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P0g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P0l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P0d.append(True)
            else: C4P0d.append(False)
          else: C4P0l.append(False), C4P0d.append(False)
        else: C4P0g.append(False), C4P0l.append(False), C4P0d.append(False)

      if ch == 11:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P1g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P1l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P1d.append(True)
            else: C1P1d.append(False)
          else: C1P1l.append(False), C1P1d.append(False)
        else: C1P1g.append(False), C1P1l.append(False), C1P1d.append(False)

      if ch == 21:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P1g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P1l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P1d.append(True)
            else: C2P1d.append(False)
          else: C2P1l.append(False), C2P1d.append(False)
        else: C2P1g.append(False), C2P1l.append(False), C2P1d.append(False)

      if ch == 31:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P1g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P1l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P1d.append(True)
            else: C3P1d.append(False)
          else: C3P1l.append(False), C3P1d.append(False)
        else: C3P1g.append(False), C3P1l.append(False), C3P1d.append(False)

      if ch == 41:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P1g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P1l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P1d.append(True)
            else: C4P1d.append(False)
          else: C4P1l.append(False), C4P1d.append(False)
        else: C4P1g.append(False), C4P1l.append(False), C4P1d.append(False)

      if ch == 12:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P2g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P2l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P2d.append(True)
            else: C1P2d.append(False)
          else: C1P2l.append(False), C1P2d.append(False)
        else: C1P2g.append(False), C1P2l.append(False), C1P2d.append(False)

      if ch == 22:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P2g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P2l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P2d.append(True)
            else: C2P2d.append(False)
          else: C2P2l.append(False), C2P2d.append(False)
        else: C2P2g.append(False), C2P2l.append(False), C2P2d.append(False)

      if ch == 32:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P2g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P2l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P2d.append(True)
            else: C3P2d.append(False)
          else: C3P2l.append(False), C3P2d.append(False)
        else: C3P2g.append(False), C3P2l.append(False), C3P2d.append(False)

      if ch == 42:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P2g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P2l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P2d.append(True)
            else: C4P2d.append(False)
          else: C4P2l.append(False), C4P2d.append(False)
        else: C4P2g.append(False), C4P2l.append(False), C4P2d.append(False)

      if ch == 13:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P3g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P3l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P3d.append(True)
            else: C1P3d.append(False)
          else: C1P3l.append(False), C1P3d.append(False)
        else: C1P3g.append(False), C1P3l.append(False), C1P3d.append(False)

      if ch == 23:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P3g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P3l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P3d.append(True)
            else: C2P3d.append(False)
          else: C2P3l.append(False), C2P3d.append(False)
        else: C2P3g.append(False), C2P3l.append(False), C2P3d.append(False)

      if ch == 33:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P3g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P3l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P3d.append(True)
            else: C3P3d.append(False)
          else: C3P3l.append(False), C3P3d.append(False)
        else: C3P3g.append(False), C3P3l.append(False), C3P3d.append(False)

      if ch == 43:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P3g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P3l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P3d.append(True)
            else: C4P3d.append(False)
          else: C4P3l.append(False), C4P3d.append(False)
        else: C4P3g.append(False), C4P3l.append(False), C4P3d.append(False)

      if ch == 14:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P4g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P4l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P4d.append(True)
            else: C1P4d.append(False)
          else: C1P4l.append(False), C1P4d.append(False)
        else: C1P4g.append(False), C1P4l.append(False), C1P4d.append(False)

      if ch == 24:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P4g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P4l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P4d.append(True)
            else: C2P4d.append(False)
          else: C2P4l.append(False), C2P4d.append(False)
        else: C2P4g.append(False), C2P4l.append(False), C2P4d.append(False)

      if ch == 34:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P4g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P4l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P4d.append(True)
            else: C3P4d.append(False)
          else: C3P4l.append(False), C3P4d.append(False)
        else: C3P4g.append(False), C3P4l.append(False), C3P4d.append(False)

      if ch == 44:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P4g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P4l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P4d.append(True)
            else: C4P4d.append(False)
          else: C4P4l.append(False), C4P4d.append(False)
        else: C4P4g.append(False), C4P4l.append(False), C4P4d.append(False)

      if ch == 15:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P5g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P5l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P5d.append(True)
            else: C1P5d.append(False)
          else: C1P5l.append(False), C1P5d.append(False)
        else: C1P5g.append(False), C1P5l.append(False), C1P5d.append(False)

      if ch == 25:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P5g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P5l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P5d.append(True)
            else: C2P5d.append(False)
          else: C2P5l.append(False), C2P5d.append(False)
        else: C2P5g.append(False), C2P5l.append(False), C2P5d.append(False)

      if ch == 35:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P5g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P5l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P5d.append(True)
            else: C3P5d.append(False)
          else: C3P5l.append(False), C3P5d.append(False)
        else: C3P5g.append(False), C3P5l.append(False), C3P5d.append(False)

      if ch == 45:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P5g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P5l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P5d.append(True)
            else: C4P5d.append(False)
          else: C4P5l.append(False), C4P5d.append(False)
        else: C4P5g.append(False), C4P5l.append(False), C4P5d.append(False)

      if ch == 16:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P6g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P6l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P6d.append(True)
            else: C1P6d.append(False)
          else: C1P6d.append(False), C1P6d.append(False)
        else: C1P6d.append(False), C1P6d.append(False), C1P6d.append(False)

      if ch == 26:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P6g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P6l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P6d.append(True)
            else: C2P6d.append(False)
          else: C2P6d.append(False), C2P6d.append(False)
        else: C2P6d.append(False), C2P6d.append(False), C2P6d.append(False)

      if ch == 36:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P6g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P6l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P6d.append(True)
            else: C3P6d.append(False)
          else: C3P6d.append(False), C3P6d.append(False)
        else: C3P6d.append(False), C3P6d.append(False), C3P6d.append(False)

      if ch == 46:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P6g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P6l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P6d.append(True)
            else: C4P6d.append(False)
          else: C4P6d.append(False), C4P6d.append(False)
        else: C4P6d.append(False), C4P6d.append(False), C4P6d.append(False)

      if ch == 17:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P7g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P7l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P7d.append(True)
            else: C1P7d.append(False)
          else: C1P7l.append(False), C1P7d.append(False)
        else: C1P7g.append(False), C1P7l.append(False), C1P7d.append(False)

      if ch == 27:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P7g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P7l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P7d.append(True)
            else: C2P7d.append(False)
          else: C2P7l.append(False), C2P7d.append(False)
        else: C2P7g.append(False), C2P7l.append(False), C2P7d.append(False)

      if ch == 37:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P7g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P7l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P7d.append(True)
            else: C3P7d.append(False)
          else: C3P7l.append(False), C3P7d.append(False)
        else: C3P7g.append(False), C3P7l.append(False), C3P7d.append(False)

      if ch == 47:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P7g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P7l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P7d.append(True)
            else: C4P7d.append(False)
          else: C4P7l.append(False), C4P7d.append(False)
        else: C4P7g.append(False), C4P7l.append(False), C4P7d.append(False)

      if ch == 18:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P8g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P8l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P8d.append(True)
            else: C1P8d.append(False)
          else: C1P8l.append(False), C1P8d.append(False)
        else: C1P8g.append(False), C1P8l.append(False), C1P8d.append(False)

      if ch == 28:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P8g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P8l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P8d.append(True)
            else: C2P8d.append(False)
          else: C2P8l.append(False), C2P8d.append(False)
        else: C2P8g.append(False), C2P8l.append(False), C2P8d.append(False)

      if ch == 38:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P8g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P8l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P8d.append(True)
            else: C3P8d.append(False)
          else: C3P8l.append(False), C3P8d.append(False)
        else: C3P8g.append(False), C3P8l.append(False), C3P8d.append(False)

      if ch == 48:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P8g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P8l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C4P8d.append(True)
            else: C4P8d.append(False)
          else: C4P8l.append(False), C4P8d.append(False)
        else: C4P8g.append(False), C4P8l.append(False), C4P8d.append(False)

      if ch == 19:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C1P9g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C1P9l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C1P9d.append(True)
            else: C1P9d.append(False)
          else: C1P9l.append(False), C1P9d.append(False)
        else: C1P9g.append(False), C1P9l.append(False), C1P9d.append(False)

      if ch == 29:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C2P9g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C2P9l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C2P9d.append(True)
            else: C2P9d.append(False)
          else: C2P9l.append(False), C2P9d.append(False)
        else: C2P9g.append(False), C2P9l.append(False), C2P9d.append(False)

      if ch == 39:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C3P9g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C3P9l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
              C3P9d.append(True)
            else: C3P9d.append(False)
          else: C3P9l.append(False), C3P9d.append(False)
        else: C3P9g.append(False), C3P9l.append(False), C3P9d.append(False)

      if ch == 49:
        if False not in GS:
          CountSelection['tGS'] += 1.
          C4P9g.append(True)
          if True in LS:
            CountSelection['tLS'] += 1.
            C4P9l.append(True)
            if True in DSS:
              CountSelection['tDSS'] += 1.
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

print '********************************************************************* Geometry Selection Success %.5f' %(CountSelection['tGS']/CountSelection['inGeo'])

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

print '********************************************************************* Location Selection Success %.5f' %(CountSelection['tLS']/CountSelection['inGeo'])

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

print '***************************************************************** Decay Search Selection Success %.5f' %(CountSelection['tDSS']/CountSelection['inGeo'])

print '********************************************************************************************************'

CharmSum = CountCharmFlavor['d'][1] + \
           CountCharmFlavor['d0'][1] + \
           CountCharmFlavor['dS'][1] + \
           CountCharmFlavor['lambdaC'][1]
C1FrProd = CountCharmFlavor['d'][1]/CharmSum
C2FrProd = CountCharmFlavor['d0'][1]/CharmSum
C3FrProd = CountCharmFlavor['dS'][1]/CharmSum
C4FrProd = CountCharmFlavor['lambdaC'][1]/CharmSum

h['cFracProd'].Fill(0,C1FrProd)
h['cFracProd'].Fill(1,C2FrProd)
h['cFracProd'].Fill(2,C3FrProd)
h['cFracProd'].Fill(3,C4FrProd)

C1FrSelc = CountCharmFlavor['d'][0]/CountCharmFlavor['d'][1]
C2FrSelc = CountCharmFlavor['d0'][0]/CountCharmFlavor['d0'][1]
C3FrSelc = CountCharmFlavor['dS'][0]/CountCharmFlavor['dS'][1]
C4FrSelc = CountCharmFlavor['lambdaC'][0]/CountCharmFlavor['lambdaC'][1]

h['cFracSelc'].Fill(0,C1FrSelc)
h['cFracSelc'].Fill(1,C2FrSelc)
h['cFracSelc'].Fill(2,C3FrSelc)
h['cFracSelc'].Fill(3,C4FrSelc)

print '    | Production |                            Selection '
print '    |  Fraction  |  Produced     Selected       Ratio   '
print '    |  --------  |  --------     --------      -------  '
print 'D+  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C1FrProd, CountCharmFlavor['d'][1], CountCharmFlavor['d'][0], C1FrSelc)
print 'D0  |   %.4f   |   %6.0f       %6.0f        %.4f' %(C2FrProd, CountCharmFlavor['d0'][1], CountCharmFlavor['d0'][0], C2FrSelc)
print 'Ds+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C3FrProd, CountCharmFlavor['dS'][1], CountCharmFlavor['dS'][0], C3FrSelc)
print 'Lc+ |   %.4f   |   %6.0f       %6.0f        %.4f' %(C4FrProd, CountCharmFlavor['lambdaC'][1], CountCharmFlavor['lambdaC'][0], C4FrSelc)
print '******************************************************************** Associated Charmed Hadron Fractions'

print '********************************************************************************************************'
print 'Total #of Events | After Geometrical Selection | After Location Selection | After Decay Search Selection'
print '     %6.0f                 %6.0f                       %6.0f                     %6.0f' %(CountSelection['inGeo'], CountSelection['tGS'], CountSelection['tLS'], CountSelection['tDSS'])

print '********************************************************************************************************'
print '*                                                                                                      *'
print '********************************************************************************************************'

#fSquark.close()
#makePlots(work_dir)

elikkayalib.finish()


print("--- %s seconds ---" % (time.time() - start_time))

#end of the script
