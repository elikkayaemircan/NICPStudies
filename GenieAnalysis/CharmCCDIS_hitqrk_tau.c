{

    TFile *f_e = new TFile("/afs/cern.ch/work/e/etepe2/Emircan_v2.10.0_CharmCCDIS_100K/nu_tau/genie-nu_tau.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_a = new TFile("/afs/cern.ch/work/e/etepe2/Annarita_TRuf/genie-nu_tau.root");
    TTree *t_a = (TTree*)f_a->Get("gst");

    TCanvas *c = new TCanvas("c", "Title", 1920, 1080);
    gStyle->SetLineWidth(2);


    TH1F *h1 = new TH1F("Emircan", "CharmCCDIS events hit quark pdg code for #nu_{#tau}", 10, -5, 5);
    h1->SetLineColor(1);
    h1->SetLineWidth(2);
    TH1F *h2 = new TH1F("Annarita", "CCDIS events hit quark pdg code for neutrino (#nu_{#tau})", 10, -5, 5);
    h2->SetLineColor(2);
    h2->SetLineWidth(2);

    unsigned int nEvents_e = t_e->GetEntries();
    unsigned int nEvents_a = t_a->GetEntries();

    int hitqrk_e;
    auto hitqrk_brc_e = t_e->GetBranch("hitqrk");
    hitqrk_brc_e->SetAddress(&hitqrk_e);

    int hitqrk_a;
    auto hitqrk_brc_a = t_a->GetBranch("hitqrk");
    hitqrk_brc_a->SetAddress(&hitqrk_a);

    for (unsigned i=0; i<nEvents_e; i++) {
        t_e->GetEvent(i);
        h1->Fill(hitqrk_e);
    }

    for (unsigned j=0; j<nEvents_a; j++) {
        t_a->GetEvent(j);
        h2->Fill(hitqrk_a);
    }

    c->Divide(2,1);

    c->cd(1);
    h1->Draw();

    c->cd(2);
    h2->Draw();

    c->Print("CharmCCDIS_hitqrk_tau.pdf");
}
