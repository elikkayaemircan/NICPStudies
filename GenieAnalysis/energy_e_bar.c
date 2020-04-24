#include "TFile.h"
#include "TTree.h"

//int main(void)  {
{

    TFile *f_e = new TFile("/afs/cern.ch/work/e/etepe2/Emircan_v2.10.0_CharmCCDIS_100K/nu_e_bar/genie-nu_e_bar.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_a = new TFile("/afs/cern.ch/work/e/etepe2/Annarita_TRuf/genie-nu_e_bar.root");
    TTree *t_a = (TTree*)f_a->Get("gst");

    TCanvas *c = new TCanvas("c", "Title", 1920, 1080);
    gStyle->SetLineWidth(2);


    TH1F *h1 = new TH1F("Emircan", "Incoming neutrino (#bar{#nu}_{e}) energy", 50, 0, 200);
    h1->SetLineColor(1);
    TH1F *h2 = new TH1F("Thomas", "Incoming neutrino (#bar{#nu}_{e}) energy", 50, 0, 200);
    h2->SetLineColor(2);

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

    c->Divide(2,1);

    c->cd(1);
    h1->Draw();

    c->cd(2);
    h2->Draw();

    c->Print("energy_e_bar.pdf");
}
