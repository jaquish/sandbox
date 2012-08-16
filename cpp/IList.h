#ifndef ILIST_H
#define ILIST_H

typedef unsigned int list_index;

class IList
{
public:
    virtual void generate() = 0;
    virtual void print() = 0;
    
    virtual void        insert(int x, list_index k) = 0;
    virtual void        remove(list_index k) = 0;
    virtual list_index  find(int x) = 0;
    virtual int         findKth(list_index k) = 0;

    virtual void insertion_sort() {};
    virtual void selection_sort() {};
    virtual void shell_sort() {};
    virtual void bubble_sort() {};
    virtual void cocktail_sort() {};
    virtual void quick_sort() {};
    
    // prevent memory leak thru IList* 
    virtual ~IList() = 0;

};

inline IList::~IList() { }

#endif // ILIST_H
