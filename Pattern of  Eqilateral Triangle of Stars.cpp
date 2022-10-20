#include<iostream>
using namespace std;

int main()
{
  int n;
  cout<<"Enter No. To Print Pattern : ";
  cin>>n;
  cout<<"Hello Guys!";
  
  for(int i=0;i<=n;i++)
  {
    for(int space=0;space<n-i;space++)
      cout<<" ";
    for(int j=0;j<i;j++)
      cout<<"* ";
    
    cout<<endl;
  }
  
}
