#ifndef BINARYTREE_H
#define BINARYTREE_H

using namespace std;

class Node;

class BinaryTree
{
    private:
    Node* root;
    
    public:
    BinaryTree();

    void insert(int x);

    void printInOrder() { printInOrder(root); }
    void printPreOrder() { printPreOrder(root);}
    void printPostOrder() { printPostOrder(root);}

    private:
    void insert(int x, Node* &n);
    void printInOrder(Node* n);
    void printPreOrder(Node* n);
    void printPostOrder(Node* n);
};

#endif
