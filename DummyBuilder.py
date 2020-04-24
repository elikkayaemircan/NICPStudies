import ROOT as r
import argparse, os

def init():
  ap = argparse.ArgumentParser(
      description='Run the dummy builder')
  ap.add_argument('--work_dir', type=str, help="work space path", dest='work_dir', default=None)
  ap.add_argument('--input_path', type=str, help="input directory path", dest='input_path', default=None)
  ap.add_argument('--geo_file', type=str, help="geometry file", dest='geo_file', default=None)
  ap.add_argument('-n', type=int, help="number of ROOT files to handle", dest='n_files', default=None)
  ap.add_argument('--flavor', type=str, help="flavor name", dest='flav', default=None)
  args = ap.parse_args()
  return args

args = init() #to get the options

work_dir = args.work_dir
input_path = args.input_path
geo_file = args.geo_file
n_files = args.n_files
flav = args.flav

foldList = os.listdir(input_path)

fn = r.TFile(work_dir+'/'+flav+'.root', 'recreate')
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

Charm = [411, 421, 431, 4122]
AntiCharm = [-411, -421, -431, -4122]

if "_bar" not in flav:
    CharmedHadron = Charm
else:
    CharmedHadron = AntiCharm

if flav == "nu_e":
    Lepton = [11]
elif flav == "nu_mu":
    Lepton = [13]
elif flav == "nu_e_bar":
    Lepton = [-11]
elif flav == "nu_mu_bar":
    Lepton = [-13]

g = r.TFile(geo_file)
sGeo = g.FAIRGeom
fGeo = r.gGeoManager

for d in xrange(n_files):

  print 'Processing event file in the the folder:', d

  f = r.TFile(input_path+'/'+foldList[d]+'/ship.conical.Genie-TGeant4.root')

  try: t = f.cbmsim
  except AttributeError: 'The file in the directory '+d+' is broken!'
  else:
    nEnt = t.GetEntries()
    t.GetEntry(0)
    mcT = t.MCTrack

    for event in xrange(nEnt):

      if event%1000 == 0: print event

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

print 'Event dummy builder finished successfully!'

#end of the script
