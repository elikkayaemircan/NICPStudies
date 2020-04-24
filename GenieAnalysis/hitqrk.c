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
    TH1F *h1 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h1->SetLineColor(2);
    h1->SetLineWidth(2);
    h1->GetXaxis()->SetTitle("PDG code");

    TH1F *h2 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h2->SetLineColor(3);
    h2->SetLineWidth(2);
    h2->GetXaxis()->SetTitle("PDG code");

    TH1F *h3 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h3->SetLineColor(4);
    h3->SetLineWidth(2);
    h3->GetXaxis()->SetTitle("PDG code");

    TH1F *h4 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h4->SetLineColor(2);
    h4->SetLineWidth(2);
    h4->GetXaxis()->SetTitle("PDG code");

    TH1F *h5 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h5->SetLineColor(3);
    h5->SetLineWidth(2);
    h5->GetXaxis()->SetTitle("PDG code");

    TH1F *h6 = new TH1F("htemp", "Hit quark PDG code", 10, -5, 5);
    h6->SetLineColor(4);
    h6->SetLineWidth(2);
    h6->GetXaxis()->SetTitle("PDG code");

    //Event numbers to run the loop
    unsigned int nE_e = t_e->GetEntries();
    unsigned int nE_e_bar = t_e_bar->GetEntries();
    unsigned int nE_mu = t_mu->GetEntries();
    unsigned int nE_mu_bar = t_mu_bar->GetEntries();
    unsigned int nE_tau = t_tau->GetEntries();
    unsigned int nE_tau_bar = t_tau_bar->GetEntries();

    //Take the branch
    int hitqrk_e;
    auto hitqrk_e_brc = t_e->GetBranch("hitqrk");
    hitqrk_e_brc->SetAddress(&hitqrk_e);

    int hitqrk_e_bar;
    auto hitqrk_e_bar_brc = t_e_bar->GetBranch("hitqrk");
    hitqrk_e_bar_brc->SetAddress(&hitqrk_e_bar);

    int hitqrk_mu;
    auto hitqrk_mu_brc = t_mu->GetBranch("hitqrk");
    hitqrk_mu_brc->SetAddress(&hitqrk_mu);

    int hitqrk_mu_bar;
    auto hitqrk_mu_bar_brc = t_mu_bar->GetBranch("hitqrk");
    hitqrk_mu_bar_brc->SetAddress(&hitqrk_mu_bar);

    int hitqrk_tau;
    auto hitqrk_tau_brc = t_tau->GetBranch("hitqrk");
    hitqrk_tau_brc->SetAddress(&hitqrk_tau);

    int hitqrk_tau_bar;
    auto hitqrk_tau_bar_brc = t_tau_bar->GetBranch("hitqrk");
    hitqrk_tau_bar_brc->SetAddress(&hitqrk_tau_bar);

    //The loops
    for (unsigned i=0; i<nE_e ; i++)    {
        t_e->GetEvent(i);
        h1->Fill(hitqrk_e);
    }

    for (unsigned j=0; j<nE_e_bar ; j++)    {
        t_e_bar->GetEvent(j);
        h4->Fill(hitqrk_e_bar);
    }

    for (unsigned k=0; k<nE_mu ; k++)    {
        t_mu->GetEvent(k);
        h2->Fill(hitqrk_mu);
    }

    for (unsigned l=0; l<nE_mu_bar ; l++)    {
        t_mu_bar->GetEvent(l);
        h5->Fill(hitqrk_mu_bar);
    }

    for (unsigned m=0; m<nE_tau ; m++)    {
        t_tau->GetEvent(m);
        h3->Fill(hitqrk_tau);
    }

    for (unsigned n=0; n<nE_tau_bar ; n++)    {
        t_tau_bar->GetEvent(n);
        h6->Fill(hitqrk_tau_bar);
    }

    //Canvas configuration
    c->Divide(3, 2);

    //Draw histograms
    c->cd(1);
    h1->Draw();

    c->cd(2);
    h2->Draw();

    c->cd(3);
    h3->Draw();

    c->cd(4);
    h4->Draw();

    c->cd(5);
    h5->Draw();

    c->cd(6);
    h6->Draw();

    c->Print("hitqrk.pdf");

}
