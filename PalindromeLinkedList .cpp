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

    ListNode* pAhead = head;
    while(pAhead) {
      len++;
      pAhead = pAhead->next;
    }

    int half;
    if (len%2==0) {
      half = len/2;
    } else {
      half = len/2 +1;
    }

    ListNode* pForward = head;
    ListNode* revLinkList = NULL;
    int count = 0;
    while(pForward && count!= half) {
      count++;
      ListNode* next = pForward->next;
      ListNode* tmp = next;
      tmp ->next = revLinkList;
      revLinkList = next;
    }

  }
};






