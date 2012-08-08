#include <iostream>
#include "IList.cpp"

using namespace std;

class Node
{
  public:
    Node* next;
    int n;
    Node(int _n) { next = NULL; n = _n; }
};

class LinkedList : public IList
{
    int size;
    Node* head;
    LinkedList() { head = NULL; }
    void append(int n);
};

void LinkedList::append(int n)
{
    if (head == NULL)
    {
        head = new Node(n);
        return;
    } else {
        Node* cur = head;
        while ( cur->next != NULL)
        {
            cur = cur->next;
        }
        cur->next = new Node(n);
        return;
    }
}

void LinkedList::insert(int n, list_index k)
{
    if (list_index == 0)
    {
        Node* old_head = head;
        head = new Node(n);
        head->next = old_head;
        size++;
        return;
    }

    // index: 0  1  2  3  4  5  6  7  8  9
    // elemnt A  B  C  D  E  F  G  H  I  J
    // size = 10

    if (list_index > size)
    {
        // can't insert into that position
        return;
    }

    Node* cur = head;
    for(int i = 0; i < k; i++)
    {
       cur = cur->next;
    }
    
    Node* old_tail = cur->next;
    cur->next = new Node(n);
    cur->next->next = old_tail;
    return;
}
