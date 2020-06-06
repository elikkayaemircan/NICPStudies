#include "TLegend.h"
#include "GenieGenerator.h"
#include "TGeoBBox.h"
#include <map>

Double_t nu_yield_general(const char* nu = "nu_mu", const char* intmode = "dis_cc", const char* charmmode = "");
void nu_yield(){ //passing neutrino types and interaction mode to nu_yield_general for estimation
  /*
  TCanvas *cspectra = new TCanvas();
  cspectra->Divide(3,3);
    
  cout<<"Yields per nue"<<endl;
  cspectra->cd(1);
  Double_t nue_dis_cc = nu_yield_general("nu_e","dis_cc");
  cspectra->cd(2);
  Double_t nue_bar_dis_cc = nu_yield_general("nu_e_bar","dis_cc");
  cspectra->cd(3);
  Double_t nue_res_cc = nu_yield_general("nu_e","res_cc");
  cspectra->cd(4);
  Double_t nue_bar_res_cc = nu_yield_general("nu_e_bar","res_cc");
  cspectra->cd(5);
  Double_t nue_qel_cc = nu_yield_general("nu_e","qel_cc");
  cspectra->cd(6);
  Double_t nue_bar_qel_cc = nu_yield_general("nu_e_bar","qel_cc");
  cspectra->cd(7);
  Double_t nue_dis_cc_charm =  nu_yield_general("nu_e","dis_cc","_charm");
  cspectra->cd(8);
  Double_t nue_bar_dis_cc_charm = nu_yield_general("nu_e_bar","dis_cc","_charm");
  cspectra->cd(9);
  Double_t nue_el =  nu_yield_general("nu_e","ve_ccncmix");
  Double_t nue_bar_el =  nu_yield_general("nu_e_bar","ve_ccncmix");
  cout<<endl;


  cout<<"NU: "<<" "<<"CCDIS"<<" "<<"CHARM"<<" "<<"RES"<<" "<<"QE"<<" "<<"NUEEL"<<endl;
  cout<<"NUE"<<" "<<nue_dis_cc<<" "<<nue_dis_cc_charm<<" "<<nue_res_cc<<" "<<nue_qel_cc<<" "<<nue_el<<endl;
  cout<<"ANTINUE"<<" "<<nue_bar_dis_cc<<" "<<nue_bar_dis_cc_charm<<" "<<nue_bar_res_cc<<" "<<nue_bar_qel_cc<<" "<<nue_bar_el<<endl;
  cout<<"Yields per numu"<<endl;
  */
  TCanvas *cspectramu = new TCanvas();
  //cspectramu->Divide(3,3);

  //cspectramu->cd(1);
  Double_t numu_dis_cc_charm =nu_yield_general("nu_mu","dis_cc","_charm");
  /*
  cspectramu->cd(2);
  //Double_t numu_bar_dis_cc_charm =nu_yield_general("nu_mu_bar","dis_cc","_charm");
  cspectramu->cd(3);
  Double_t numu_dis_cc = nu_yield_general("nu_mu","dis_cc");
  cspectramu->cd(4);  
  Double_t numu_bar_dis_cc =nu_yield_general("nu_mu_bar","dis_cc");
  cspectramu->cd(5);  
  Double_t numu_res_cc =nu_yield_general("nu_mu","res_cc");
  cspectramu->cd(6);
  Double_t numu_bar_res_cc =nu_yield_general("nu_mu_bar","res_cc");
  cspectramu->cd(7);
  Double_t numu_qel_cc =nu_yield_general("nu_mu","qel_cc");
  cspectramu->cd(8);
  Double_t numu_bar_qel_cc =nu_yield_general("nu_mu_bar","qel_cc");
  cspectramu->cd(9);
  Double_t numu_el =nu_yield_general("nu_mu","ve_nc");   
  Double_t numu_bar_el =nu_yield_general("nu_mu_bar","ve_nc");
  */
  cout<<endl;

  //cout<<"NUMU"<<" "<<numu_dis_cc<<" "<<numu_dis_cc_charm<<" "<<numu_res_cc<<" "<<numu_qel_cc<<" "<<numu_el<<endl;
  //cout<<"NUMU"<<" "<<numu_dis_cc_charm<<endl;
  //cout<<"ANTINUMU"<<" "<<numu_bar_dis_cc<<" "<<numu_bar_dis_cc_charm<<" "<<numu_bar_res_cc<<" "<<numu_bar_qel_cc<<" "<<numu_bar_el<<endl;
  
  /*
  TCanvas *cspectratau = new TCanvas();
  cspectratau->Divide(3,3);
  cout<<"Yields per nutau"<<endl;
  cspectratau->cd(1);
  Double_t nutau_dis_cc_charm =nu_yield_general("nu_tau","dis_cc","_charm");
  cspectratau->cd(2);
  Double_t nutau_bar_dis_cc_charm =nu_yield_general("nu_tau_bar","dis_cc","_charm");
  cspectratau->cd(3);
  Double_t nutau_dis_cc = nu_yield_general("nu_tau","dis_cc");
  cspectratau->cd(4);
  Double_t nutau_bar_dis_cc =nu_yield_general("nu_tau_bar","dis_cc");
  cspectratau->cd(5);
  Double_t nutau_qel_cc =nu_yield_general("nu_tau","qel_cc");
  cspectratau->cd(6);
  Double_t nutau_bar_qel_cc =nu_yield_general("nu_tau_bar","qel_cc");
  cspectratau->cd(7);  
  Double_t nutau_res_cc =nu_yield_general("nu_tau","res_cc");
  cspectratau->cd(8);
  Double_t nutau_bar_res_cc =nu_yield_general("nu_tau_bar","res_cc");
  cspectratau->cd(9);
  Double_t nutau_el =nu_yield_general("nu_tau","ve_nc");   
  Double_t nutau_bar_el =nu_yield_general("nu_tau_bar","ve_nc");

  cout<<"NUTAU"<<" "<<nutau_dis_cc<<" "<<nutau_dis_cc_charm<<" "<<nutau_res_cc<<" "<<nutau_qel_cc<<" "<<nutau_el<<endl;
  cout<<"ANTINUTAU"<<" "<<nutau_bar_dis_cc<<" "<<nutau_bar_dis_cc_charm<<" "<<nutau_bar_res_cc<<" "<<nutau_bar_qel_cc<<" "<<nutau_bar_el<<endl;
  */
  
}
//general layout with FORM to estimate number of neutrino interactions 
Double_t nu_yield_general(const char* nu = "nu_mu", const char* intmode = "dis_cc", const char* charmmode = ""){     
  TFile *xsec = TFile::Open("/eos/experiment/ship/user/eelikkaya/NICPBackup/Outputs/XSecROOT/nu_mu/nu_mu_0.root"); //normal splines are cut at 350 GeV
  //TFile *flux = TFile::Open("neutrinos_detector.root");
  TFile *flux = TFile::Open("neutrinos_detector_upto1GeV.root");

  //const char* nu = "nu_mu"; //neutrino type
  //const char* intmode = "dis_cc"; //interaction mode;

  //  const char* charmmode = "_charm"; //write _charm for CHARMCCDIS
  
  TH1D *hfluxnu = (TH1D*) flux->Get(Form("h%s",nu));

  bool nullp = false, nulln = false, nullother = false; //for DIS both are possible, but not for other interactions
  TGraph *hxsec_p = (TGraph*) xsec->Get(Form("%s_Pb208/%s_p%s",nu,intmode,charmmode));   
  TGraph *hxsec_n = (TGraph*) xsec->Get(Form("%s_Pb208/%s_n%s",nu,intmode,charmmode));
  TGraph *hxsec_other = (TGraph*) xsec->Get(Form("%s_Pb208/%s%s",nu,intmode,charmmode));
  if (hxsec_p == NULL) nullp = true;
  if (hxsec_n == NULL) nulln = true;
  if (hxsec_other == NULL) nullother = true;
  
  const Int_t A = 208; //initial approximation, only pb208 considered
  const Int_t Z = 82;

  Float_t Ninteracting = 0.;
  Double_t mass = 8183*1e+3; //mass in grams
  //Double_t surface = 90.3 * 74.9; //surface in square centimetres (rectangular configuration)
  Double_t surface = 80. * 80.; //surface in square centimetres (squared configuration)
  //Double_t surface = 1.4e+4;
  
  Double_t avogadro = 6.022e+23;
  Double_t NT = mass/A * avogadro;  
  Double_t x, y ,ysec;

  TFile *outputfile = new TFile(Form("plots/results_%s_%s%s.root",nu,intmode,charmmode),"RECREATE");
  TGraph *hxsec_total = new TGraph(); //summing protons and neutrons when both are present
  TH1D *hspectrum_int = new TH1D(Form("hspectrum_%s_int%s%s",nu,intmode,charmmode),Form("Spettro neutrini %s interagenti in %s%s",nu,intmode,charmmode), 400, 0, 400); 
  TH1D *htest = new TH1D(Form("htest_%s_int%s%s",nu,intmode,charmmode),Form("Spettro neutrini %s interagenti in %s%s",nu,intmode,charmmode), 400, 0, 400); 

  for (int n = 0; n < hfluxnu->GetNbinsX(); n++){
  
  y = hfluxnu->GetBinContent(n+1);
  x = hfluxnu->GetBinLowEdge(n+1) + hfluxnu->GetBinWidth(n+1)/2.;
  
  if (nullp && nulln && nullother) cout<<Form("ERROR: no cross sections are present for neutrino %s in interaction %s%s",nu,intmode,charmmode)<<endl;
  if (nullp && nulln) ysec = hxsec_other->Eval(x);
  else if (nullp) ysec = hxsec_n->Eval(x);
  else if (nulln) ysec = hxsec_p->Eval(x);
  else ysec = (hxsec_p->Eval(x) + hxsec_n->Eval(x)); //summing proton and neutron cross section

  hxsec_total->SetPoint(n+1,x,ysec);
  Ninteracting = ysec *1e-38 * NT * y/surface * hfluxnu->GetBinWidth(n+1);  
  htest->SetBinContent(n+1,hfluxnu->GetBinWidth(n+1)*y);
  hspectrum_int->SetBinContent(n+1,Ninteracting);

  }
  Double_t counting = hfluxnu->Integral();

  Double_t yield =  hspectrum_int->Integral(0,400);
  //cout<<Form("numero neutrini %s per spill interagenti in mode %s%s",nu,intmode,charmmode)<<" "<<hspectrum_int->Integral()<<endl;
  hspectrum_int->Draw();
  hspectrum_int->GetXaxis()->SetTitle("GeV/c");
  // hxsec_total->Draw();
  hxsec_total->SetTitle(Form("cross section from GENIE for %s in interaction mode %s%s",nu,intmode,charmmode));
  outputfile->Write();
  hxsec_total->Write("xsec");
  outputfile->Close();
  //cout<<"TEST "<<htest->GetEntries()<<endl;
  //Double_t countingtest = htest->Integral();
  //cout<<"Test conteggio "<<counting<<"integrale manuale "<<countingtest<<endl;
  return yield;
}
