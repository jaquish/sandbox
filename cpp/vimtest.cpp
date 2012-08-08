#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>  // atoi

#include "Utility.cpp"
#include "AbstractList.cpp"

using namespace std;

//const unsigned int list_size = 20;
const unsigned int element_max = 100;

class ArrayList : public AbstractList
{
    public:
        ArrayList(int size);     // constructor
        ~ArrayList();            // 

        void generate();
        void print();

        // sorting
        void insertion_sort();
        void selection_sort();
        void shell_sort();
        void bubble_sort();
        void cocktail_sort();
        void quick_sort();
        
    private:
        const unsigned int list_size;
        int* _list;
};

ArrayList::ArrayList(int size) : list_size(size)
{
    _list = new int[size];
    generate();
}

void ArrayList::generate()
{
    srand(time(NULL));
    for (int i = 0; i < list_size; ++i)
    {
        _list[i] = rand() % element_max + 1;
    }
}

void ArrayList::print()
{
    cout << "ArrayList: [";
    for (int i = 0; i < list_size; ++i)
    {
        cout << setw(3) << _list[i];
        if (i != list_size - 1)
            cout << ',';
    }
    cout << "]\n";
}

void ArrayList::insertion_sort()
{
    // go through the list once, in order
    for (int i = 1; i < list_size; i++)
    {
        // save the value at i (so we can shift items right)
        int key = _list[i];

        // from i -> 0, look for insertion spot
        int j;
        for (j = i; j > 0; j--)
        {
            this->print(); // test test 
            if (key > _list[j-1]) {
                break;
            }

            _list[j] = _list[j-1];
        }
        _list[j] = key;
    }
}

void ArrayList::selection_sort()
{
    for (int i = 0; i < list_size; i++)
    {
        this->print();

        // find the minimum
        int min = _list[i];
        int min_index = i;

        for (int j = i; j < list_size; j++)
        {
            if ( _list[j] < min)
            {
                min = _list[j];
                min_index = j;
            }
        }

        // swap with position 1
        int temp = _list[min_index];
        _list[min_index] = _list[i];
        _list[i] = temp;
    }
}

void ArrayList::shell_sort()
{
    ;
}

void ArrayList::bubble_sort()
{
    // continue until all elements are in order (no swaps)
    while(1)
    {
        this->print();

        bool done = true;

        for (int i = 0; i < list_size - 1; i++)
        {
            // bubble up
            if (_list[i] > _list[i+1])
            {
                // swap
                int temp = _list[i];
                _list[i] = _list[i+1];
                _list[i+1] = temp;
                done = false;
            }
        }

        if (done == true)
            return;
    }
}

// naive implementation
void ArrayList::quick_sort()
{
    ;//quick_sort_internal(
}
/*
void ArrayList::quick_sort_internal(unsigned int start, unsigned int end)
{
    if (start == end)
        return;

    // find the median
    int m_left = start;
    int m_right = end;
    int median_index;
    int median;

    while (1)
    {
        m_left++;
        if (m_left == m_right) {
            median_index = m_left;
            break;
        }

        m_right--;
        if (m_left == m_right) {
            median_index = m_left;
            break
        }
    }

    median = _list[median_index];

    // partition
    while(1)
    {
        while( _list[m_left] < median )
            m_left++;

        while( _list[m_right] > median )
            m_right++;

        // swap
        temp       = _list[m_right];
        _list[m_right] = _list[m_left];
        _list[m_left]  = temp;

        if (
}
*/

void ArrayList::cocktail_sort()
{
    ;
}