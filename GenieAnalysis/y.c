{
    //Input files and trees
    TFile *f_e = new TFile("../genie_events/genie-nu_e.root");
    TTree *t_e = (TTree*)f_e->Get("gst");

    TFile *f_e_bar = new TFile("../genie_events/genie-nu_e_bar.root");
    TTree *t_e_bar = (TTree*)f_e_bar->Get("gst");

    TFile *f_mu = new TFile("../genie_events/genie-nu_mu.root");
    TTree *t_mu = (TTree*)f_mu->Get("gst");

    TFile *f_mu_bar = new TFile("../genie_events/genie-nu_mu_bar.root");
    TTree *t_mu_bar = (TTree*)f_mu_bar->Get("gst");

    TFile *f_tau = new TFile("../genie_events/genie-nu_tau.root");
    TTree *t_tau = (TTree*)f_tau->Get("gst");

    TFile *f_tau_bar = new TFile("../genie_events/genie-nu_tau_bar.root");
    TTree *t_tau_bar = (TTree*)f_tau_bar->Get("gst");

    //Canvas setup
    TCanvas *c = new TCanvas("c", "Title", 1920, 1080);

    //Histogram setup
    TH1F *h1 = new TH1F("#nu_{e} + #bar{#nu}_{e}", "Inelasticity y distribution for #nu + #bar{#nu}", 100, 0, 1);
    h1->SetLineColor(2);
    h1->SetLineWidth(2);

    TH1F *h2 = new TH1F("#nu_{#mu} + #bar{#nu}_{#mu}", "Inelasticity y distribution for #nu + #bar{#nu}", 100, 0, 1);
    h2->SetLineColor(3);
    h2->SetLineWidth(2);

    TH1F *h3 = new TH1F("#nu_{#tau} + #bar{#nu}_{#tau}", "Inelasticity y distribution for #nu + #bar{#nu}", 100, 0, 1);
    h3->SetLineColor(4);
    h3->SetLineWidth(2);

    //Event numbers to run the loop
    unsigned int nE_e = t_e->GetEntries();
    unsigned int nE_e_bar = t_e_bar->GetEntries();
    unsigned int nE_mu = t_mu->GetEntries();
    unsigned int nE_mu_bar = t_mu_bar->GetEntries();
    unsigned int nE_tau = t_tau->GetEntries();
    unsigned int nE_tau_bar = t_tau_bar->GetEntries();

    //Take the branch
    double y_e;
    auto y_e_brc = t_e->GetBranch("y");
    y_e_brc->SetAddress(&y_e);

    double y_e_bar;
    auto y_e_bar_brc = t_e_bar->GetBranch("y");
    y_e_bar_brc->SetAddress(&y_e_bar);

    double y_mu;
    auto y_mu_brc = t_mu->GetBranch("y");
    y_mu_brc->SetAddress(&y_mu);

    double y_mu_bar;
    auto y_mu_bar_brc = t_mu_bar->GetBranch("y");
    y_mu_bar_brc->SetAddress(&y_mu_bar);

    double y_tau;
    auto y_tau_brc = t_tau->GetBranch("y");
    y_tau_brc->SetAddress(&y_tau);

    double y_tau_bar;
    auto y_tau_bar_brc = t_tau_bar->GetBranch("y");
    y_tau_bar_brc->SetAddress(&y_tau_bar);

    //The loops
    for (unsigned i=0; i<nE_e ; i++)    {
        t_e->GetEvent(i);
        h1->Fill(y_e);
    }

    for (unsigned j=0; j<nE_e_bar ; j++)    {
        t_e_bar->GetEvent(j);
        h1->Fill(y_e_bar);
    }

    h1->Draw();
    c->Update();

    TPaveStats *s1 = (TPaveStats*)h1->FindObject("stats");
    //double X1 = s1->GetX1NDC();
    double X1 = 0.02;
    double Y1 = s1->GetY1NDC();
    //double X2 = s1->GetX2NDC();
    double X2 = 0.22;
    double Y2 = s1->GetY2NDC();

    s1->SetX1NDC(X1);
    s1->SetX2NDC(X2);

    for (unsigned k=0; k<nE_mu ; k++)    {
        t_mu->GetEvent(k);
        h2->Fill(y_mu);
    }

    for (unsigned l=0; l<nE_mu_bar ; l++)    {
        t_mu_bar->GetEvent(l);
        h2->Fill(y_mu_bar);
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

    for (unsigned m=0; m<nE_tau ; m++)    {
        t_tau->GetEvent(m);
        h3->Fill(y_tau);
    }

    for (unsigned n=0; n<nE_tau_bar ; n++)    {
        t_tau_bar->GetEvent(n);
        h3->Fill(y_tau_bar);
    }

    h3->Draw();
    c->Update();

    TPaveStats *s3 = (TPaveStats*)h3->FindObject("stats");
    double Y13 = (Y12 - (Y22 - Y12) - 0.02);
    double Y23 = (Y12 - 0.02);
    s3->SetX1NDC(X1);
    s3->SetY1NDC(Y13);
    s3->SetX2NDC(X2);
    s3->SetY2NDC(Y23);

    double Y14 = (Y13 - (Y23 - Y13) - 0.02);
    double Y24 = (Y13 - 0.02);
    TLegend *l = new TLegend(X1, Y14, X2, Y24);
    l->AddEntry(h1, "#nu_{e} + #bar{#nu}_{e}");
    l->AddEntry(h2, "#nu_{#mu} + #bar{#nu}_{#mu}");
    l->AddEntry(h3, "#nu_{#tau} + #bar{#nu}_{#tau}");

    h3->Draw("Y+");
    h1->Draw("same");
    h2->Draw("same");

    h1->GetXaxis()->SetTitle("Inelasticity y");
    h2->GetXaxis()->SetTitle("Inelasticity y");
    h3->GetXaxis()->SetTitle("Inelasticity y");

    s1->Draw();
    s2->Draw("same");
    s3->Draw("same");

    l->Draw();

    c->Print("y2.pdf");

}
