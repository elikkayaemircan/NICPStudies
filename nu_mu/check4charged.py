import ROOT as r
import pypdt

from numpy import arctan

r.gROOT.ProcessLine('.L ../cret.C')

cret_ch = r.TChain('cret', 'cret')
cret_ch.Add('../C_nu_mu.root')

cret = r.cret(cret_ch)

nEnt = cret.fChain.GetEntries()

test = open('test.txt', 'w')

for event in xrange(nEnt):

	cret.GetEntry(event)
	for vtx in xrange(cret.VertexInfo.size()):
		if (cret.VertexInfo.at(vtx) == 1):
			p = pypdt.get(cret.PdgCode.at(vtx))
			test.write(str(p)+'\n')

#end of the script
