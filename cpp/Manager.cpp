#include "LinkedList.cpp"
#include "ArrayList.cpp"

// function prototypes
void sort_menu(IList* list);

void main_menu(IList* list)
{
    while(1)
    {
        cout << "--------------------------------------  \n"
             << "g - generate the list                   \n"
             << "p - print the list                      \n"
             << "r - resize the list                     \n"
             << "s - sort the list                       \n"
             << "                                        \n"
             << "q - QUIT                                \n"
             << "--------------------------------------  \n";

        char c = get_char_immediately();

        switch (c) {
            case 'g': list->generate(); list->print(); break;
            case 'p': list->print(); break;
            case 's': sort_menu(list); break;
            case 'q': return;
            default : cout << "Not an option.\n";
        }
    }
}

void sort_menu(IList* list)
{
    while(1)
    {
        cout << "--------------------------------------     \n"
             << "Select a sorting algorithm:                \n"
             << "1 - bubble sort"     "\t best- O(n) \t avg O(n^2) \t worst- O(n^2)\n"
             << "2 - cocktail sort"   
             << "3 - selection sort \n"
             << "4 - insertion sort\n"
             << "5 - shell sort\n"
             << "6 - comb sort\n"
             << "7 - merge sort\n"
             << "8 - heap sort\n"
             << "9 - quick sort\n"
             << "                                        \n"
             << "m - back to main menu\n"
             << "--------------------------------------     \n";

        char c = get_char_immediately();

        switch (c) {
            case '1': list->bubble_sort();    list->print(); return;
            case '2': list->cocktail_sort();  list->print(); return;
            case '3': list->selection_sort(); list->print(); return;
            case '4': list->insertion_sort(); list->print(); return;
            case 'm': return;
            default : cout << "Not an option";
        };
    }
}

int main_2();

int main()
{
    main_2();
    IList* list = new ArrayList(20);

    cout << "Welcome to the super sorter!\n";

    main_menu(list);

    return 0;
}

int main_2()
{
    LinkedList* list = new LinkedList();
}
