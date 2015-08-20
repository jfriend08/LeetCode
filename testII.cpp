#include <iostream>

using namespace std;

int main()
{	
	int n=0, count;	
	
	if (n==0){
		int a;
		cin >> a;
		count=a;
		n=1;		
	}
	
	for (int i=0; i<count; i++){
		int a, b;
		cin >> a >> b;
		if (a>b) cout<<">"<<endl;
		else if (a==b) cout<<"="<<endl;
		else if (a<b) cout<<"<"<<endl;
	}
	return 0;
	
}	


