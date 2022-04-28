#include <iostream>
using namespace std;
void bublesort(int arr[],int n)
{
    int temp; // khai bao temp
        for (int i = 0; i < n-1; i++)// dat vong lap de lay stage 1
        // Last i elements are in place
        {
            for (int j = 0; j < n-i-1 ; j++) // long them  vonf lap de lay gia tri cau stage 2
            {
                if(arr[j] > arr[j+1]) //wrong oder
                {
                    temp=arr[j];
                    arr[j] = arr[j+1];  // swap
                    arr[j+1] = temp;  // after swap arr[j] > arr[j+1]
            
                }
            }
            
        }
        cout << "Sorted Array: ";
        for (int i = 0; i < n; i++) // vong lap cuoi de lay cac gia tri da cho
        {
            cout <<" "<< arr[i] << endl; // in ra cac mang da duoc sap xep
        }
}
int main()
{
    int n; // khai bao bien n
    int arr[] = {64, 34, 25, 12, 22, 11, 90}; // khai bao mang
    n = 7; // 7 is the number of elements in the array
    bublesort(arr,n); // function call
    return 0;

}
