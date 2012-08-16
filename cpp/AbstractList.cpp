class AbstractList
{
public:
    // pure virtual functions- force class to be abstract
    virtual void generate() = 0;
    virtual void print() = 0;
    
    virtual void insertion_sort() = 0;
    virtual void selection_sort() = 0;
    virtual void shell_sort() = 0;
    virtual void bubble_sort() = 0;
    virtual void cocktail_sort() = 0;
    virtual void quick_sort() = 0;
};