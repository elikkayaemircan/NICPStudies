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
    TH1F *h1 = new TH1F("htemp", "Charm production from #nu_{e}", 3, 0, 3);
    h1->SetLineColor(2);
    h1->SetLineWidth(2);

    TH1F *h2 = new TH1F("htemp", "Charm production from #nu_{#mu}", 3, 0, 3);
    h2->SetLineColor(3);
    h2->SetLineWidth(2);

    TH1F *h3 = new TH1F("htemp", "Charm production from #nu_{#tau}", 3, 0, 3);
    h3->SetLineColor(4);
    h3->SetLineWidth(2);

    TH1F *h4 = new TH1F("htemp", "Charm production from #bar{#nu}_{e}", 3, 0, 3);
    h4->SetLineColor(2);
    h4->SetLineWidth(2);

    TH1F *h5 = new TH1F("htemp", "Charm production from #bar{#nu}_{#mu}", 3, 0, 3);
    h5->SetLineColor(3);
    h5->SetLineWidth(2);

    TH1F *h6 = new TH1F("htemp", "Charm production from #bar{#nu}_{#tau}", 3, 0, 3);
    h6->SetLineColor(4);
    h6->SetLineWidth(2);

    //Event numbers to run the loop
    unsigned int nE_e = t_e->GetEntries();
    unsigned int nE_e_bar = t_e_bar->GetEntries();
    unsigned int nE_mu = t_mu->GetEntries();
    unsigned int nE_mu_bar = t_mu_bar->GetEntries();
    unsigned int nE_tau = t_tau->GetEntries();
    unsigned int nE_tau_bar = t_tau_bar->GetEntries();

    //Take the branch
    int charm_e;
    auto charm_e_brc = t_e->GetBranch("charm");
    charm_e_brc->SetAddress(&charm_e);

    int charm_e_bar;
    auto charm_e_bar_brc = t_e_bar->GetBranch("charm");
    charm_e_bar_brc->SetAddress(&charm_e_bar);

    int charm_mu;
    auto charm_mu_brc = t_mu->GetBranch("charm");
    charm_mu_brc->SetAddress(&charm_mu);

    int charm_mu_bar;
    auto charm_mu_bar_brc = t_mu_bar->GetBranch("charm");
    charm_mu_bar_brc->SetAddress(&charm_mu_bar);

    int charm_tau;
    auto charm_tau_brc = t_tau->GetBranch("charm");
    charm_tau_brc->SetAddress(&charm_tau);

    int charm_tau_bar;
    auto charm_tau_bar_brc = t_tau_bar->GetBranch("charm");
    charm_tau_bar_brc->SetAddress(&charm_tau_bar);

    //The loops
    for (unsigned i=0; i<nE_e ; i++)    {
        t_e->GetEvent(i);
        h1->Fill(charm_e);
    }

    for (unsigned j=0; j<nE_e_bar ; j++)    {
        t_e_bar->GetEvent(j);
        h4->Fill(charm_e_bar);
    }

    for (unsigned k=0; k<nE_mu ; k++)    {
        t_mu->GetEvent(k);
        h2->Fill(charm_mu);
    }

    for (unsigned l=0; l<nE_mu_bar ; l++)    {
        t_mu_bar->GetEvent(l);
        h5->Fill(charm_mu_bar);
    }

    for (unsigned m=0; m<nE_tau ; m++)    {
        t_tau->GetEvent(m);
        h3->Fill(charm_tau);
    }

    for (unsigned n=0; n<nE_tau_bar ; n++)    {
        t_tau_bar->GetEvent(n);
        h6->Fill(charm_tau_bar);
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

    c->Print("charm.pdf");

}
