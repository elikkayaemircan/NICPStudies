#include "TFile.h"
#include "TTree.h"

//int main(void)  {
{

    TFile *f_e = new TFile("/afs/cern.ch/work/e/etepe2/Emircan_v2.10.0_CharmCCDIS_100K/nu_tau_bar/genie-nu_tau_bar.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_a = new TFile("/afs/cern.ch/work/e/etepe2/Annarita_TRuf/genie-nu_tau_bar.root");
    TTree *t_a = (TTree*)f_a->Get("gst");

    TCanvas *c = new TCanvas("c", "Title");

    gStyle->SetLineWidth(2);
    //gStyle->SetStatY(0.9);
    //gStyle->SetStatX(0.3);

    TH1F *h1 = new TH1F("Emircan", "title", 50, 0, 200);
    h1->SetLineColor(1);
    //h1->SetLineWidth(2);
    //TPaveStats *s1 = (TPaveStats*)h1->FindObject("stats");
    //s1->SetX1NDC(0.5);
    //s1->SetX2NDC(0.9);
    //h1->GetXaxis("0.5");
    //s1->SetX1NDC(0.4);
    TH1F *h2 = new TH1F("Annarita", "title", 50, 0, 200);
    h2->SetLineColor(2);
    //h2->SetLineWidth(2);
    //h2->GetXaxis();

    unsigned int nEvents_e = t_e->GetEntries();
    unsigned int nEvents_a = t_a->GetEntries();

    double Ev_e;
    auto Ev_brc_e = t_e->GetBranch("Ev");
    Ev_brc_e->SetAddress(&Ev_e);

    double Ev_a;
    auto Ev_brc_a = t_a->GetBranch("Ev");
    Ev_brc_a->SetAddress(&Ev_a);

    for (unsigned i=0; i<nEvents_e; i++) {
        t_e->GetEvent(i);
        h1->Fill(Ev_e);
    }

    for (unsigned j=0; j<nEvents_e; j++) {
        t_a->GetEvent(j);
        h2->Fill(Ev_a);
    }

    h2->Draw();
    h1->Draw("same");

    c->Print("main.png");
}
