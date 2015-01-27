/*
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

*/

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
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <limits>
#include <queue>
#include <math.h>
#include <stack>

using namespace std;

class Solution {
public:
    void solve(vector<vector<char> > &board) {
    	if(board.size()==0) return;
    	vector<vector<int> > surroundedTable(board.size(), vector<int>(board[0].size(), -1) );

    	table_init(board,surroundedTable);
    	printVV(board);    	 
    	// printVV(surroundedTable);    	 

    	for (int i=0; i<board.size(); i++){
    		for (int j=0; j<board[i].size(); j++){
    			// for the case that characters at the edge
    			if (i==0|i==board.size()-1|j==0|j==board[i].size()-1){
    				// cout<<"i:"<<i<<" j:"<<j<<endl;
    				if (board[i][j]=='X') surroundedTable[i][j]=1;
    				else if (board[i][j]=='O') surroundedTable[i][j]=0;
    			}
    			// not at the edge
    			else{
    				if (board[i][j]=='X') surroundedTable[i][j]=1;
    				else if (board[i][j]=='O') {
    					// cout<<"start here:"<<i<<" "<<j<<endl;
    					surroundedTable[i][j]= checkarround(i,j, board, surroundedTable);
    					// cout<<"now value is:"<<surroundedTable[i][j]<<endl;
    					// printVV(surroundedTable);
    				}
    			}
    		}
    	}        
		// printVV(surroundedTable);    	 
		modifyboard(board, surroundedTable);
		printVV(board);

    }
    void table_init(vector<vector<char> > &board, vector<vector<int> > &surroundedTable){
    	for (int i=0; i<surroundedTable.size(); i++){
    		for (int j=0; j<surroundedTable.size(); j++){
    			if (i==0|i==surroundedTable.size()-1|j==0|j==surroundedTable[i].size()-1){
    				surroundedTable[i][j]= board[i][j]=='X' ? 1:0;
    			}
    		}
    	}
    }

    void modifyboard(vector<vector<char> > &board, vector<vector<int> > &surroundedTable){
    	for(int i=0; i<surroundedTable.size(); i++){
    		for (int j=0; j<surroundedTable[i].size();j++){
    			if(surroundedTable[i][j]==1) board[i][j]='X';
    			// else if(!surroundedTable) board[i][j]='X';
    		}
    	}
    }

    int checkarround(int i, int j, vector<vector<char> > &board, vector<vector<int> > &surroundedTable){
    	// cout<<i<<"_"<<j<<endl;
		// if (board[i][j]=='X') return 1;
    	if (board[i][j]=='X'){
    		surroundedTable[i][j]=1;
    		return 1; 
    	}
    	if (i==0||i==board.size()-1||j==0||j==board[i].size()-1){    		
    		surroundedTable[i][j]= (board[i][j]=='O') ? 0:1;    		
    		return surroundedTable[i][j];
    	}
    	if (board[i-1][j]=='O' && surroundedTable[i-1][j]!=-1){
    		surroundedTable[i][j]=surroundedTable[i-1][j];
    		return surroundedTable[i-1][j];
    		// return surroundedTable[i-1][j]==-1 ? checkarround(i-1, j, board, surroundedTable):surroundedTable[i-1][j];
    	}
    	
    	else if (board[i][j-1]=='O' && surroundedTable[i][j-1]!=-1){
    		surroundedTable[i][j]=surroundedTable[i][j-1];    		
    		return surroundedTable[i][j-1];    		
    	}
    	
    	else if (board[i+1][j]=='O'){
			surroundedTable[i][j]= checkarround(i+1, j, board, surroundedTable)==0 ? 0:checkarround(i, j+1, board, surroundedTable);    		    			    		
    		return surroundedTable[i][j];
    	}
    	
    	else if (board[i][j+1]=='O'){    		
    		surroundedTable[i][j]= checkarround(i, j+1, board, surroundedTable)==0 ? 0:checkarround(i+1, j, board, surroundedTable);    		    			    		
    		return surroundedTable[i][j];
    	}
    	// all neighbors are not X
    	else {
    		surroundedTable[i][j]=1;
    		return 1; 
    	}
    }


