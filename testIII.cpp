#include <iostream>
#include <vector> 
#include <algorithm> 
#include <map> 
using namespace std;

struct elm{
	int val;
	int idx;
};

bool myfunction (elm i,elm j) { return (i.val<j.val); }



int main()
{	
	map<int,int> mymap;	
	int numI, numD;
	cin >> numI >> numD;		
	
	vector<elm> v, result;	

	for (int i=0; i<numI;i++){
		int a;
		elm cur_elm;
		cin >> a;
		cur_elm.val=a;
		cur_elm.idx=i;
		v.push_back(cur_elm);
	}

	sort (v.begin(), v.begin()+numI, myfunction);

	int sum=0;
	for (int i=0; sum+v[i].val<=numD && i<v.size(); i++){
		sum=sum+v[i].val;		
		cout<<v[i].idx;		
	}
	cout<<endl;
	return 0;
	
}	


