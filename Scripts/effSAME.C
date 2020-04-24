{
    TFile *em = new TFile("../SingleCheck_Mu/emircanGS.root");
    TFile *an = new TFile("../SingleCheck_Mu/antonioGS.root");

    TH1D *hem = (TH1D*)em->Get("effPlot");
    TH1D *han = (TH1D*)an->Get("effPlot");

    TCanvas *c = new TCanvas("c", "title", 1920, 1080);

    gStyle->SetOptStat(0);
    hem->SetLineWidth(2);
    hem->Draw("E0");
    han->SetLineColor(2);
    han->SetLineWidth(2);
    han->Draw("SAME");

    c->Print("test.pdf");
}
