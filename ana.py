import ROOT as r

r.gROOT.ProcessLine('.L nu_mu/cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('nu_mu/C_nu_mu.root')

cret = r.cret(cret_ch)

nEnt = cret.fChain.GetEntries()

c = r.TCanvas('c', 'title', 1920, 1080)
h1 = r.TH1F('bjor', 'Bjorken x', 100, 0, 1)
h2 = r.TH1F('inel', 'Inelasticity y', 100, 0, 1)

for event in xrange(nEnt):
	mom4_nu = r.TLorentzVector(0., 0., 0., 0.)
	mom4_nucl = r.TLorentzVector(0., 0., 0., 0.)
	mom4_lept = r.TLorentzVector(0., 0., 0., 0.)
	mom4_hshow = r.TLorentzVector(0., 0., 0., 0.)
	cret.GetEntry(event)
	for vtx in xrange(cret.Energy.size()):
		if (cret.VertexInfo.at(vtx) == 0):
			mom4_nu += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
			mom4_nucl += r.TLorentzVector(0., 0., 0., 0.938)
		if (cret.VertexInfo.at(vtx) == 1):
			if (cret.PdgCode.at(vtx) == 13):
				mom4_lept += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
			#elif (cret.PdgCode.at(vtx) != 22):
				#mom4_hshow += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))
			else:
				#print cret.PdgCode.at(vtx)
				mom4_hshow += r.TLorentzVector(cret.Px.at(vtx), cret.Py.at(vtx), cret.Pz.at(vtx), cret.Energy.at(vtx))

	BjorX1 = 2*(mom4_nu*mom4_lept)/(2*(mom4_nucl*(mom4_nu-mom4_lept)))
	#print BjorX1
	#BjorX2 = 2*(mom4_hshow*mom4_nucl)/(2*(mom4_nucl*(mom4_hshow-mom4_nucl)))
	#print BjorX2

	InelY1 = (mom4_nucl*(mom4_nu - mom4_lept))/(mom4_nucl*mom4_nu)
	#print InelY1
	#InelY2 = (mom4_nucl*(mom4_hshow - mom4_nucl))/(mom4_nucl*mom4_nu)
	#print InelY2

	h1.Fill(BjorX1)
	h2.Fill(InelY1)

h1.Draw()
c.Print('Bjor_nu_mu.pdf')
c.Update()

h2.Draw()
c.Print('Inel_nu_mu.pdf')
c.Update()

#end of the script
