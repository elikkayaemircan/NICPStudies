void drawXSec() {

    TFile *f = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Outputs/XSecROOT/nu_mu/nu_mu_119.root");
    TDirectory *d = (TDirectory*)f->Get("nu_mu_Pb204");

    TGraph *g1 = (TGraph*)d->Get("dis_cc_p_charm");
    TGraph *g2 = (TGraph*)d->Get("dis_cc_n_charm");
    TGraph *g3 = (TGraph*)d->Get("tot_cc");

    double R1 = g1->Integral(0,400);
    double R2 = g2->Integral(0,400);
    double R3 = g3->Integral(0,400);

    cout << "R1: "<< R1 << " R2: " << R2 << " R3: " << R3 << endl;

    double f_Charm = ((R1+R2)/R3)/R3;

    cout << "f_Charm: " << f_Charm << endl;

}
