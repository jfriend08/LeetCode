/*
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

An important website for pointer to pointer:
http://www.eskimo.com/~scs/cclass/int/sx8.html

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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode *p1=head, **p2=&head;
        // make p1 is n+1 steps ahead
        
        for (int i=1; i<n; i++){
            p1=p1->next;
        }
        
        while (p1->next){
            p1=p1->next;
            p2=&((*p2)->next);
        }
        
        *p2= (*p2)->next;
        return head;
    }
    
};



int main(){  
  Solution sol;  

}










