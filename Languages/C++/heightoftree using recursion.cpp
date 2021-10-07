#include <bits/stdc++.h>
using namespace std;
 

class node
{
    public:
    int data;
    node* lchild;
    node* rchild;
};
 

node* newNode(int data)
{
    node* Node = new node();
    Node->data = data;
    Node->lchild = NULL;
    Node->rchild = NULL;
         
    return(Node);
}
 
/* function to find the height a tree. */
int heightoftree(node* node)
{
    // considering root level as 1
    if (node == NULL)
        return 0;
    else
        return(max(heightoftree(node->lchild),heightoftree(node->rchild))+1);
}
 

int main()
{
    node *root = newNode(1);
    root->lchild = newNode(2);
    root->rchild = newNode(4);
    root->lchild->lchild = newNode(6);
    root->lchild->rchild = newNode(10);
     
    cout << "Height of the tree is " << heightoftree(root);
    return 0;
}
