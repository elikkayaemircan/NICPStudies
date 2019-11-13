import ROOT as r
from decorators import *

f = r.TFile('$EOS/events_geo/event_CharmCCDIS_Mar18_newgeo/nu_mu/ship.conical.Genie-TGeant4.root')
t = f.cbmsim

fn = r.TFile('C_nu_mu.root', 'recreate')
tn = r.TTree('cret', 'Charm related events')

Energy = r.std.vector(float)()
Px = r.std.vector(float)()
Py = r.std.vector(float)()
Pz = r.std.vector(float)()
PdgCode = r.std.vector(int)()
StartX = r.std.vector(float)()
StartY = r.std.vector(float)()
StartZ = r.std.vector(float)()
VertexInfo = r.std.vector(int)()
IntInGeo = r.std.vector(bool)()

tn.Branch('Energy', Energy)
tn.Branch('Px', Px)
tn.Branch('Py', Py)
tn.Branch('Pz', Pz)
tn.Branch('PdgCode', PdgCode)
tn.Branch('StartX', StartX)
tn.Branch('StartY', StartY)
tn.Branch('StartZ', StartZ)
tn.Branch('VertexInfo', VertexInfo)
tn.Branch('IntInGeo', IntInGeo)

nEnt = t.GetEntries()
t.GetEntry(0)
mcT = t.MCTrack

for event in xrange(nEnt):

	t.GetEntry(event)
	TrackNo= 0

	Energy.clear()
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
				Px.push_back(track.GetPx())
				Py.push_back(track.GetPy())
				Pz.push_back(track.GetPz())
				PdgCode.push_back(track.GetPdgCode())
				StartX.push_back(track.GetStartX())
				StartY.push_back(track.GetStartY())
				StartZ.push_back(track.GetStartZ())
				if (track.GetPdgCode() == 411 or track.GetPdgCode() == 421 or track.GetPdgCode() == 431 or track.GetPdgCode() == 4122):
					CharmTrack = TrackNo
					if (-45. < track.GetStartX() < 45. and -37. < track.GetStartY() < 37. and -3345. < track.GetStartZ() < -3045.):
						IntInGeo.push_back(True)
					else:
						IntInGeo.push_back(False)

		try: CharmTrack
		except NameError:
			pass
		else:
			if (track.GetMotherId() == CharmTrack):
				VertexInfo.push_back(2)
				Energy.push_back(track.GetEnergy())
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

	tn.Fill()

fn.Write()
fn.Close()

#end of the script
