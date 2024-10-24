
using namespace std;

void TREE(){

  TRandom3 rnd;
  double x;
  TTree *t=new TTree();
  t->Branch("t",&x,"t/D");

  for(int i=0;i<1000;i++){
    x=rnd.Gaus();
    t->Fill();
  }


  auto *h=new TH1D("h","h",50,-10,10);
  t->Draw("t>>h");
  auto *f=new  TF1("f","[0]*TMath::Gaus(x,0,1,1)",-10,10);
  f->FixParameter(0,1);
  t->UnbinnedFit("f","t");
  f->FixParameter(0,h->GetEntries()*h->GetBinWidth(1));
  f->Draw("same");
  cout << "p-val="<<f->GetProb() << endl;
  
  
  



}
