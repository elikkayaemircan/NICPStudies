import ROOT as r

from numpy import arctan

r.gROOT.ProcessLine('.L cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('C_nu_mu_bar.root')

cret = r.cret(cret_ch)

nEnt = cret.fChain.GetEntries()

c = r.TCanvas('c', 'title', 1920, 1080)
h1 = r.TH1F('bjor', 'Bjorken x', 100, 0, 1)
h2 = r.TH1F('inel', 'Inelasticity y', 100, 0, 1)

for event in xrange(nEnt):

	cret.GetEntry(event)
	mom4_nu, mom4_nucl, mom4_lept, mom4_hshow = r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.)
	P_unique, P_special, Qx, Qy = 0, 0, 0, 0

	if (cret.IntInGeo.at(0)):

		for vtx in xrange(cret.VertexInfo.size()):

			if (cret.VertexInfo.at(vtx) == 0):
				mom4_nu += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
				mom4_nucl += r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2.)

			if (cret.VertexInfo.at(vtx) == 1):
				if (abs(cret.PdgCode.at(vtx)) not in [12, 22, 111, 130, 421, 2112]):
					if (cret.P.at(vtx) > 1.):
						P_unique += 1
					if (cret.P.at(vtx) > 0.01):
						P_special += 1
					if (arctan(cret.Px.at(vtx) / cret.Pz.at(vtx)) < 1.):
						Qx += 1
					if (arctan(cret.Py.at(vtx) / cret.Pz.at(vtx)) < 1.):
						Qy += 1
				if (cret.PdgCode.at(vtx) == -13):
					mom4_lept += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
				#else:
					#mom4_hshow += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))

		if( P_unique >= 1 and P_special >= 2 and Qx >= 2 and Qy >= 2):
			BjorX1 = 2*(mom4_nu*mom4_lept)/(2*(mom4_nucl*(mom4_nu-mom4_lept)))
			InelY1 = (mom4_nucl*(mom4_nu - mom4_lept))/(mom4_nucl*mom4_nu)
			h1.Fill(BjorX1)
			h2.Fill(InelY1)

	else:
		pass

h1.Draw()
c.Print('Bjor_nu_mu_bar.pdf')
c.Update()

h2.Draw()
c.Print('Inel_nu_mu_bar.pdf')
c.Update()

#end of the script
