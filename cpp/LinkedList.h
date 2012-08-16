#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include "IList.h"

using namespace std;

class LinkedList : public IList
{
    private:
    int size;
    Node* head;

    public:
    LinkedList();
    LinkedList(int size);
    ~LinkedList();

    // IList interface - force to use it
    private:
    void generate();
    void print();

    void        insert(int x, list_index k);
    void        remove(list_index k);
    list_index  find(int x);
    int         findKth(list_index k);

    void append(int n);
};

#endif // LINKEDLIST_H
