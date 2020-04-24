{

  unsigned int totalabove=0, totalbelow=0;

  {
  unsigned int above = 0, below = 0;

  for(Int_t i=0; i<130; i++){

    cout << "Inside the folder: " << i << endl;

    TString file="/eos/experiment/ship/user/eelikkaya/NICPStudies/WeightEvents/nu_e/7039684."; file+=i;

    TFile *f = new TFile(file+"/gntp.0.gst.root");
    TTree *t = (TTree*)f->Get("gst");

    unsigned int nEvents = t->GetEntries();
    unsigned int above = 0, below = 0;

    double Ev;
    auto Ev_brc = t->GetBranch("Ev");
    Ev_brc->SetAddress(&Ev);

    for (unsigned j=0; j<nEvents; j++) {
        t->GetEvent(j);
        if ( Ev <= 10.0 )  {
          below++ ;
        }
        else {
          above++ ;
        }
    }

  cout << above << endl;
  totalabove += above;

  cout << below << endl;
  totalbelow += below;
 
  }
  }

  cout << """Event weights in total==" << endl;

  cout << totalabove/125 << endl;
  cout << totalbelow/125 << endl;

}
