#include <TMath.h>

void allInteract() {

    //Input files
    TFile *f_xsec = TFile::Open("/eos/experiment/ship/user/eelikkaya/NICPBackup/Outputs/XSecROOT/nu_mu/nu_mu_0.root");
    TFile *f_eflux = TFile::Open("BGAcc.root");

    //Nu Flux Histogram
    TH1D *efluxNu = (TH1D*)f_eflux->Get("1014");

    //XSec Total CC
    TGraph *xsec204 = (TGraph*)f_xsec->Get("nu_mu_Pb204/tot_cc");
    TGraph *xsec206 = (TGraph*)f_xsec->Get("nu_mu_Pb206/tot_cc");
    TGraph *xsec207 = (TGraph*)f_xsec->Get("nu_mu_Pb207/tot_cc");
    TGraph *xsec208 = (TGraph*)f_xsec->Get("nu_mu_Pb208/tot_cc");

    //XSec CCDIS w/ charm
    TGraph *xsecP204c = (TGraph*)f_xsec->Get("nu_mu_Pb204/dis_cc_p_charm");
    TGraph *xsecN204c = (TGraph*)f_xsec->Get("nu_mu_Pb204/dis_cc_n_charm");
    TGraph *xsecP206c = (TGraph*)f_xsec->Get("nu_mu_Pb206/dis_cc_p_charm");
    TGraph *xsecN206c = (TGraph*)f_xsec->Get("nu_mu_Pb206/dis_cc_n_charm");
    TGraph *xsecP207c = (TGraph*)f_xsec->Get("nu_mu_Pb207/dis_cc_p_charm");
    TGraph *xsecN207c = (TGraph*)f_xsec->Get("nu_mu_Pb207/dis_cc_n_charm");
    TGraph *xsecP208c = (TGraph*)f_xsec->Get("nu_mu_Pb208/dis_cc_p_charm");
    TGraph *xsecN208c = (TGraph*)f_xsec->Get("nu_mu_Pb208/dis_cc_n_charm");

    //Constants
    Int_t nBinsFlux = efluxNu->GetNbinsX();

    Double_t nAvogadro = TMath::Na();
    Double_t dMass = 9.16e+5;   //detector mass in grams
    Double_t dSurface = 78.4;   //detector surface in cm^2
    Double_t nAtoms = nAvogadro*dMass;  // should divided by mass number, but I leave it inside loop

    Double_t nCC, nCharm, fCharm;
    for (Int_t x=0; x<nBinsFlux; x++) {

        Double_t flux = efluxNu->GetBinContent(x+1) / dSurface;

        Double_t sigmaCC = (  (xsec204->Eval(x+1))*0.014/204 +
                              (xsec206->Eval(x+1))*0.241/206 +
                              (xsec207->Eval(x+1))*0.221/207 +
                              (xsec208->Eval(x+1))*0.521/208
        )*1e-38;
        nCC += nAtoms * flux * sigmaCC;

        Double_t sigmaCharm = (  (xsecP204c->Eval(x+1) + xsecN204c->Eval(x+1))*0.014/204 +
                                 (xsecP206c->Eval(x+1) + xsecN206c->Eval(x+1))*0.241/206 +
                                 (xsecP207c->Eval(x+1) + xsecN207c->Eval(x+1))*0.221/207 +
                                 (xsecP208c->Eval(x+1) + xsecN208c->Eval(x+1))*0.521/208
        )*1e-38;
        nCharm += nAtoms * flux * sigmaCharm;

        fCharm += nAtoms * flux * sigmaCC * sigmaCharm/sigmaCC;

    }

    cout << "Number of CC interactions: " << nCC*5e+6 << endl;
    cout << "Number of CCDIS Charm interactions: " << nCharm*5e+6 << endl;
    cout << "Corresponding Charm Function: " << fCharm/nCC << endl;

}
