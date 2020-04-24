void drawXSec() {

    TFile *f = new TFile("/eos/experiment/ship/user/eelikkaya/NICPStudies/Outputs/XSecROOT/nu_mu/xsec_2.root");
    TDirectory *d = (TDirectory*)f->Get("nu_mu_Pb204");
    TGraph *g = (TGraph*)d->Get("dis_cc_n_dval_charm");

    TCanvas *c = new TCanvas();
    c->SetLogy();
    g->Draw();
    g->GetYaxis()->SetLimits(0.01, 10e4);
    c->Print("dis_cc_n_dval_charm.pdf");

}
