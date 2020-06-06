void summaryYield() {

    TFile *fAcc = TFile::Open("/afs/cern.ch/user/e/eelikkay/prodYield/BGAcc.root");
    TFile *fRaw = TFile::Open("/eos/experiment/ship/user/eelikkaya/NICPStudies/Inputs/pythia8_Geant4_1.0_withCharm_nu.root");

    TH1D *hAcc =  (TH1D*)fAcc->Get("2016");
    TH1D *hRawA = (TH1D*)fRaw->Get("2016");
    TH1D *hRawB = (TH1D*)fRaw->Get("2016");

    Double_t Acc, Above, Below;

    for (Int_t x=0; x<10; x++) {
        Acc += hAcc->GetBinContent(x+1);
        Below += hRawB->GetBinContent(x+1);
    }

    for (Int_t y=11; y<400; y++) {
        Acc += hAcc->GetBinContent(y+1);
        Above += hRawB->GetBinContent(y+1);
    }

    cout << "Total number of events: " << (Above+Below)*5e6 << endl;
    cout << "Accepted number of events: " << Acc*5e6 << endl;
    cout << "The Ratio: " << Acc/(Above+Below) << endl;

}
