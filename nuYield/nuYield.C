void above() {

    gRandom = new TRandom3(0);

    //Input background file
    TFile *fInput = TFile::Open("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_10.0_withCharm_nu.root");

    //Input P
    TH1D *h1d = (TH1D*)fInput->Get("1016");
    Int_t nBins1d = h1d->GetEntries();

    //Pt related histograms
    TH2D *h2d = (TH2D*)fInput->Get("1216");
    TH1D *hP = h2d->ProjectionX("P",0, -1);
    TH1D *hPx[26];

    for (Int_t x=17; x<=25; x++) {
        hPx[x] = h2d->ProjectionY("Pt", x, x);
    }

    //Output P Accepted
    TFile *fOutput = new TFile("BGAcc.root", "UPDATE");
    TH1D *h = new TH1D("1016", "nu_tau momentum (GeV) - Accepted", 400, 0, 400);

    ULong_t Acc, Tot;
    //Calculate weight
    for (Int_t y=10; y<400; y++) {
        Int_t AccW;
        Double_t Plog10 = log10(y+1);
        Int_t theBin = hP->FindBin(Plog10);
        if (theBin > 25) theBin = 25;
        Double_t wX = h1d->GetBinContent(y+1);

        if (wX > 1e9 ) {
            Double_t w = wX/1e3;
            for (Int_t z=0; z<w; z++) {
                Double_t Ptlog10 = hPx[theBin]->GetRandom();
                //hist was filled with: log10(pt+0.01)
                Double_t Pt = pow(10., Ptlog10)-0.01;
                Tot += 1;
                if ( (y+1)/Pt >= 88.92) {
                    AccW += 1;
                    //Acc += 1;
                }
            }
            h->Fill(y,AccW*1e3);
        }
        else {
            Double_t w = wX/1e3;
            for (Int_t z=0; z<w; z++) {
                Double_t Ptlog10 = hPx[theBin]->GetRandom();
                //hist was filled with: log10(pt+0.01)
                Double_t Pt = pow(10., Ptlog10)-0.01;
                Tot += 1;
                if ( (y+1)/Pt >= 88.92) {
                    AccW += 1;
                    //Acc += 1;
                }
            }
            h->Fill(y,AccW);
        }

    }

    h->Draw("HIST");
    fOutput->Write();
    fOutput->Close();

}
void below() {

    gRandom = new TRandom3(0);

    //Input background file
    TFile *fInput = TFile::Open("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_1.0_withCharm_nu.root");

    //Input P
    TH1D *h1d = (TH1D*)fInput->Get("1016");
    Int_t nBins1d = h1d->GetEntries();

    //Pt related histograms
    TH2D *h2d = (TH2D*)fInput->Get("1216");
    TH1D *hP = h2d->ProjectionX("P",0, -1);
    TH1D *hPx[26];

    for (Int_t x=4; x<=17; x++) {
        hPx[x] = h2d->ProjectionY("Pt", x, x);
    }

    //Output P Accepted
    TFile *fOutput = new TFile("BGAcc.root", "UPDATE");
    TH1D *h = (TH1D*)fOutput->Get("1016");

    ULong_t Acc, Tot;
    //Calculate weight
    for (Int_t y=0; y<10; y++) {
        Int_t AccW;
        Double_t Plog10 = log10(y+1);
        Int_t theBin = hP->FindBin(Plog10);
        if (theBin < 1) theBin = 1;
        Double_t wX = h1d->GetBinContent(y+1);

        if ( wX > 1e9 ) {
            Double_t w = wX/1e3;
            for (Int_t z=0; z<w; z++) {
                Double_t Ptlog10 = hPx[theBin]->GetRandom();
                //hist was filled with: log10(pt+0.01)
                Double_t Pt = pow(10., Ptlog10)-0.01;
                Tot += 1;
                if ( (y+1)/Pt >= 88.92) {
                    AccW += 1;
                    //Acc += 1000;
                }
            }
            h->Fill(y,AccW*1e3);
        }
        else {
            Double_t w = wX;
            for (Int_t z=0; z<w; z++) {
                Double_t Ptlog10 = hPx[theBin]->GetRandom();
                //hist was filled with: log10(pt+0.01)
                Double_t Pt = pow(10., Ptlog10)-0.01;
                Tot += 1;
                if ( (y+1)/Pt >= 88.92) {
                    AccW += 1;
                    //Acc += 1;

                }
            }
            h->Fill(y,AccW);
        }
    }

    h->Draw("HIST");
    fOutput->Write();
    fOutput->Close();

}

// MAIN Func

void nuYield() {

    above();
    below();

}
