#include<iostream>
using namespace std;
void thuattoanSelection(int arr[], int size)
{
    int small,pos,temp;
    for (int i = 0; i < size-1; i++)
    {
            small = arr[i];
            pos = i;
        for (int j = i + 1 ; j < size; j++)
        {
                if(arr[j] < small)
                {
                    small = arr[j];
                    pos = j;
                }
        }
        temp = arr[i];
        arr[i] = arr[pos];
        arr[pos] = temp;

        
    }
    for (int i = 0; i < size; i++)
    {
       cout << arr[i] << " " ;
    }
    
    
}
int main()
{
    int n;
    int arr[] = {8,4,9,1,3,6,5,2,7};
    n = 9;
    thuattoanSelection(arr, n);

}