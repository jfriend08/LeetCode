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

    int len = 0;
    // check length
    ListNode* pAhead = head;
    while(pAhead) {
      len++;
      pAhead = pAhead->next;
    }

    if (len == 1) {
      return true;
    } else if (len ==0) {
      return false;
    }

    // devide half number
    int half,count = 0;
    if (len%2==0) {
      half = len/2;
    } else {
      half = len/2 + 1;
    }

    ListNode* pForward = head;
    ListNode* revLinkList = NULL;

    while(pForward && count<half) {
      count++;
      if (count < half){
        ListNode* tmp = pForward;
        tmp->next = revLinkList;
        revLinkList = tmp;
      }
      pForward = pForward->next;
    }

    if(len%2==0) {
      pForward = pForward->next;
    }

    ListNode* pReverse;
    while(pForward) {
      int forwardVal = pForward->val;
      int revVal = pReverse->val;
      if(forwardVal != revVal) {
        return false;
      }
      pForward = pForward->next;
      pReverse = pReverse->next;
    }
    return true;
  }
};






