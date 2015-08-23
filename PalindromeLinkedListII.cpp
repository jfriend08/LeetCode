/*
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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
  bool isPalindrome(ListNode* head) {
    ListNode* fastP = head;
    ListNode* slowP = head;
    ListNode* revP = NULL;
    while(fastP && fastP->next) {
      fastP = fastP->next->next;
      ListNode* tmpP = slowP->next;
      slowP->next = revP;
      revP = slowP;
      slowP = tmpP;
    }

    if(fastP) {slowP = slowP->next;}

    while(slowP && revP) {
      if(slowP->val != revP->val) {
        return false;
      }
      revP = revP -> next;
      slowP = slowP -> next;
    }
    return true;

  }
};






