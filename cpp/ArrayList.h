#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include "IList.h"

using namespace std;

const unsigned int element_max = 100;

class ArrayList : public IList
{
    public:
        ArrayList();
        ArrayList(int size);     // constructor
        ~ArrayList();            // destructor

    // force to use IList interface
    private:

        void generate();
        void print();

		void        insert(int x, list_index k);
    	void        remove(list_index k);
    	list_index  find(int x);
    	int         findKth(list_index k);

        // sorting
        void insertion_sort();
        void selection_sort();
        void shell_sort();
        void bubble_sort();
        void cocktail_sort();
        void quick_sort();
        
    private:
        unsigned int list_size;
        int* _list;
};

#endif // ARRAYLIST_H