    void printVV(vector<vector<char> > board){
    	for (int i=0; i<board.size(); i++){
    		for (int j=0; j<board[i].size(); j++){
    			cout<<board[i][j]<<" ";
    		}
    		cout<<endl;
    	}
    	cout<<endl;
    }
    void printVV(vector<vector<int> > board){    	
    	for (int i=0; i<board.size(); i++){
    		for (int j=0; j<board[i].size(); j++){
    			cout<<board[i][j]<<" ";
    		}
    		cout<<endl;
    	}
    	cout<<endl;
    }

};


int main(){
	vector<vector<char> > myinput;	
	vector<char> v1 (6,'O');	
	vector<char> v2 (6,'X');	
	vector<char> v3 (6,'X');	
	vector<char> v4 (6,'X');
	vector<char> v5 (6,'X');
	vector<char> v6 (6,'O');
	myinput.push_back(v1);myinput.push_back(v2);myinput.push_back(v3);myinput.push_back(v4);myinput.push_back(v5);myinput.push_back(v6);

	myinput[1][0]='O';myinput[1][5]='O';
	myinput[2][0]='O';myinput[2][2]='O';myinput[2][3]='O';myinput[2][5]='O';
	myinput[3][0]='O';myinput[3][2]='O';myinput[3][3]='O';myinput[3][5]='O';
	myinput[4][0]='O';myinput[4][5]='O';


	// vector<char> v1 (10,'X');	
	// vector<char> v2 (10,'X');	
	// vector<char> v3 (10,'X');	
	// vector<char> v4 (10,'X');
	// vector<char> v5 (10,'X');
	// vector<char> v6 (10,'X');
	// vector<char> v7 (10,'X');
	// vector<char> v8 (10,'X');
	// vector<char> v9 (10,'X');
	// vector<char> v10 (10,'X');
	// myinput.push_back(v1);myinput.push_back(v2);myinput.push_back(v3);myinput.push_back(v4);myinput.push_back(v5);myinput.push_back(v6);
	// myinput.push_back(v7);myinput.push_back(v8);myinput.push_back(v9);myinput.push_back(v10);
	// myinput[0][1]='O';myinput[0][2]='O';myinput[0][6]='O';myinput[0][8]='O';myinput[0][9]='O';	
	// myinput[1][1]='O';	
	// myinput[2][4]='O';
	// myinput[3][1]='O';myinput[3][5]='O';myinput[3][9]='O';
	// myinput[4][0]='O';myinput[4][4]='O';myinput[4][6]='O';myinput[4][8]='O';
	// myinput[5][2]='O';myinput[5][5]='O';myinput[5][6]='O';
	// myinput[6][0]='O';myinput[6][3]='O';myinput[6][4]='O';myinput[6][6]='O';myinput[6][9]='O';
	// myinput[7][0]='O';myinput[7][6]='O';
	// myinput[8][1]='O';myinput[8][2]='O';myinput[8][5]='O';myinput[8][8]='O';myinput[8][9]='O';
	// myinput[9][3]='O';myinput[9][4]='O';myinput[9][6]='O';myinput[9][9]='O';

	// myinput[1][0]='O';myinput[1][3]='O';myinput[1][4]='O';
	// myinput[2][1]='O';myinput[2][3]='O';myinput[2][4]='O';myinput[2][5]='O';
	// myinput[3][1]='O';myinput[3][2]='O';myinput[3][3]='O';myinput[3][5]='O';
	// myinput[4][0]='O';myinput[4][1]='O';myinput[4][4]='O';
	// myinput[5][1]='O';myinput[5][3]='O';


	// myinput[1][3]='O';myinput[1][4]='O';
	// myinput[2][3]='O';myinput[2][4]='O';
	// myinput[3][3]='O';
	
	// vector<char> v1 (4,'X');	
	// vector<char> v2 (4,'X');	
	// vector<char> v3 (4,'X');	
	// vector<char> v4 (4,'X');
	// myinput.push_back(v1);myinput.push_back(v2);myinput.push_back(v3);myinput.push_back(v4);
	// myinput[1][1]='O';myinput[1][2]='O';myinput[2][2]='O';myinput[3][1]='O';

	// vector<char> v1 (3,'X');	
	// vector<char> v2 (3,'X');	
	// vector<char> v3 (3,'X');	
	// myinput.push_back(v1);myinput.push_back(v2);myinput.push_back(v3);
	// myinput[0][1]='O';myinput[1][0]='O';myinput[1][2]='O';myinput[2][1]='O';
	
	Solution sol;
	sol.solve(myinput);
	
}























