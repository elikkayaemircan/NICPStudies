import ROOT as r
import argparse

def init():
  ap = argparse.ArgumentParser(
      description='Run the dummy builder')
  ap.add_argument('-w', '--work_dir', type=str, help="work space path", dest='work_dir', default=None)
  ap.add_argument('-n', '--numb', type=int, help="number of ROOT files to handle", dest='nof', default=None)
  args = ap.parse_args()
  return args

args = init() #to get the options

work_dir = args.work_dir
nof = args.nof

fn = r.TFile(work_dir+'/nu_mu.root', 'recreate')
tn = r.TTree('cret', 'Charm related events')

Energy = r.std.vector(float)()
P = r.std.vector(float)()
Px = r.std.vector(float)()
Py = r.std.vector(float)()
Pz = r.std.vector(float)()
PdgCode = r.std.vector(int)()
StartX = r.std.vector(float)()
StartY = r.std.vector(float)()
StartZ = r.std.vector(float)()
VertexInfo = r.std.vector(int)()
IntInGeo = r.std.vector(bool)() #Event Based Branch

tn.Branch('Energy', Energy)
tn.Branch('P', P)
tn.Branch('Px', Px)
tn.Branch('Py', Py)
tn.Branch('Pz', Pz)
tn.Branch('PdgCode', PdgCode)
tn.Branch('StartX', StartX)
tn.Branch('StartY', StartY)
tn.Branch('StartZ', StartZ)
tn.Branch('VertexInfo', VertexInfo)
tn.Branch('IntInGeo', IntInGeo)

CharmedHadron = [411, 421, 431, 4122]
Lepton = [13]

for d in xrange(nof):

  d = str(d)
  print d

  f = r.TFile(work_dir+'/nu_mu/'+d+'/ship.conical.Genie-TGeant4.root')
  g = r.TFile(work_dir+'/nu_mu/'+d+'/geofile_full.conical.Genie-TGeant4.root')

  t = f.cbmsim
  sGeo = g.FAIRGeom
  fGeo = r.gGeoManager

  nEnt = t.GetEntries()
  t.GetEntry(0)
  mcT = t.MCTrack

  for event in xrange(nEnt):

    t.GetEntry(event)
    TrackNo= 0

    Energy.clear()
    P.clear()
    Px.clear()
    Py.clear()
    Pz.clear()
    PdgCode.clear()
    StartX.clear()
    StartY.clear()
    StartZ.clear()
    VertexInfo.clear()
    IntInGeo.clear()

    for track in mcT:

      try: NuTrack
      except NameError:
        if (track.GetMotherId() == -1):
          VertexInfo.push_back(0)
          Energy.push_back(track.GetEnergy())
          P.push_back(track.GetP())
          Px.push_back(track.GetPx())
          Py.push_back(track.GetPy())
          Pz.push_back(track.GetPz())
          PdgCode.push_back(track.GetPdgCode())
          StartX.push_back(track.GetStartX())
          StartY.push_back(track.GetStartY())
          StartZ.push_back(track.GetStartZ())
          NuTrack = TrackNo
      else:
        if (track.GetMotherId() == NuTrack):
          VertexInfo.push_back(1)
          Energy.push_back(track.GetEnergy())
          P.push_back(track.GetP())
          Px.push_back(track.GetPx())
          Py.push_back(track.GetPy())
          Pz.push_back(track.GetPz())
          PdgCode.push_back(track.GetPdgCode())
          X = track.GetStartX()
          Y = track.GetStartY()
          Z = track.GetStartZ()
          StartX.push_back(X)
          StartY.push_back(Y)
          StartZ.push_back(Z)
          fGeo.SetCurrentPoint(X, Y, Z)
          fGeo.FindNode()
          if fGeo.GetCurrentVolume().GetName() == "Lead" or fGeo.GetCurrentVolume().GetName() == "Emulsion":
            IntInGeo.push_back(True)
          else:
            IntInGeo.push_back(False)
          if track.GetPdgCode() in Lepton:
            LeptonTrack = TrackNo
          if track.GetPdgCode() in CharmedHadron:
            CharmTrack = TrackNo

      try: LeptonTrack
      except NameError:
      	pass
      else:
        if (track.GetMotherId() == LeptonTrack):
          VertexInfo.push_back(21)
          Energy.push_back(track.GetEnergy())
          P.push_back(track.GetP())
          Px.push_back(track.GetPx())
          Py.push_back(track.GetPy())
          Pz.push_back(track.GetPz())
          PdgCode.push_back(track.GetPdgCode())
          StartX.push_back(track.GetStartX())
          StartY.push_back(track.GetStartY())
          StartZ.push_back(track.GetStartZ())

      try: CharmTrack
      except NameError:
      	pass
      else:
        if (track.GetMotherId() == CharmTrack):
          VertexInfo.push_back(22)
          Energy.push_back(track.GetEnergy())
          P.push_back(track.GetP())
          Px.push_back(track.GetPx())
          Py.push_back(track.GetPy())
          Pz.push_back(track.GetPz())
          PdgCode.push_back(track.GetPdgCode())
          StartX.push_back(track.GetStartX())
          StartY.push_back(track.GetStartY())
          StartZ.push_back(track.GetStartZ())

      TrackNo += 1

    del TrackNo
    del NuTrack
    del CharmTrack

    try: LeptonTrack
    except NameError: pass
    else: del LeptonTrack

    tn.Fill()

fn.Write()
fn.Close()

#end of the script
