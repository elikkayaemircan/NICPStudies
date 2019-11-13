import ROOT as r

from numpy import arctan, sqrt

r.gROOT.ProcessLine('.L cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('C_nu_mu_bar.root')

cret = r.cret(cret_ch)

nEnt = cret.fChain.GetEntries()

c = r.TCanvas('c', 'title', 1920, 1080)
h1 = r.TH1F('bjor', 'Bjorken x', 100, 0, 1)
h2 = r.TH1F('inel', 'Inelasticity y', 100, 0, 1)
h3 = r.TH2F('tplane', 'Transverse Plane of Neutrino Target', 100, -50, 50, 100, -50, 50)
h4 = r.TH1F('z-axis', 'Z Axis of Neutrino Target', 100, -3350, -3030)
h5 = r.TH1F('energy', 'Incoming Neutrino Energy', 100, 0, 200)
h6 = r.TH1F('energy_show', 'Hadronic Shower Energy', 100, 0, 200)
h7 = r.TH1F('flength', 'Flight Length of Charmed Hadron', 100, 0., 1.)
h8 = r.TH1F('cratio', 'Charmed Hadron Production Ratio', 4, 0, 4)

for event in xrange(nEnt):

	cret.GetEntry(event)
	mom4_nu, mom4_nucl, mom4_lept, mom4_hshow = r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.)
	P_unique, P_special, Qx, Qy = 0, 0, 0, 0

	if (cret.IntInGeo.at(0)):

		for vtx in xrange(cret.VertexInfo.size()):

			if (cret.VertexInfo.at(vtx) == 0):
				mom4_nu += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
				mom4_nucl += r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2.)
				Enu = cret.Energy.at(vtx)

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
					Elept = cret.Energy.at(vtx)
				if (cret.PdgCode.at(vtx) in [-411, -421, -431, -4122]):
					X = cret.StartX.at(vtx)
					Y = cret.StartY.at(vtx)
					Z = cret.StartZ.at(vtx)
					if (cret.PdgCode.at(vtx) == -411):
						h8.Fill(0, 1)
					if (cret.PdgCode.at(vtx) == -421):
						h8.Fill(1, 1)
					if (cret.PdgCode.at(vtx) == -431):
						h8.Fill(2, 1)
					if (cret.PdgCode.at(vtx) == -4122):
						h8.Fill(3, 1)

			if (cret.VertexInfo.at(vtx) == 2):
				x = cret.StartX.at(vtx)
				y = cret.StartY.at(vtx)
				z = cret.StartZ.at(vtx)

		if( P_unique >= 1 and P_special >= 2 and Qx >= 2 and Qy >= 2):
			BjorX1 = 2*(mom4_nu*mom4_lept)/(2*(mom4_nucl*(mom4_nu-mom4_lept)))
			InelY1 = (mom4_nucl*(mom4_nu - mom4_lept))/(mom4_nucl*mom4_nu)
			h1.Fill(BjorX1)
			h2.Fill(InelY1)
			h3.Fill(X, Y)
			h4.Fill(Z)
			h5.Fill(Enu)
			h6.Fill(Enu - Elept)
			h7.Fill(sqrt((x-X)**2 + (y-Y)**2 + (z-Z)**2))

	else:
		pass

h1.Draw()
c.Print('Bjor_nu_mu_bar.pdf')
c.Update()

h2.Draw()
c.Print('Inel_nu_mu_bar.pdf')
c.Update()

h3.Draw('COLZ')
c.Print('tplane_nu_mu_bar.pdf')
c.Update()

h4.Draw()
c.Print('z_nu_mu_bar.pdf')
c.Update()

h5.Draw()
c.Print('energy_nu_mu_bar.pdf')
c.Update()

h6.Draw()
c.Print('energy_hshow_nu_mu_bar.pdf')
c.Update()

h7.Draw()
c.Print('flength_nu_mu_bar.pdf')
c.Update()

h8.GetXaxis().SetBinLabel(1, "D^{-}")
h8.GetXaxis().SetBinLabel(2, "#bar{D}^{0}")
h8.GetXaxis().SetBinLabel(3, "D_{s}^{-}")
h8.GetXaxis().SetBinLabel(4, "#Lambda_{c}^{-}")

h8.Draw()
c.Print('cratio_nu_mu_bar.pdf')
c.Update()

#end of the script
