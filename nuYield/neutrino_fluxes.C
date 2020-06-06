#include "TLegend.h"
#include "GenieGenerator.h"
#include "TGeoBBox.h"
#include <map>

//when you discover the difficulty of copying from the masters. Trying to replicate Annarita's studies on neutrino fluxes

void neutrino_fluxes(){ //projecting neutrino fluxes to the target
 TFile * f = TFile::Open("/eos/experiment/ship/data/Mbias/pythia8_Geant4-withCharm_onlyNeutrinos.root");
 TTree *tree = (TTree*) f->Get("pythia8-Geant4");
 TGeoManager * tgeom = new TGeoManager("Geometry", "Geane geometry");
 tgeom->Import("/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_mu/below/7274958.1/geofile_full.conical.Genie-TGeant4.root");
 Double_t targetZ = 2* ((TGeoBBox*) (gGeoManager->GetVolume("volTarget")->GetShape()))->GetDZ();

 //Double_t targetZ = 320.83; 

 cout<<"Spessore bersaglio neutrini da fairship: "<<targetZ<<endl; 

 Double_t bparam;
 Double_t mparam[10];

 GenieGenerator *fMaterialInvestigator = new GenieGenerator();
 Double_t start[3], end[3]; //start and end of neutrino positions at z of neutrino target
 const Int_t nneutrinos = tree->GetEntries();
 //getting the branches

 Float_t id, px, py, pz,w,x,y;

 tree->SetBranchAddress("id",&id);
 tree->SetBranchAddress("x",&x);
 tree->SetBranchAddress("y",&y);
 tree->SetBranchAddress("px",&px);
 tree->SetBranchAddress("py",&py);
 tree->SetBranchAddress("pz",&pz);
 tree->SetBranchAddress("w",&w);
 
 Float_t deltaz = 3969.; //distance between center of proton target and start of neutrino target
 //Float_t deltaz = 5500.;
 Float_t xfin, yfin, tanx,tany; //angles and positions after projections

 Float_t nnudet = 0., nallneutrinos = 0.;
 map<Int_t, Float_t> nall = {{12, 0.},{-12,0.},{14,0.},{-14,0.},{16,0.},{-16,0.}}; //neutrinos produced, mapped per pdg
 map<Int_t, Float_t> ndet = {{12, 0.},{-12,0.},{14,0.},{-14,0.},{16,0.},{-16,0.}}; //neutrinos arrived at det

 map<Int_t, TH1D*> hspectrumdet;

 TFile *outfile = new TFile("neutrinos_detector_upto1GeV.root","RECREATE"); //spectra arrived in detector are saved here
 //nutau
 hspectrumdet[16] = new TH1D("hnu_tau","Spectrum tau neutrinos arrived at detector",1000,0,1);
 hspectrumdet[-16] = new TH1D("hnu_tau_bar","Spectrum tau neutrinos arrived at detector",1000,0,1);
 TH2D *hxy_nutau_arrived = new TH2D("hxy", "XY distribution of tau neutrinos at detector",2000,-1000,1000,2000,-1000,1000);
 TH2D *hxy_nutau_arrived_det = new TH2D("hxy_det", "XY distribution of tau neutrinos at detector",90,-45,45,76,-38,38);

 TH1D *hnutaubar_weight = new TH1D("hnutaubar_weight", "Mean density per length transversed in target region",400,0,400);

 //numu
 hspectrumdet[14] = new TH1D("hnu_mu","Spectrum muon neutrinos arrived at detector",1000,0,1);
 hspectrumdet[-14] = new TH1D("hnu_mu_bar","Spectrum muon antineutrinos arrived at detector",1000,0,1);

 hspectrumdet[12] = new TH1D("hnu_e","Spectrum electron neutrinos arrived at detector",1000,0,1);
 hspectrumdet[-12] = new TH1D("hnu_e_bar","Spectrum electron antineutrinos arrived at detector",1000,0,1);

 Double_t targetdx = 45.15, targetdy = 37.45;
 //Double_t targetdx = 55, targetdy = 55;
 cout<<"N NEUTRINOS: "<<nneutrinos<<endl;
 for (int i = 0; i < nneutrinos; i++){

 tree->GetEntry(i);
 if (i%100000 == 0) cout<<i<<endl;
 tanx = px/pz;
 tany = py/pz;

 Double_t momentum = TMath::Sqrt(pow(px,2) + pow(py,2) + pow(pz,2));

 start[0] = tanx * deltaz; //projecting produced neutrinos to neutrino detector, aggiungere x e y non cambia significativamente il risultato
 start[1] = tany * deltaz;
 start[2] = -3259;

 end[0] = tanx * (deltaz + targetZ);
 end[1] = tany * (deltaz + targetZ);
 end[2] = start[2] + targetZ;

 nallneutrinos += w;

 nall[id] +=w;

 if(TMath::Abs(start[0]) < targetdx && TMath::Abs(start[1]) < targetdy){ //checking how many neutrinos are inside the detector
  nnudet += w;
  ndet[id] += w;
  hspectrumdet[id]->Fill(momentum,w);
  bparam = fMaterialInvestigator->MeanMaterialBudget(start, end, mparam);
  if (id == -16) hnutaubar_weight->Fill(mparam[0]/mparam[4]);
  }
 }
 
// cout<<hxy_all->Integral()<<endl; //totale entries
 cout<<nallneutrinos<<endl;
 cout<<nnudet<<endl; //dovrebbe escludere underflow and overflow
 cout<<"Ratio arriving at det: "<<nnudet/nallneutrinos<<endl;

 cout<<"Electron neutrinos"<<endl;
 cout<<nall[12]<<" "<<nall[-12]<<endl;
 cout<<ndet[12]<<" "<<ndet[-12]<<endl; //dovrebbe escludere underflow and overflow
 cout<<"Ratio arriving at det: "<<ndet[12]/nall[12]<<" "<<ndet[-12]/nall[-12]<<endl;;

 cout<<"Muon neutrinos"<<endl;
 cout<<nall[14]<<" "<<nall[-14]<<endl;
 cout<<ndet[14]<<" "<<ndet[-14]<<" "<<endl; //dovrebbe escludere underflow and overflow
 cout<<"Ratio arriving at det: "<<ndet[14]/nall[14]<<" "<<ndet[-14]/nall[-14]<<endl;

 cout<<"Tau neutrinos and anti neutrinos"<<endl;
 cout<<nall[16]<<" "<<nall[-16]<<endl;
 cout<<ndet[16]<<" "<<ndet[-16]<<endl; //dovrebbe escludere underflow and overflow
 cout<<"Ratio arriving at det: "<<ndet[16]/nall[16]<<" "<<ndet[-16]/nall[-16]<<endl;

 TCanvas *c4 = new TCanvas();
 hxy_nutau_arrived->Draw("COLZ");
 TCanvas *c5 = new TCanvas();
 hxy_nutau_arrived_det->Draw("COLZ");

 outfile->Write();
 outfile->Close();
}
