/*
What are pointers to pointers good for, in practice?

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

class Solution {
public:
    
    void fx(int* ptr){
        *ptr=5;
    }
};



int main(){  
  Solution sol;  
  
  // What are pointers to pointers good for, in practice?

  /*
  then f will ``return'' the value 5 by writing it to the location specified by 
  the pointer passed by the caller; in this case, to the caller's variable i. 
  A function might ``return'' values in this way if it had multiple things to return, 
  since a function can only have one formal return value (that is, it can only return 
  one value via the return statement.) The important thing to notice is that for the 
  function to return a value of type int, it used a parameter of type pointer-to-int.
  */
  int i;
  sol.fx(&i);
  cout<<i<<endl;
    

    /* delete node containing i from list pointed to by lp */
    struct list *lp, *prevlp;
    for(lp = list; lp != NULL; lp = lp->next){
        if(lp->item == i){
            if(lp == list)
                list = lp->next;
            else    
                prevlp->next = lp->next;
            break;
        }
        prevlp = lp;
    }
    /*
    This code works, but it has two blemishes. One is that it has to use an extra variable 
    to keep track of the node one behind the one it's looking at, and the other is that it 
    has to use an extra test to special-case the situation in which the node being deleted 
    is at the head of the list. Both of these problems arise because the deletion of a node 
    from the list involves modifying the previous pointer to point to the next node (that is
    , the node before the deleted node to point to the one following). But, depending on whether 
    the node being deleted is the first node in the list or not, the pointer that needs modifying 
    is either the pointer that points to the head of the list, or the next pointer in the previous node.
    */

//////////////////////////////////////////////
    /*
    We can write another version of the list-deletion code, which is (in some ways, at least) 
    much cleaner, by using a pointer to a pointer to a struct list. 
    */
    struct list **lpp;
    for(lpp = &list; *lpp != NULL; lpp = &(*lpp)->next){
        if((*lpp)->item == i){
            *lpp = (*lpp)->next;
            break;            
        }
    }

    /*
    That single line
    *lpp = (*lpp)->next;
    updates the correct pointer, to splice the node it refers to out of the list, regardless of whether the 
    pointer being updated is the head pointer or one of the next pointers. (Of course, the payoff is not absolute, 
    because the use of a pointer to a pointer to a struct list leads to an algorithm which might not be nearly as 
    obvious at first glance.)
    */

    /*
    The expression:     (*lpp)->next
    describes the next pointer of the struct node which is pointed to by *lpp, that is, which is pointed to by the pointer which is pointed to by lpp. 
    */

    /*
    The expression:     lpp = &(*lpp)->next
    sets lpp to point to the next field of the struct list pointed to by *lpp. In both cases, the parentheses 
    around *lpp are needed because the precedence of * is lower than ->.
    */


//////////////////////////////////////////////
    /*
    As a second, related example, here is a piece of code for inserting a new node into a list, in 
    its proper order. This code uses a pointer-to-pointer-to-struct list for the same reason, namely, 
    so that it doesn't have to worry about treating the beginning of the list specially.
    */

    /* insert node newlp into list */

    struct list **lpp;
    for(lpp = &list; *lpp != NULL; lpp = &(*lpp)->next)
        {
        struct list *lp = *lpp;
        if(newlp->item < lp->item)
            {
            newlp->next = lp;
            *lpp = newlp;
            break;
            }
        }
    }


}










