/*
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

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
    bool isValidSudoku(vector<vector<char> > &board) {
        for(int i=0; i<9; i++){
            vector<int> rowV(9,0), colV(9,0), squV(9,0);
            
            for (int j=0; j<9; j++){
                if (board[i][j] != '.'){
                    int num1=board[i][j]-'1';
                    if (rowV[num1] != 0) return false;
                    else rowV[num1]=1;
                }
                
                if (board[j][i] != '.'){
                    int num2=board[j][i]-'1';
                    if(colV[num2] != 0) return false;
                    else colV[num2]=1;
                }
                
                if(board[i/3*3+j/3][i%3*3+j%3] != '.'){
                    int num3=board[i/3*3+j/3][i%3*3+j%3]-'1';
                    if (squV[num3] !=0) return false;
                    else squV[num3]=1;
                }
            }
            
            
            
        }
        return true;
        
    }
};



int main(){  
  Solution sol;   
  sol.isValidSudoku();

}










