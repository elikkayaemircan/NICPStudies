{
  TFile *below = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_1.0_withCharm_nu.root");
  TFile *above = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_10.0_withCharm_nu.root");

  TFile *merged = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_wo2d_withCharm_nu.root", "NEW");

  //nu_e Calc'
  TH1D *bH1012 = (TH1D*)below->Get("1012");
  TH1D *aH1012 = (TH1D*)above->Get("1012");

  TH1D *nH1012 = new TH1D("1012", "nu_e momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_e flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH1012->GetBinContent(i);
    nH1012->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1012->GetBinContent(j);
    nH1012->Fill(j-1,enta);
  }

  nH1012->Draw("HIST");

  //****************************************************************************************************************

  //nu_mu Calc'
  TH1D *bH1014 = (TH1D*)below->Get("1014");
  TH1D *aH1014 = (TH1D*)above->Get("1014");

  TH1D *nH1014 = new TH1D("1014", "nu_mu momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_mu flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH1014->GetBinContent(i);
    nH1014->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1014->GetBinContent(j);
    nH1014->Fill(j-1,enta);
  }

  nH1014->Draw("HIST");

  //****************************************************************************************************************

  //nu_tau Calc'
  TH1D *bH1016 = (TH1D*)below->Get("1016");
  TH1D *aH1016 = (TH1D*)above->Get("1016");

  TH1D *nH1016 = new TH1D("1016", "nu_tau momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_tau flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH1016->GetBinContent(i);
    nH1016->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1016->GetBinContent(j);
    nH1016->Fill(j-1,enta);
  }

  nH1016->Draw("HIST");

  //****************************************************************************************************************

  //nu_e_bar Calc'
  TH1D *bH2012 = (TH1D*)below->Get("2012");
  TH1D *aH2012 = (TH1D*)above->Get("2012");

  TH1D *nH2012 = new TH1D("2012", "nu_e_bar momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_e_bar flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH2012->GetBinContent(i);
    nH2012->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2012->GetBinContent(j);
    nH2012->Fill(j-1,enta);
  }

  nH2012->Draw("HIST");

  //****************************************************************************************************************

  //nu_mu_bar Calc'
  TH1D *bH2014 = (TH1D*)below->Get("2014");
  TH1D *aH2014 = (TH1D*)above->Get("2014");

  TH1D *nH2014 = new TH1D("2014", "nu_mu_bar momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_mu_bar flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH2014->GetBinContent(i);
    nH2014->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2014->GetBinContent(j);
    nH2014->Fill(j-1,enta);
  }

  nH2014->Draw("HIST");

  //****************************************************************************************************************

  //nu_tau_bar Calc'
  TH1D *bH2016 = (TH1D*)below->Get("2016");
  TH1D *aH2016 = (TH1D*)above->Get("2016");

  TH1D *nH2016 = new TH1D("2016", "nu_tau_bar momentum (GeV)", 400, 0, 400);

  cout << "Processing nu_tau_bar flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH2016->GetBinContent(i);
    nH2016->Fill(i-1,entb);
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2016->GetBinContent(j);
    nH2016->Fill(j-1,enta);
  }

  nH2016->Draw("HIST");

  merged->Write();

}
