/*
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

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

using namespace std;



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        // if there is anyone that empty, then no point to merge. Just return the other one
        if(!l1) return l2;
        if(!l2) return l1;
        
        // initial new pointer, and assign proper beginning loot to it
        ListNode* newList=NULL;
        if(l1->val <= l2->val){newList=l1; l1=l1->next;}
        else if(l1->val > l2->val){newList=l2; l2=l2->next;}
        
        // use the pointer to iterate it
        ListNode* ptr=newList;        
        while (l1 && l2){
            // decide which on to assign to, then move on for next one
            if(l1->val <= l2->val){ptr->next =l1;l1=l1->next;}
            else{ptr->next=l2;l2=l2->next;}            
            // ptr move on too
            ptr=ptr->next;
        }
        
        // if there is anything left, assign the remaining
        if(l2){ptr->next=l2;}
        else if(l1){ptr->next=l1;}
        
        return newList;
    }
};




int main(){  
  Solution sol;
  
}



