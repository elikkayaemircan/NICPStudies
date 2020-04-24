{
  TFile *below = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_1.0_withCharm_nu.root");
  TFile *above = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_10.0_withCharm_nu.root");

  //nu_e Calc'
  TH1D *bH1012 = (TH1D*)below->Get("1012");
  TH1D *aH1012 = (TH1D*)above->Get("1012");
  Double_t nue = 0.0;

  cout << "Processing nu_e flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH1012->GetBinContent(i);
    nue += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1012->GetBinContent(j);
    nue += enta;
  }

  cout << "Number of nu_e: " << nue << endl;

  //****************************************************************************************************************

  //nu_mu Calc'
  TH1D *bH1014 = (TH1D*)below->Get("1014");
  TH1D *aH1014 = (TH1D*)above->Get("1014");
  Double_t numu = 0.0;

  cout << "Processing nu_mu flux.." << endl;
  for (Int_t i=1; i<=10; i++)  {
    Double_t entb = bH1014->GetBinContent(i);
    numu += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1014->GetBinContent(j);
    numu += enta;
  }

  cout << "Number of nu_mu: " << numu << endl;

  //****************************************************************************************************************

  //nu_tau Calc'
  TH1D *bH1016 = (TH1D*)below->Get("1016");
  TH1D *aH1016 = (TH1D*)above->Get("1016");
  Double_t nutau = 0.0;

  cout << "Processing nu_tau flux.." << endl;
  for (Int_t i=0; i<=10; i++)  {
    Double_t entb = bH1016->GetBinContent(i);
    nutau += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH1016->GetBinContent(j);
    nutau += enta;
  }

  cout << "Number of nu_tau: " << nutau << endl;

  //****************************************************************************************************************

  //nu_e_bar Calc'
  TH1D *bH2012 = (TH1D*)below->Get("2012");
  TH1D *aH2012 = (TH1D*)above->Get("2012");
  Double_t nuebar = 0.0;

  cout << "Processing nu_e_bar flux.." << endl;
  for (Int_t i=0; i<=10; i++)  {
    Double_t entb = bH2012->GetBinContent(i);
    nuebar += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2012->GetBinContent(j);
    nuebar += enta;
  }

  cout << "Number of nu_e_bar: " << nuebar << endl;

  //****************************************************************************************************************

  //nu_mu_bar Calc'
  TH1D *bH2014 = (TH1D*)below->Get("2014");
  TH1D *aH2014 = (TH1D*)above->Get("2014");
  Double_t numubar = 0.0;

  cout << "Processing nu_mu_bar flux.." << endl;
  for (Int_t i=0; i<=10; i++)  {
    Double_t entb = bH2014->GetBinContent(i);
    numubar += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2014->GetBinContent(j);
    numubar += enta;
  }

  cout << "Number of nu_mu_bar: " << numubar << endl;

  //****************************************************************************************************************

  //nu_tau_bar Calc'
  TH1D *bH2016 = (TH1D*)below->Get("2016");
  TH1D *aH2016 = (TH1D*)above->Get("2016");
  Double_t nutaubar = 0.0;

  cout << "Processing nu_tau_bar flux.." << endl;
  for (Int_t i=0; i<=10; i++)  {
    Double_t entb = bH2016->GetBinContent(i);
    nutaubar += entb;
  }

  for (Int_t j=11; j<=400; j++)  {
    Double_t enta = aH2016->GetBinContent(j);
    nutaubar += enta;
  }

  cout << "Number of nu_tau_bar: " << nutaubar << endl;

}
