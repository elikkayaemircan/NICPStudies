{

  TFile *f = new TFile("gntp.0.gst.root");
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

  cout << "Below: " << below << endl;
  cout << "Above: " << above << endl;
 
}
