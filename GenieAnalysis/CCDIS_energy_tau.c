{

    TFile *f_e = new TFile("/afs/cern.ch/work/e/etepe2/Emircan_v2.10.0_CCDIS_100K/nu_tau/genie-nu_tau.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_a = new TFile("/afs/cern.ch/work/e/etepe2/Annarita_TRuf/genie-nu_tau.root");
    TTree *t_a = (TTree*)f_a->Get("gst");

    TCanvas *c = new TCanvas("c", "Title", 1920, 1080);
    gStyle->SetLineWidth(2);

    TH1F *h1 = new TH1F("Emircan", "#nu_{#tau} energy", 50, 0, 200);
    h1->SetLineColor(1);
    h1->SetLineWidth(2);

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

    h1->Draw();
    c->Update();

    TPaveStats *s1 = (TPaveStats*)h1->FindObject("stats");
    double X1 = s1->GetX1NDC();
    double Y1 = s1->GetY1NDC();
    double X2 = s1->GetX2NDC();
    double Y2 = s1->GetY2NDC();

    TH1F *h2 = new TH1F("Annarita", "#nu_{#tau} energy", 50, 0, 200);
    h2->SetLineColor(2);
    h2->SetLineWidth(2);

    for (unsigned j=0; j<nEvents_a; j++) {
        t_a->GetEvent(j);
        h2->Fill(Ev_a);
    }

    h2->Draw();
    c->Update();

    TPaveStats *s2 = (TPaveStats*)h2->FindObject("stats");
    double Y12 = (Y1 - (Y2 - Y1) - 0.02);
    double Y22 = (Y1 - 0.02);
    s2->SetX1NDC(X1);
    s2->SetY1NDC(Y12);
    s2->SetX2NDC(X2);
    s2->SetY2NDC(Y22);

    double Y13 = (Y12 - (Y22 - Y12) - 0.02);
    double Y23 = (Y12 - 0.02);
    TLegend *l = new TLegend(X1, Y13, X2, Y23);
    l->AddEntry(h1, "Emircan data");
    l->AddEntry(h2, "Annarita data");

    Double_t norm = 1;

    Double_t scale1 = norm/(h1->Integral());
    Double_t scale2 = norm/(h2->Integral());

    h1->Scale(scale1);
    h2->Scale(scale2);

    h2->Draw();
    h1->Draw("same");

    s1->Draw("same");
    s2->Draw("same");

    l->Draw();

    c->Print("CCDIS_energy_tau.pdf");

}
