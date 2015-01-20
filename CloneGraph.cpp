/*
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

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
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
private:
    // mymap stored the visited ID, and its corresponding new-cloned pointer
    map<int, UndirectedGraphNode*> mymap;
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node==NULL) return NULL;
        // if this original node has been visited, then we should have its new-cloned pointer, so we just return it
        if(mymap.find(node->label) != mymap.end() ) return mymap[node->label];
        
        // this node has not been visited, new clone it, and update mymap
        UndirectedGraphNode* root=new UndirectedGraphNode(node->label);
        mymap[root->label]=root;
        
        // foreach of the neighbors of current node, and do recursion. 
        // so the recursion will new-clone its neighbor or just return the new pointer from mymap
        vector<UndirectedGraphNode *> nv=node->neighbors;
        for(int i=0; i<nv.size(); i++){
            (root->neighbors).push_back( cloneGraph(nv[i]) );
        }
        return root;
    }
};




