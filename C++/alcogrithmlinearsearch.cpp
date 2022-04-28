// concept linear-search algorithm in C++

#include <iostream>
using namespace std;

int lsearch(int arr[], int size, int item) // create function linear seacrh 
{
    for (int i = 0; i < size; i++)  // loop to check each element in array
    {
        if (arr[i] == item) // if arr[i] == item
        {
            return i;
        }
    }
    return -1; // return -1 if not found
    
}
int main()
{

    // create an array of integers   
    int arr[] = {12,7,5,4,11,6};
    int n = 6; // size of array
    int x = 4; // item to be searched

    // declare temp int function main
    int temp;
    temp = lsearch(arr,n,x); // use linear sreach algorithm
    if (temp!= -1)
    {
        cout <<"the item is found at: " << temp+1; 
    }
    else
    {
        cout <<" the item does not found:" << endl;
    }
    return 0;
}