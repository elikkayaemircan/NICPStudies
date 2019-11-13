import ROOT as r

from numpy import arctan
from array import array

r.gROOT.ProcessLine('.L cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('C_nu_mu_bar.root')

cret = r.cret(cret_ch)

nEnt = cret.fChain.GetEntries()

c = r.TCanvas('c', 'title', 1920, 1080)

bjor_edges = [0., 5e-3, 3.8e-2, 7e-2, 0.113, 0.18, 0.6, 1.]
#bjor_edges = [0., 5e-3, 5e-2, 0.1, 0.16, 0.26, 0.65, 1.]
h_bjor = r.TH1D('htemp_bjor', 'Bjorken x', 7, array('d', bjor_edges))

inel_edges = [0., 0.55, 0.77, 1.]
#inel_edges = [0., 0.53, 0.75, 1.]
h_inel = r.TH1D('htemp_inel', 'Inelasticity y', 3, array('d', inel_edges))

ener_edges = [10., 34., 58., 140.]
#ener_edges = [10., 37.5, 65., 150.]
h_ener = r.TH1D('htemp_ener', 'Energy', 3, array('d', ener_edges))

bjor_txt = open('bjor_nu_mu_bar.txt', 'w')
inel_txt = open('inel_nu_mu_bar.txt', 'w')
ener_txt = open('ener_nu_mu_bar.txt', 'w')

for event in xrange(nEnt):

	cret.GetEntry(event)
	mom4_nu, mom4_nucl, mom4_lept, mom4_hshow = r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.), r.TLorentzVector(0., 0., 0., 0.)
	P_unique, P_special, Qx, Qy = 0, 0, 0, 0

	if (cret.IntInGeo.at(0)):

		for vtx in xrange(cret.VertexInfo.size()):

			if (cret.VertexInfo.at(vtx) == 0):
				mom4_nu += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
				mom4_nucl += r.TLorentzVector(0., 0., 0., (0.9383+0.9396)/2)
				Energy = cret.Energy.at(vtx)

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
			h_bjor.Fill(BjorX1)
			bjor_txt.write(str(BjorX1)+'		'+str(event)+'\n')
			InelY1 = (mom4_nucl*(mom4_nu - mom4_lept))/(mom4_nucl*mom4_nu)
			h_inel.Fill(InelY1)
			inel_txt.write(str(InelY1)+'		'+str(event)+'\n')
			h_ener.Fill(Energy)
			ener_txt.write(str(Energy)+'		'+str(event)+'\n')

	else:
		pass

h_bjor.Draw()
c.Print('bjor_binning_nu_mu_bar.pdf')
c.Update()

h_inel.Draw()
c.Print('inel_binning_nu_mu_bar.pdf')
c.Update()

h_ener.Draw()
c.Print('ener_binning_nu_mu_bar.pdf')
c.Update()

bjor_txt.close()
inel_txt.close()
ener_txt.close()

#end of the script
