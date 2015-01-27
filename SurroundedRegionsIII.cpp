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
private:
    int rowN, colN;

public:
     void solve(vector<vector<char> > &board) {
        if(board.size()==0) return;
        rowN=board.size();
        colN=board[0].size();
        
        vector<vector<bool> > surroundedTable(rowN, vector<bool>(colN, false) );
        queue<pair<int,int> > myV;

        printVV(board);
        table_init(board,surroundedTable, myV);
        // printVV (surroundedTable);
        // printQ(myV);

        while(!myV.empty()){
            pair<int,int> qtop= myV.front();
            
            int r=qtop.first;   
            int c=qtop.second;
            myV.pop();

            // cout<<"i:"<<r<<" j:"<<c<<endl;
            // r-1,c
            if(r-1>0 && board[r-1][c]=='O' && !surroundedTable[r-1][c] ){myV.push( make_pair(r-1,c)); surroundedTable[r-1][c]=true;}
            // r+1,c
            if(r+1<rowN && board[r+1][c]=='O' && !surroundedTable[r+1][c] ){ myV.push( make_pair(r+1,c)); surroundedTable[r+1][c]=true;}
            // r,c-1
            if(c-1>0 && board[r][c-1]=='O' && !surroundedTable[r][c-1] ){ myV.push( make_pair(r,c-1)); surroundedTable[r][c-1]=true;}
            //r,c+1
            if(c+1<colN && board[r][c+1]=='O' && !surroundedTable[r][c+1] ){ myV.push( make_pair(r,c+1)); surroundedTable[r][c+1]=true;}
        }
        
        printVV(surroundedTable);
        modifyboard(board,surroundedTable);
        printVV(board);


     }

    void table_init(vector<vector<char> > &board, vector<vector<bool> > &surroundedTable, queue<pair<int,int> > &myV){
        for (int i=0; i<rowN; i++){            
            for (int j=0; j<colN; j++){
                if ((i==0|i==rowN-1|j==0|j==colN-1) && board[i][j]=='O'){
                    myV.push(make_pair(i,j) );
                    surroundedTable[i][j]=true;
                }
            }
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
    void printVV(vector<vector<bool> > board){       
        for (int i=0; i<board.size(); i++){
            for (int j=0; j<board[i].size(); j++){
                cout<<board[i][j]<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    
    void modifyboard(vector<vector<char> > &board, vector<vector<bool> > &surroundedTable){
        for(int i=0; i<rowN; i++){
            for (int j=0; j<colN;j++){
                if(surroundedTable[i][j]) board[i][j]='O';
                else if(!surroundedTable[i][j]) board[i][j]='X';
            }
        }
    }
        

};


int main(){
    Solution sol;
    vector<vector<char> > myinput;  

    vector<char> v1 (10,'X');    
    vector<char> v2 (10,'X');    
    vector<char> v3 (10,'X');    
    vector<char> v4 (10,'X');
    vector<char> v5 (10,'X');
    vector<char> v6 (10,'X');
    vector<char> v7 (10,'X');
    vector<char> v8 (10,'X');
    vector<char> v9 (10,'X');
    vector<char> v10 (10,'X');
    myinput.push_back(v1);myinput.push_back(v2);myinput.push_back(v3);myinput.push_back(v4);myinput.push_back(v5);myinput.push_back(v6);
    myinput.push_back(v7);myinput.push_back(v8);myinput.push_back(v9);myinput.push_back(v10);
    myinput[0][1]='O';myinput[0][2]='O';myinput[0][6]='O';myinput[0][8]='O';myinput[0][9]='O';   
    myinput[1][1]='O';   
    myinput[2][4]='O';
    myinput[3][1]='O';myinput[3][5]='O';myinput[3][9]='O';
    myinput[4][0]='O';myinput[4][4]='O';myinput[4][6]='O';myinput[4][8]='O';
    myinput[5][2]='O';myinput[5][5]='O';myinput[5][6]='O';
    myinput[6][0]='O';myinput[6][3]='O';myinput[6][4]='O';myinput[6][6]='O';myinput[6][9]='O';
    myinput[7][0]='O';myinput[7][6]='O';
    myinput[8][1]='O';myinput[8][2]='O';myinput[8][5]='O';myinput[8][8]='O';myinput[8][9]='O';
    myinput[9][3]='O';myinput[9][4]='O';myinput[9][6]='O';myinput[9][9]='O';

    myinput[1][0]='O';myinput[1][3]='O';myinput[1][4]='O';
    myinput[2][1]='O';myinput[2][3]='O';myinput[2][4]='O';myinput[2][5]='O';
    myinput[3][1]='O';myinput[3][2]='O';myinput[3][3]='O';myinput[3][5]='O';
    myinput[4][0]='O';myinput[4][1]='O';myinput[4][4]='O';
    myinput[5][1]='O';myinput[5][3]='O';


    myinput[1][3]='O';myinput[1][4]='O';
    myinput[2][3]='O';myinput[2][4]='O';
    myinput[3][3]='O';


    
    sol.solve(myinput);
}



