{

    TFile *f_e = new TFile("/afs/cern.ch/work/e/etepe2/Emircan_v2.10.0_CharmCCDIS_100K/nu_tau_bar/genie-nu_tau_bar.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_a = new TFile("/afs/cern.ch/work/e/etepe2/Annarita_TRuf/genie-nu_tau_bar.root");
    TTree *t_a = (TTree*)f_a->Get("gst");

    TCanvas *c = new TCanvas("c", "Title", 1920, 1080);
    gStyle->SetLineWidth(2);


    TH1F *h1 = new TH1F("Emircan", "#bar{#nu}_{#tau} charm production", 3, 0, 3);
    h1->SetLineColor(1);
    h1->SetLineWidth(2);
    TH1F *h2 = new TH1F("Annarita", "#bar{#nu}_{#tau} charm production", 3, 0, 3);
    h2->SetLineColor(2);
    h2->SetLineWidth(2);

    unsigned int nEvents_e = t_e->GetEntries();
    unsigned int nEvents_a = t_a->GetEntries();

    int charm_e;
    auto charm_brc_e = t_e->GetBranch("charm");
    charm_brc_e->SetAddress(&charm_e);

    int charm_a;
    auto charm_brc_a = t_a->GetBranch("charm");
    charm_brc_a->SetAddress(&charm_a);

    for (unsigned i=0; i<nEvents_e; i++) {
        t_e->GetEvent(i);
        h1->Fill(charm_e);
    }

    for (unsigned j=0; j<nEvents_a; j++) {
        t_a->GetEvent(j);
        h2->Fill(charm_a);
    }

    c->Divide(2,1);

    c->cd(1);
    h1->Draw();

    c->cd(2);
    h2->Draw();

    c->Print("CharmCCDIS_charm_tau_bar.pdf");
}
