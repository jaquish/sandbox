#include <iostream> // printing list
#include <iomanip>  // printing list
#include <ctime>    // seeding random()

#include "LinkedList.h"

class Node
{
  private:
    Node* next;
    int n;
    Node(int _n) { next = NULL; n = _n; }
    friend class LinkedList;
};

LinkedList::LinkedList()
{
    head = NULL;
}


LinkedList::LinkedList(int set_size)
{
    head = NULL;
}

LinkedList::~LinkedList()
{
    Node* h = head;
}

void LinkedList::generate()
{
     
}
void LinkedList::print() {;}

void        LinkedList::remove(list_index k){;}
list_index  LinkedList::find(int x){;}
int         LinkedList::findKth(list_index k){;}

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
    if (k == 0)
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

    if (k > size)
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
