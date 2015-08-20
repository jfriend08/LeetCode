#include <fstream>
#include <iostream>
#include <string>
#include <vector> 
#include <list>
#include <sstream>
#include <iterator>
#include <map> 
#include <iomanip>
#include <utility> 
#include <stdlib.h>

using namespace std;
int main(int argc, char *argv[]){
	
	ifstream the_file ( argv[1] );
	int firstnum;
	int lineCount=0;

	// should always start with a value
	while(the_file>>firstnum){			
		// if first num is 0, then do nothing
		if (firstnum==0) {}
		
		// lineCount%3==0 means the first block
		else if(lineCount%3==0){
			cout<<"block1"<<endl;		
			for (int i=0; i<firstnum; i++){
				string var;
				int val;
				the_file >>var >>val;
				cout<<var<<" "<<val<<" ";
			}
			cout<<endl;
		}

		// lineCount%3==1 means the second block
		else if(lineCount%3==1){
			cout<<"block2"<<endl;
			for (int i=0; i<firstnum; i++){
				string var;
				the_file >> var;
				cout<<var<<" ";
			}
			cout<<endl;
		}	

		// lineCount%3==2 means the third block
		else if(lineCount%3==2){
			cout<<"block3"<<endl;
			for (int i=0; i<firstnum; i++){			
				string var;
				int val;
				the_file >> var >> val;
				cout<<var<<" "<<val<<" ";
			}
			cout<<endl;
		}	

		// lineCount is important value for deciding the proper block
		lineCount++;
	}
}