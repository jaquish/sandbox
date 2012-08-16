#ifndef ILIST_HEADER
#define ILIST_HEADER

typedef int list_index;

class IList
{
public:
    virtual void generate() { ; }
    virtual void print() { ; }
    
    virtual void        insert(int x, list_index k) { ; }
    virtual void        remove(list_index k) { ; }
    virtual list_index  find(int x) { ; }
    virtual int         findKth(list_index k) { ; }

    virtual void insertion_sort() { ; }
    virtual void selection_sort() { ; }
    virtual void shell_sort() { ; }
    virtual void bubble_sort() { ; }
    virtual void cocktail_sort() { ; }
    virtual void quick_sort() { ; }
    
    // force abstract 
    virtual ~IList() = 0;
};

#endif
