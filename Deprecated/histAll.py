import rootUtils as ut
import ROOT as r

h = {}

ut.bookHist(h, 'nuE',       'Incoming Neutrino Beam Energy #nu_{#mu}',            60, 0, 300)
ut.bookHist(h, 'g-nuEs',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Geometric Selection',               60, 0, 300)
ut.bookHist(h, 'l-nuEs',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Location Selection',                60, 0, 300)
ut.bookHist(h, 'd-nuEs',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Decay Search Selection',            60, 0, 300)

ut.bookHist(h, 'd-nuEsFL',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Flight Length Cut',               60, 0, 300)
ut.bookHist(h, 'd-nuEsIP',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Impact Parameter Cut',            60, 0, 300)
ut.bookHist(h, 'd-nuEsOKA',     'Incoming Neutrino Energy Spectrum #nu_{#mu}: Opening-Kink Angle Cut',          60, 0, 300)

ut.bookHist(h, 'd-nuEs1',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Charmed Hadron Flavor D{+}',               60, 0, 300)
ut.bookHist(h, 'd-nuEs2',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Charmed Hadron Flavor D{0}',               60, 0, 300)
ut.bookHist(h, 'd-nuEs3',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Charmed Hadron Flavor D_{s}^{0}',               60, 0, 300)
ut.bookHist(h, 'd-nuEs4',      'Incoming Neutrino Energy Spectrum #nu_{#mu}: Charmed Hadron Flavor L_{c}^{+}',               60, 0, 300)

ut.bookHist(h, 'g-nuEff',      'Efficiency Plot #nu_{#mu}: Geometric Selection',               60, 0, 300)
ut.bookHist(h, 'l-nuEff',      'Efficiency Plot #nu_{#mu}: Location Selection',                60, 0, 300)
ut.bookHist(h, 'd-nuEff',      'Efficiency Plot #nu_{#mu}: Decay Search Selection',            60, 0, 300)

ut.bookHist(h, 'd-nuEffFL',      'Efficiency Plot #nu_{#mu}: Flight Length Cut',            60, 0, 300)
ut.bookHist(h, 'd-nuEffIP',      'Efficiency Plot #nu_{#mu}: Impact Parameter Cut',         60, 0, 300)
ut.bookHist(h, 'd-nuEffOKA',     'Efficiency Plot #nu_{#mu}: Opening-Kink Angle Cut',       60, 0, 300)

ut.bookHist(h, 'd-nuEff1',      'Efficiency Plot #nu_{#mu}: Charmed Hadron D^{+}',            60, 0, 300)
ut.bookHist(h, 'd-nuEff2',      'Efficiency Plot #nu_{#mu}: Charmed Hadron D^{0}',            60, 0, 300)
ut.bookHist(h, 'd-nuEff3',      'Efficiency Plot #nu_{#mu}: Charmed Hadron D_{s}^{+}',            60, 0, 300)
ut.bookHist(h, 'd-nuEff4',      'Efficiency Plot #nu_{#mu}: Charmed Hadron L_{c}^{+}',            60, 0, 300)

ut.bookHist(h, 'eCorr',           'Correlation Between #mu and #nu_{#mu} Energies',                                                     150, 0, 300, 50, 0, 100)
ut.bookHist(h, 'g-eCorrs',        'Correlation Between #mu and #nu_{#mu} Energies: Geometric Selection',                                150, 0, 300, 50, 0, 100)
ut.bookHist(h, 'l-eCorrs',        'Correlation Between #mu and #nu_{#mu} Energies: Location Selection',                                 150, 0, 300, 50, 0, 100)
ut.bookHist(h, 'd-eCorrs',        'Correlation Between #mu and #nu_{#mu} Energies: Decay Search Selection',                             150, 0, 300, 50, 0, 100)

ut.bookHist(h, 'fCorr',           'Correlation Between Charmed Hadron FL and #nu_{#mu} Energy',                                         150, 0, 300, 50, 0, 10)
ut.bookHist(h, 'g-fCorrs',        'Correlation Between Charmed Hadron FL and #nu_{#mu} Energy: Geometric Selection',                    150, 0, 300, 50, 0, 10)
ut.bookHist(h, 'l-fCorrs',        'Correlation Between Charmed Hadron FL and #nu_{#mu} Energy: Location Selection',                     150, 0, 300, 50, 0, 10)
ut.bookHist(h, 'd-fCorrs',        'Correlation Between Charmed Hadron FL and #nu_{#mu} Energy: Decay Search Selection',                 150, 0, 300, 50, 0, 10)

ut.bookHist(h, 'iCorr',           'Correlation Between Charmed Hadron IP and #nu_{#mu} Energy',                                         150, 0, 300, 50, 0, 500)
ut.bookHist(h, 'g-iCorrs',        'Correlation Between Charmed Hadron IP and #nu_{#mu} Energy: Geometric Selection',                    150, 0, 300, 50, 0, 500)
ut.bookHist(h, 'l-iCorrs',        'Correlation Between Charmed Hadron IP and #nu_{#mu} Energy: Location Selection',                     150, 0, 300, 50, 0, 500)
ut.bookHist(h, 'd-iCorrs',        'Correlation Between Charmed Hadron IP and #nu_{#mu} Energy: Decay Search Selection',                 150, 0, 300, 50, 0, 500)

ut.bookHist(h, 'okCorr',           'Correlation Between Charmed Hadron OKAng and #nu_{#mu} Energy',                                     150, 0, 300, 50, 0, 1)
ut.bookHist(h, 'g-okCorrs',        'Correlation Between Charmed Hadron OKAng and #nu_{#mu} Energy: Geometric Selection',                150, 0, 300, 50, 0, 1)
ut.bookHist(h, 'l-okCorrs',        'Correlation Between Charmed Hadron OKAng and #nu_{#mu} Energy: Location Selection',                 150, 0, 300, 50, 0, 1)
ut.bookHist(h, 'd-okCorrs',        'Correlation Between Charmed Hadron OKAng and #nu_{#mu} Energy: Decay Search Selection',             150, 0, 300, 50, 0, 1)

ut.bookHist(h, 'nuAngDistXB',     'Angular Distribution: Below 100GeV in X-axis',                  240, -12, 12)
ut.bookHist(h, 'nuAngDistYB',     'Angular Distribution: Below 100GeV in Y-axis',                  240, -12, 12)
ut.bookHist(h, 'd-nuAngDistXBs',    'Angular Distribution: Below 100GeV in X-axis (Selected)',     240, -12, 12)
ut.bookHist(h, 'd-nuAngDistYBs',    'Angular Distribution: Below 100GeV in Y-axis (Selected)',     240, -12, 12)

ut.bookHist(h, 'nuAngDistXA',     'Angular Distribution: Above 100GeV in X-axis',                  240, -12, 12)
ut.bookHist(h, 'nuAngDistYA',     'Angular Distribution: Above 100GeV in Y-axis',                  240, -12, 12)
ut.bookHist(h, 'd-nuAngDistXAs',    'Angular Distribution: Above 100GeV in X-axis (Selected)',     240, -12, 12)
ut.bookHist(h, 'd-nuAngDistYAs',    'Angular Distribution: Above 100GeV in Y-axis (Selected)',     240, -12, 12)

ut.bookHist(h, 'nuAngDistXF',     'Angular Distribution: Full Spectrum in X-axis',                 240, -12, 12)
ut.bookHist(h, 'nuAngDistYF',     'Angular Distribution: Full Spectrum in Y-axis',                 240, -12, 12)
ut.bookHist(h, 'd-nuAngDistXFs',    'Angular Distribution: Full Spectrum in X-axis (Selected)',    240, -12, 12)
ut.bookHist(h, 'd-nuAngDistYFs',    'Angular Distribution: Full Spectrum in Y-axis (Selected)',    240, -12, 12)

ut.bookHist(h, 'nuAng2DB',     'Angular Distribution: Below 100 GeV in X-Y',      240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'nuAng2DA',     'Angular Distribution: Above 100 GeV in X-Y',      240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'nuAng2DF',     'Angular Distribution: Full Spectrum in X-Y',      240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'd-nuAng2DBs',     'Angular Distribution: Below 100GeV in X-Y (Selected)',      240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'd-nuAng2DAs',     'Angular Distribution: Above 100GeV in X-Y (Selected)',      240, -12, 12, 240, -12, 12)
ut.bookHist(h, 'd-nuAng2DFs',     'Angular Distribution: Full Spectrum in X-Y (Selected)',     240, -12, 12, 240, -12, 12)

ut.bookHist(h, 'nuAngSpcF',        'Space Angle of Neutrinos',                 150, 0, 15)
ut.bookHist(h, 'd-nuAngSpcFs',     'Space Angle of Neutrinos (Selected)',      150, 0, 15)

ut.bookHist(h, 'cFracProd',  'Charmed Hadron Production Fractions',            4, 0, 4)
ut.bookHist(h, 'cFracSelc',  'Charmed Hadron Interactions Selection Ratios',            4, 0, 4)

####

ut.bookHist(h, 'BjorX',     'Bjorken X Distribution',                   100, 0, 1)
ut.bookHist(h, 'BjorXs',    'Bjorken X Distribution (Selected)',        100, 0, 1)
ut.bookHist(h, 'InelY',     'Inelasticity Y Distribution',              100, 0, 1)
ut.bookHist(h, 'InelYs',    'Inelasticity Y Distribution (Selected)',   100, 0, 1)

ut.bookHist(h, 'tplane',    'Neutrino Interactions at Transverse Plane',                100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'tplaneS',   'Neutrino Interactions at Transverse Plane (Selected)',     100, -50, 50, 100, -50, 50)
ut.bookHist(h, 'za',    'Interactions at z-axis',               400, -3300, -2900)
ut.bookHist(h, 'zaS',   'Interactions at z-axis (Selected)',    400, -3300, -2900)

ut.bookHist(h, 'dC1E',      'Charmed Hadron Energy Spectrum D+',                40, 0, 100)
ut.bookHist(h, 'dC1ES',     'Charmed Hadron Energy Spectrum D+ (Selected)',     40, 0, 100)
ut.bookHist(h, 'dC2E',      'Charmed Hadron Energy Spectrum D0',                40, 0, 100)
ut.bookHist(h, 'dC2ES',     'Charmed Hadron Energy Spectrum D0 (Selected)',     40, 0, 100)
ut.bookHist(h, 'dC3E',      'Charmed Hadron Energy Spectrum Ds+',               40, 0, 100)
ut.bookHist(h, 'dC3ES',     'Charmed Hadron Energy Spectrum Ds+ (Selected)',    40, 0, 100)
ut.bookHist(h, 'dC4E',      'Charmed Hadron Energy Spectrum Lc+',               40, 0, 100)
ut.bookHist(h, 'dC4ES',     'Charmed Hadron Energy Spectrum Lc+ (Selected)',    40, 0, 100)

ut.bookHist(h, 'dC1FL',     'Charmed Hadron Flight Length D+',                  50, 0, 10)
ut.bookHist(h, 'dC1FLS',    'Charmed Hadron Flight Length D+ (Selected)',       50, 0, 10)
ut.bookHist(h, 'dC2FL',     'Charmed Hadron Flight Length D0',                  50, 0, 10)
ut.bookHist(h, 'dC2FLS',    'Charmed Hadron Flight Length D0 (Selected)',       50, 0, 10)
ut.bookHist(h, 'dC3FL',     'Charmed Hadron Flight Length Ds+',                 50, 0, 10)
ut.bookHist(h, 'dC3FLS',    'Charmed Hadron Flight Length Ds+ (Selected)',      50, 0, 10)
ut.bookHist(h, 'dC4FL',     'Charmed Hadron Flight Length Lc+',                 50, 0, 10)
ut.bookHist(h, 'dC4FLS',    'Charmed Hadron Flight Length Lc+ (Selected)',      50, 0, 10)

ut.bookHist(h, 'dC1IP',     'Charmed Hadron Impact Parameter D+',                  100, 0, 500)
ut.bookHist(h, 'dC1IPS',    'Charmed Hadron Impact Parameter D+ (Selected)',       100, 0, 500)
ut.bookHist(h, 'dC2IP',     'Charmed Hadron Impact Parameter D0',                  100, 0, 500)
ut.bookHist(h, 'dC2IPS',    'Charmed Hadron Impact Parameter D0 (Selected)',       100, 0, 500)
ut.bookHist(h, 'dC3IP',     'Charmed Hadron Impact Parameter Ds+',                 100, 0, 500)
ut.bookHist(h, 'dC3IPS',    'Charmed Hadron Impact Parameter Ds+ (Selected)',      100, 0, 500)
ut.bookHist(h, 'dC4IP',     'Charmed Hadron Impact Parameter Lc+',                 100, 0, 500)
ut.bookHist(h, 'dC4IPS',    'Charmed Hadron Impact Parameter Lc+ (Selected)',      100, 0, 500)

ut.bookHist(h, 'dC1KA',     'Kink Angle at Charm Vertex D+',                    50, 0, 1)
ut.bookHist(h, 'dC1KAS',    'Kink Angle at Charm Vertex D+ (Selected)',         50, 0, 1)
ut.bookHist(h, 'dC3KA',     'Kink Angle at Charm Vertex Ds+',                   50, 0, 1)
ut.bookHist(h, 'dC3KAS',    'Kink Angle at Charm Vertex Ds+ (Selected)',        50, 0, 1)
ut.bookHist(h, 'dC4KA',     'Kink Angle at Charm Vertex Lc+',                   50, 0, 1)
ut.bookHist(h, 'dC4KAS',    'Kink Angle at Charm Vertex Lc+ (Selected)',        50, 0, 1)

ut.bookHist(h, 'dC2OA',     'Opening Angle at Charm Vertex D0',                 50, 0, 1)
ut.bookHist(h, 'dC2OAS',    'Opening Angle at Charm Vertex D0 (Selected)',      50, 0, 1)

ut.bookHist(h, 'dC1M',      'Charmed Hadron Multiplicity at Primary Vertex D+',                 15, 0, 15)
ut.bookHist(h, 'dC1MS',     'Charmed Hadron Multiplicity at Primary Vertex D+ (Selected)',      15, 0, 15)
ut.bookHist(h, 'dC2M',      'Charmed Hadron Multiplicity at Primary Vertex D0',                 15, 0, 15)
ut.bookHist(h, 'dC2MS',     'Charmed Hadron Multiplicity at Primary Vertex D0 (Selected)',      15, 0, 15)
ut.bookHist(h, 'dC3M',      'Charmed Hadron Multiplicity at Primary Vertex Ds+',                15, 0, 15)
ut.bookHist(h, 'dC3MS',     'Charmed Hadron Multiplicity at Primary Vertex Ds+ (Selected)',     15, 0, 15)
ut.bookHist(h, 'dC4M',      'Charmed Hadron Multiplicity at Primary Vertex Lc+',                15, 0, 15)
ut.bookHist(h, 'dC4MS',     'Charmed Hadron Multiplicity at Primary Vertex Lc+ (Selected)',     15, 0, 15)

ut.bookHist(h, 'dC1M2',     'Charmed Hadron Multiplicity at Secondary Vertex D+',               8, 0, 8)
ut.bookHist(h, 'dC1M2S',    'Charmed Hadron Multiplicity at Secondary Vertex D+ (Selected)',    8, 0, 8)
ut.bookHist(h, 'dC2M2',     'Charmed Hadron Multiplicity at Secondary Vertex D0',               8, 0, 8)
ut.bookHist(h, 'dC2M2S',    'Charmed Hadron Multiplicity at Secondary Vertex D0 (Selected)',    8, 0, 8)
ut.bookHist(h, 'dC3M2',     'Charmed Hadron Multiplicity at Secondary Vertex Ds+',              8, 0, 8)
ut.bookHist(h, 'dC3M2S',    'Charmed Hadron Multiplicity at Secondary Vertex Ds+ (Selected)',   8, 0, 8)
ut.bookHist(h, 'dC4M2',     'Charmed Hadron Multiplicity at Secondary Vertex Lc+',              8, 0, 8)
ut.bookHist(h, 'dC4M2S',    'Charmed Hadron Multiplicity at Secondary Vertex Lc+ (Selected)',   8, 0, 8)

def makePlots(work_dir):

  #Neutrino Beam Energy Histograms
  ut.bookCanvas(h,key='CnuE',title='Incoming Neutrino Beam Energy',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat('mr')
  cv = h['CnuE'].cd(1)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  r.gPad.Update()
  sBox_nuE = h['nuE'].FindObject('stats')
  sBox_nuE.SetY1NDC(0.8)
  sBox_nuE.SetY2NDC(0.7)
  h['g-nuEs'].SetFillStyle(3335)
  h['g-nuEs'].SetFillColor(2)
  h['g-nuEs'].Draw('SAMES')
  cv = h['CnuE'].cd(2)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  h['l-nuEs'].SetFillStyle(3335)
  h['l-nuEs'].SetFillColor(2)
  h['l-nuEs'].Draw('SAMES')
  cv = h['CnuE'].cd(3)
  h['nuE'].Draw()
  h['nuE'].SetXTitle('Energy (GeV)')
  h['d-nuEs'].SetFillStyle(3335)
  h['d-nuEs'].SetFillColor(2)
  h['d-nuEs'].Draw('SAMES')
  h['CnuE'].Print(work_dir+'/Histograms/CnuE.pdf')

  '''
  #Efficiency Plot With Neutrino Energy Spectrum
  ut.bookCanvas(h,key='CnuEff',title='Efficiency Plot',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEff'].cd(1)
  h['nuE'].Draw()
  h['g-nuEs'].Draw()
  h['g-nuEs'].Sumw2()
  h['g-nuEff'].Divide(h['g-nuEs'],h['nuE'],1.,1.,'B')
  h['g-nuEff'].Draw('E0')
  h['g-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(2)
  h['nuE'].Draw()
  h['l-nuEs'].Draw()
  h['l-nuEs'].Sumw2()
  h['l-nuEff'].Divide(h['l-nuEs'],h['nuE'],1.,1.,'B')
  h['l-nuEff'].Draw('E0')
  h['l-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(3)
  h['nuE'].Draw()
  h['d-nuEs'].Draw()
  h['d-nuEs'].Sumw2()
  h['d-nuEff'].Divide(h['d-nuEs'],h['nuE'],1.,1.,'B')
  h['d-nuEff'].Draw('E0')
  h['d-nuEff'].SetXTitle('Energy (GeV)')
  h['CnuEff'].Print(work_dir+'/Histograms/CnuEff.pdf')
  '''

  #Efficiency Plot With Neutrino Energy Spectrum: Incremental Search
  ut.bookCanvas(h,key='CnuEff',title='Efficiency Plot',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEff'].cd(1)
  h['nuE'].Draw()
  h['g-nuEs'].Draw()
  h['g-nuEs'].Sumw2()
  h['g-nuEff'].Divide(h['g-nuEs'],h['nuE'],1.,1.,'B')
  h['g-nuEff'].Draw('E0')
  h['g-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(2)
  h['g-nuEs'].Draw()
  h['l-nuEs'].Draw()
  h['l-nuEs'].Sumw2()
  h['l-nuEff'].Divide(h['l-nuEs'],h['g-nuEs'],1.,1.,'B')
  h['l-nuEff'].Draw('E0')
  h['l-nuEff'].SetXTitle('Energy (GeV)')
  cv = h['CnuEff'].cd(3)
  h['l-nuEs'].Draw()
  h['d-nuEs'].Draw()
  h['d-nuEs'].Sumw2()
  h['d-nuEff'].Divide(h['d-nuEs'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEff'].Draw('E0')
  h['d-nuEff'].SetXTitle('Energy (GeV)')
  h['CnuEff'].Print(work_dir+'/Histograms/CnuEff.pdf')

  #Efficiency Plot With Neutrino Energy Spectrum: Break Down Search
  ut.bookCanvas(h,key='CnuEffBD',title='Efficiency Plot',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEffBD'].cd(1)
  h['l-nuEs'].Draw()
  h['d-nuEsFL'].Draw()
  h['d-nuEsFL'].Sumw2()
  h['d-nuEffFL'].Divide(h['d-nuEsFL'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEffFL'].Draw('E0')
  h['d-nuEffFL'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffBD'].cd(2)
  h['l-nuEs'].Draw()
  h['d-nuEsIP'].Draw()
  h['d-nuEsIP'].Sumw2()
  h['d-nuEffIP'].Divide(h['d-nuEsIP'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEffIP'].Draw('E0')
  h['d-nuEffIP'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffBD'].cd(3)
  h['l-nuEs'].Draw()
  h['d-nuEsOKA'].Draw()
  h['d-nuEsOKA'].Sumw2()
  h['d-nuEffOKA'].Divide(h['d-nuEsOKA'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEffOKA'].Draw('E0')
  h['d-nuEffOKA'].SetXTitle('Energy (GeV)')
  h['CnuEffBD'].Print(work_dir+'/Histograms/CnuEffBD.pdf')

  #Efficiency Plot With Neutrino Energy Spectrum: Seperated Charm Flavors
  ut.bookCanvas(h,key='CnuEffCF',title='Efficiency Plot',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat(0)
  cv = h['CnuEffCF'].cd(1)
  h['l-nuEs'].Draw()
  h['d-nuEs1'].Draw()
  h['d-nuEs1'].Sumw2()
  h['d-nuEff1'].Divide(h['d-nuEs1'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEff1'].Draw('E0')
  h['d-nuEff1'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(2)
  h['l-nuEs'].Draw()
  h['d-nuEs2'].Draw()
  h['d-nuEs2'].Sumw2()
  h['d-nuEff2'].Divide(h['d-nuEs2'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEff2'].Draw('E0')
  h['d-nuEff2'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(3)
  h['l-nuEs'].Draw()
  h['d-nuEs3'].Draw()
  h['d-nuEs3'].Sumw2()
  h['d-nuEff3'].Divide(h['d-nuEs3'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEff3'].Draw('E0')
  h['d-nuEff3'].SetXTitle('Energy (GeV)')
  cv = h['CnuEffCF'].cd(4)
  h['l-nuEs'].Draw()
  h['d-nuEs4'].Draw()
  h['d-nuEs4'].Sumw2()
  h['d-nuEff4'].Divide(h['d-nuEs4'],h['l-nuEs'],1.,1.,'B')
  h['d-nuEff4'].Draw('E0')
  h['d-nuEff4'].SetXTitle('Energy (GeV)')
  h['CnuEffCF'].Print(work_dir+'/Histograms/CnuEffCF.pdf')

  #Scatter Plot for Correlation Between Lepton Energy and Neutrino Energy
  ut.bookCanvas(h,key='CCorr',title='Correlation Between Lepton Energy and Neutrino Energy',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat('nmr')
  cv = h['CCorr'].cd(1)
  h['eCorr'].Draw('BOX')
  h['eCorr'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['eCorr'].SetYTitle('#mu Energy (GeV)')
  cv = h['CCorr'].cd(2)
  h['g-eCorrs'].Draw('BOX')
  h['g-eCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['g-eCorrs'].SetYTitle('#mu Energy (GeV)')
  cv = h['CCorr'].cd(3)
  h['l-eCorrs'].Draw('BOX')
  h['l-eCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['l-eCorrs'].SetYTitle('#mu Energy (GeV)')
  cv = h['CCorr'].cd(4)
  h['d-eCorrs'].Draw('BOX')
  h['d-eCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['d-eCorrs'].SetYTitle('#mu Energy (GeV)')
  h['CCorr'].Print(work_dir+'/Histograms/CCorr.pdf')

  #Scatter Plot for Correlation Between Charmed Hadron FL and Neutrino Energy
  ut.bookCanvas(h,key='CfCorr',title='Correlation Between Lepton Energy and Neutrino Energy',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat('nmr')
  cv = h['CfCorr'].cd(1)
  h['fCorr'].Draw('BOX')
  h['fCorr'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['fCorr'].SetYTitle('H_{C} Flight Length (mm)')
  cv = h['CfCorr'].cd(2)
  h['g-fCorrs'].Draw('BOX')
  h['g-fCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['g-fCorrs'].SetYTitle('H_{C} Flight Length (mm)')
  cv = h['CfCorr'].cd(3)
  h['l-fCorrs'].Draw('BOX')
  h['l-fCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['l-fCorrs'].SetYTitle('H_{C} Flight Length (mm)')
  cv = h['CfCorr'].cd(4)
  h['d-fCorrs'].Draw('BOX')
  h['d-fCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['d-fCorrs'].SetYTitle('H_{C} Flight Length (mm)')
  h['CfCorr'].Print(work_dir+'/Histograms/CfCorr.pdf')

  #Scatter Plot for Correlation Between Charmed Hadron IP and Neutrino Energy
  ut.bookCanvas(h,key='CiCorr',title='Correlation Between Lepton Energy and Neutrino Energy',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat('nmr')
  cv = h['CiCorr'].cd(1)
  h['iCorr'].Draw('BOX')
  h['iCorr'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['iCorr'].SetYTitle('H_{C} Impact Parameter (#mum)')
  cv = h['CiCorr'].cd(2)
  h['g-iCorrs'].Draw('BOX')
  h['g-iCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['g-iCorrs'].SetYTitle('H_{C} Impact Parameter (#mum)')
  cv = h['CiCorr'].cd(3)
  h['l-iCorrs'].Draw('BOX')
  h['l-iCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['l-iCorrs'].SetYTitle('H_{C} Impact Parameter (#mum)')
  cv = h['CiCorr'].cd(4)
  h['d-iCorrs'].Draw('BOX')
  h['d-iCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['d-iCorrs'].SetYTitle('H_{C} Impact Parameter (#mum)')
  h['CiCorr'].Print(work_dir+'/Histograms/CiCorr.pdf')

  #Scatter Plot for Correlation Between Charmed Hadron OK Angles and Neutrino Energy
  ut.bookCanvas(h,key='CokCorr',title='Correlation Between Lepton Energy and Neutrino Energy',nx=1920,ny=1080,cx=2,cy=2)
  r.gStyle.SetOptStat('nmr')
  cv = h['CokCorr'].cd(1)
  h['okCorr'].Draw('BOX')
  h['okCorr'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['okCorr'].SetYTitle('H_{C} O-K Angles (rad)')
  cv = h['CokCorr'].cd(2)
  h['g-okCorrs'].Draw('BOX')
  h['g-okCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['g-okCorrs'].SetYTitle('H_{C} O-K Angles (rad)')
  cv = h['CokCorr'].cd(3)
  h['l-okCorrs'].Draw('BOX')
  h['l-okCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['l-okCorrs'].SetYTitle('H_{C} O-K Angles (rad)')
  cv = h['CokCorr'].cd(4)
  h['d-okCorrs'].Draw('BOX')
  h['d-okCorrs'].SetXTitle('#nu_{#mu} Energy (GeV)')
  h['d-okCorrs'].SetYTitle('H_{C} O-K Angles (rad)')
  h['CokCorr'].Print(work_dir+'/Histograms/CokCorr.pdf')

  #Angular Distribution of Neutrinos in X-axis
  ut.bookCanvas(h,key='CnuAngDistX',title='Angular Distribution of Neutrinos in X-axis',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(1111)
  cv = h['CnuAngDistX'].cd(1)
  h['nuAngDistXB'].Draw('HIST')
  h['nuAngDistXB'].SetXTitle('mrad')
  h['d-nuAngDistXBs'].SetFillStyle(3335)
  h['d-nuAngDistXBs'].SetFillColor(2)
  h['d-nuAngDistXBs'].Draw('SAME')
  cv = h['CnuAngDistX'].cd(2)
  h['nuAngDistXA'].Draw('HIST')
  h['nuAngDistXA'].SetXTitle('mrad')
  h['d-nuAngDistXAs'].SetFillStyle(3335)
  h['d-nuAngDistXAs'].SetFillColor(2)
  h['d-nuAngDistXAs'].Draw('SAME')
  cv = h['CnuAngDistX'].cd(3)
  h['nuAngDistXF'].Draw('HIST')
  h['nuAngDistXF'].SetXTitle('mrad')
  h['d-nuAngDistXFs'].SetFillStyle(3335)
  h['d-nuAngDistXFs'].SetFillColor(2)
  h['d-nuAngDistXFs'].Draw('SAME')
  h['CnuAngDistX'].Print(work_dir+'/Histograms/CnuAngDistX.pdf')

  #Angular Distribution of Neutrinos in Y-axis
  ut.bookCanvas(h,key='CnuAngDistY',title='Angular Distribution of Neutrinos in Y-axis',nx=2880,ny=540,cx=3,cy=1)
  r.gStyle.SetOptStat(1111)
  cv = h['CnuAngDistY'].cd(1)
  h['nuAngDistYB'].Draw('HIST')
  h['nuAngDistYB'].SetXTitle('mrad')
  h['d-nuAngDistYBs'].SetFillStyle(3335)
  h['d-nuAngDistYBs'].SetFillColor(2)
  h['d-nuAngDistYBs'].Draw('SAME')
  cv = h['CnuAngDistY'].cd(2)
  h['nuAngDistYA'].Draw('HIST')
  h['nuAngDistYA'].SetXTitle('mrad')
  h['d-nuAngDistYAs'].SetFillStyle(3335)
  h['d-nuAngDistYAs'].SetFillColor(2)
  h['d-nuAngDistYAs'].Draw('SAME')
  cv = h['CnuAngDistY'].cd(3)
  h['nuAngDistYF'].Draw('HIST')
  h['nuAngDistYF'].SetXTitle('mrad')
  h['d-nuAngDistYFs'].SetFillStyle(3335)
  h['d-nuAngDistYFs'].SetFillColor(2)
  h['d-nuAngDistYFs'].Draw('SAME')
  h['CnuAngDistY'].Print(work_dir+'/Histograms/CnuAngDistY.pdf')

  #Angular Distribution of Neutrinos X-Y Scatter Plot
  ut.bookCanvas(h,key='CnuAng2D',title='Angular Distribution X-Y Scatter Plot',nx=2880,ny=1080,cx=3,cy=2)
  r.gStyle.SetOptStat(1111)
  cv = h['CnuAng2D'].cd(1)
  h['nuAng2DB'].Draw('COLZ')
  h['nuAng2DB'].SetXTitle('mrad')
  h['nuAng2DB'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(2)
  h['nuAng2DA'].Draw('COLZ')
  h['nuAng2DA'].SetXTitle('mrad')
  h['nuAng2DA'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(3)
  h['nuAng2DF'].Draw('COLZ')
  h['nuAng2DF'].SetXTitle('mrad')
  h['nuAng2DF'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(4)
  h['d-nuAng2DBs'].Draw('COLZ')
  h['d-nuAng2DBs'].SetXTitle('mrad')
  h['d-nuAng2DBs'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(5)
  h['d-nuAng2DAs'].Draw('COLZ')
  h['d-nuAng2DAs'].SetXTitle('mrad')
  h['d-nuAng2DAs'].SetYTitle('mrad')
  cv = h['CnuAng2D'].cd(6)
  h['d-nuAng2DFs'].Draw('COLZ')
  h['d-nuAng2DFs'].SetXTitle('mrad')
  h['d-nuAng2DFs'].SetYTitle('mrad')
  h['CnuAng2D'].Print(work_dir+'/Histograms/CnuAng2D.pdf')

  #Space Angle Distribution of Neutrinos Scatter Plot
  ut.bookCanvas(h,key='CnuAngSpc',title='Angular Distribution of Neutrinos in Y-axis',nx=1920,ny=540,cx=2,cy=1)
  r.gStyle.SetOptStat(1111)
  cv = h['CnuAngSpc'].cd(1)
  h['nuAngSpcF'].Draw('HIST')
  h['nuAngSpcF'].SetXTitle('mrad')
  cv = h['CnuAngSpc'].cd(2)
  h['d-nuAngSpcFs'].Draw('HIST')
  h['d-nuAngSpcFs'].SetXTitle('mrad')
  h['CnuAngSpc'].Print(work_dir+'/Histograms/CnuAngSpc.pdf')

  #Charmed Hadron Fraction Histogram
  ut.bookCanvas(h,key='CcFrac',title='Produced Charmed Hadron Fractions',nx=1920,ny=540,cx=2,cy=1)
  r.gStyle.SetOptStat(0)
  cv = h['CcFrac'].cd(1)
  cv.SetGridy()
  h['cFracProd'].SetFillStyle(3335)
  h['cFracProd'].SetFillColor(2)
  h['cFracProd'].Draw('HIST DM(2)')
  h['cFracProd'].GetXaxis().SetBinLabel(1,"D^{+}")
  h['cFracProd'].GetXaxis().SetBinLabel(2,"D^{0}")
  h['cFracProd'].GetXaxis().SetBinLabel(3,"D_{s}^{+}")
  h['cFracProd'].GetXaxis().SetBinLabel(4,"#Lambda_{c}^{+}")
  cv = h['CcFrac'].cd(2)
  cv.SetGridy()
  h['cFracSelc'].SetFillStyle(3335)
  h['cFracSelc'].SetFillColor(2)
  h['cFracSelc'].Draw('HIST')
  h['cFracSelc'].GetXaxis().SetBinLabel(1,"D^{+}")
  h['cFracSelc'].GetXaxis().SetBinLabel(2,"D^{0}")
  h['cFracSelc'].GetXaxis().SetBinLabel(3,"D_{s}^{+}")
  h['cFracSelc'].GetXaxis().SetBinLabel(4,"#Lambda_{c}^{+}")
  h['cFracSelc'].Draw('HIST DM(2)')
  h['CcFrac'].Print(work_dir+'/Histograms/CcFrac.pdf')

########################

  #Charmed Hadron Energy Histograms
  ut.bookCanvas(h,key='dEnergyAnalysis',title='Produced Charmed Hadron Energies',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dEnergyAnalysis'].cd(1)
  r.gStyle.SetOptStat(1111)
  h['dC1E'].Draw()
  h['dC1E'].SetXTitle('Energy (GeV)')
  h['dC1ES'].SetFillStyle(3335)
  h['dC1ES'].SetFillColor(2)
  h['dC1ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(2)
  h['dC2E'].Draw()
  h['dC2E'].SetXTitle('Energy (GeV)')
  h['dC2ES'].SetFillStyle(3335)
  h['dC2ES'].SetFillColor(2)
  h['dC2ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(3)
  h['dC3E'].Draw()
  h['dC3E'].SetXTitle('Energy (GeV)')
  h['dC3ES'].SetFillStyle(3335)
  h['dC3ES'].SetFillColor(2)
  h['dC3ES'].Draw('same')
  cv = h['dEnergyAnalysis'].cd(4)
  h['dC4E'].Draw()
  h['dC4E'].SetXTitle('Energy (GeV)')
  h['dC4ES'].SetFillStyle(3335)
  h['dC4ES'].SetFillColor(2)
  h['dC4ES'].Draw('same')
  h['dEnergyAnalysis'].Print(work_dir+'/Histograms/dcenergy.pdf')

  #Flight Length Histograms
  ut.bookCanvas(h,key='dFLAnalysis',title='Produced Charmed Hadron Flight Lengths',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dFLAnalysis'].cd(1)
  h['dC1FL'].Draw()
  h['dC1FL'].SetXTitle('Decay Length (mm)')
  h['dC1FLS'].SetFillStyle(3335)
  h['dC1FLS'].SetFillColor(2)
  h['dC1FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(2)
  h['dC2FL'].Draw()
  h['dC2FL'].SetXTitle('Decay Length (mm)')
  h['dC2FLS'].SetFillStyle(3335)
  h['dC2FLS'].SetFillColor(2)
  h['dC2FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(3)
  h['dC3FL'].Draw()
  h['dC3FL'].SetXTitle('Decay Length (mm)')
  h['dC3FLS'].SetFillStyle(3335)
  h['dC3FLS'].SetFillColor(2)
  h['dC3FLS'].Draw('same')
  cv = h['dFLAnalysis'].cd(4)
  h['dC4FL'].Draw()
  h['dC4FL'].SetXTitle('Decay Length (mm)')
  h['dC4FLS'].SetFillStyle(3335)
  h['dC4FLS'].SetFillColor(2)
  h['dC4FLS'].Draw('same')
  h['dFLAnalysis'].Print(work_dir+'/Histograms/dcfl.pdf')

  #Impact Parameter Histograms
  ut.bookCanvas(h,key='dIPAnalysis',title='Produced Charmed Hadron Impact Parameters',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dIPAnalysis'].cd(1)
  h['dC1IP'].Draw()
  h['dC1IP'].SetXTitle('Decay Length (#mum)')
  h['dC1IPS'].SetFillStyle(3335)
  h['dC1IPS'].SetFillColor(2)
  h['dC1IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(2)
  h['dC2IP'].Draw()
  h['dC2IP'].SetXTitle('Decay Length (#mum)')
  h['dC2IPS'].SetFillStyle(3335)
  h['dC2IPS'].SetFillColor(2)
  h['dC2IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(3)
  h['dC3IP'].Draw()
  h['dC3IP'].SetXTitle('Decay Length (#mum)')
  h['dC3IPS'].SetFillStyle(3335)
  h['dC3IPS'].SetFillColor(2)
  h['dC3IPS'].Draw('same')
  cv = h['dIPAnalysis'].cd(4)
  h['dC4IP'].Draw()
  h['dC4IP'].SetXTitle('Decay Length (#mum)')
  h['dC4IPS'].SetFillStyle(3335)
  h['dC4IPS'].SetFillColor(2)
  h['dC4IPS'].Draw('same')
  h['dIPAnalysis'].Print(work_dir+'/Histograms/dcip.pdf')

  #Multiplicity at Neutrino Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis',title='Multiplicity at Primary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dMultAnalysis'].cd(1)
  h['dC1M'].Draw()
  h['dC1MS'].SetFillStyle(3335)
  h['dC1MS'].SetFillColor(2)
  h['dC1MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(2)
  h['dC2M'].Draw()
  h['dC2MS'].SetFillStyle(3335)
  h['dC2MS'].SetFillColor(2)
  h['dC2MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(3)
  h['dC3M'].Draw()
  h['dC3MS'].SetFillStyle(3335)
  h['dC3MS'].SetFillColor(2)
  h['dC3MS'].Draw('same')
  cv = h['dMultAnalysis'].cd(4)
  h['dC4M'].Draw()
  h['dC4MS'].SetFillStyle(3335)
  h['dC4MS'].SetFillColor(2)
  h['dC4MS'].Draw('same')
  h['dMultAnalysis'].Print(work_dir+'/Histograms/dcmult.pdf')

  #Multiplicity at Charm Vertex Histograms
  ut.bookCanvas(h,key='dMultAnalysis2',title='Multiplicity at Secondary Vertex',nx=1920,ny=1080,cx=2,cy=2)
  cv = h['dMultAnalysis2'].cd(1)
  h['dC1M2'].Draw()
  h['dC1M2S'].SetFillStyle(3335)
  h['dC1M2S'].SetFillColor(2)
  h['dC1M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(2)
  h['dC2M2'].Draw()
  h['dC2M2S'].SetFillStyle(3335)
  h['dC2M2S'].SetFillColor(2)
  h['dC2M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(3)
  h['dC3M2'].Draw()
  h['dC3M2S'].SetFillStyle(3335)
  h['dC3M2S'].SetFillColor(2)
  h['dC3M2S'].Draw('same')
  cv = h['dMultAnalysis2'].cd(4)
  h['dC4M2'].Draw()
  h['dC4M2S'].SetFillStyle(3335)
  h['dC4M2S'].SetFillColor(2)
  h['dC4M2S'].Draw('same')
  h['dMultAnalysis2'].Print(work_dir+'/Histograms/dcmult2.pdf')

  #Kink Angle Histograms
  ut.bookCanvas(h,key='kAngle',title='Kink Angle',nx=1920,ny=540,cx=3,cy=1)
  cv = h['kAngle'].cd(1)
  h['dC1KA'].Draw()
  h['dC1KA'].SetXTitle('Kink Angle (rad)')
  h['dC1KAS'].SetFillStyle(3335)
  h['dC1KAS'].SetFillColor(2)
  h['dC1KAS'].Draw('same')
  cv = h['kAngle'].cd(2)
  h['dC3KA'].Draw()
  h['dC3KA'].SetXTitle('Kink Angle (rad)')
  h['dC3KAS'].SetFillStyle(3335)
  h['dC3KAS'].SetFillColor(2)
  h['dC3KAS'].Draw('same')
  cv = h['kAngle'].cd(3)
  h['dC4KA'].Draw()
  h['dC4KA'].SetXTitle('Kink Angle (rad)')
  h['dC4KAS'].SetFillStyle(3335)
  h['dC4KAS'].SetFillColor(2)
  h['dC4KAS'].Draw('same')
  h['kAngle'].Print(work_dir+'/Histograms/kAngle.pdf')

  #Opening Angle Histograms
  ut.bookCanvas(h,key='oAngle',title='Opening Angle',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['oAngle'].cd(1)
  h['dC2OA'].Draw()
  h['dC2OA'].SetXTitle('Opening Angle (rad)')
  h['dC2OAS'].SetFillStyle(3335)
  h['dC2OAS'].SetFillColor(2)
  h['dC2OAS'].Draw('same')
  h['oAngle'].Print(work_dir+'/Histograms/oAngle.pdf')

  #Neutrino Interactions at Transverse Plane Histogram
  ut.bookCanvas(h,key='nutp',title='Transverse Plane Interactions',nx=1920,ny=720,cx=2,cy=1)
  cv = h['nutp'].cd(1)
  h['tplane'].Draw('COLZ')
  cv = h['nutp'].cd(2)
  h['tplaneS'].Draw('COLZ')
  h['nutp'].Print(work_dir+'/Histograms/nutplane.pdf')

  #Z-axis interactions
  ut.bookCanvas(h,key='zaxis',title='Z Axis Interactions',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['zaxis'].cd(1)
  h['za'].Draw()
  h['zaS'].SetFillStyle(3335)
  h['zaS'].SetFillColor(2)
  h['zaS'].Draw('same')
  h['zaxis'].Print(work_dir+'/Histograms/nuZ.pdf')

  #Bjorken X distribution
  ut.bookCanvas(h,key='bjor',title='Bjorken X Distribution',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['bjor'].cd(1)
  h['BjorX'].Draw()
  h['BjorXs'].SetFillStyle(3335)
  h['BjorXs'].SetFillColor(2)
  h['BjorXs'].Draw('same')
  h['bjor'].Print(work_dir+'/Histograms/bjorkenX.pdf')

  #Inelasticity Y distribution
  ut.bookCanvas(h,key='inel',title='Inelasticity Y Distribution',nx=1920,ny=1080,cx=1,cy=1)
  cv = h['inel'].cd(1)
  h['InelY'].Draw()
  h['InelYs'].SetFillStyle(3335)
  h['InelYs'].SetFillColor(2)
  h['InelYs'].Draw('same')
  h['inel'].Print(work_dir+'/Histograms/inelasticityY.pdf')
