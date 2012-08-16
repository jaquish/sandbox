#include <iostream>
#include <cstdlib>
#include <ctime>

#include "BinaryTree.h"

class Node
{
    friend class BinaryTree;
    int value;
    Node* left;
    Node* right;
    public:
    Node(int n) : value(n) { }
};

BinaryTree::BinaryTree()
{
    srand(time(0));
    Node* cur = root;
    for(int i = 0; i < 5; i++)
    {
       // insert(i);
       insert(rand() % 100);
    }
}

void BinaryTree::insert(int x)
{
    insert(x, root); 
}

void BinaryTree::insert(int x, Node* &n)
{
    if (n == NULL)
    {
        n = new Node(x);
        return;
    }

    if (x < n->value)
    {
        insert(x, n->left);
    } else {
        insert(x, n->right);
    }
}

void BinaryTree::printInOrder(Node* n)
{
    if (n == NULL)
        return;
    printInOrder(n->left);
    cout << n->value << " - ";
    printInOrder(n->right);
}

void BinaryTree::printPreOrder(Node* n)
{
    if (n == NULL)
        return;
    cout << n->value << " - ";
    printPreOrder(n->left);
    printPreOrder(n->right);
}

void BinaryTree::printPostOrder(Node* n)
{
    if (n == NULL)
        return;
    printPostOrder(n->left);
    printPostOrder(n->right);
    cout << n->value << " - ";
}
