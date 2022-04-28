/* thuật toán selection sort:
*** Sắp xếp chọn là một trong những thuật toán đơn giản. Nó thực hiện công việc so sánh các phần tử trong danh sách.
Danh sách chứa các phần tử sẽ được chia làm hai phần. Phần ở bên trái là phần được sắp xếp (sort list) và phần ở bên phải là phần chưa được sắp xếp (unsorted list).
Ban đầu chưa được sắp xếp thì phần sorted list sẽ trống và phần unsorted list sẽ chứa tất cả các phần tử ban đầu.
Phần tử nhỏ nhất trong list sẽ được chọn và tráo đổi với vị trí đầu tiên trong list, tiếp đến sẽ là vị trí nhỏ thứ hai tiếp tục được tráo đổi ngay sau vị trí nhỏ nhất.
**giải thích:
==> Thiết lập giá trị nhỏ nhất (min) về vị trí số 0.

== >Tạo vòng lặp for để di chuyển ranh giới của sorted list và unsorted list.

==> Tìm phần tử nhỏ nhất trong list chưa được sắp xếp.

==> Sau khi tìm được phần tử nhỏ nhất thì đổi chỗ phần tử đó với phần tử đầu tiên. Ở bước này chúng ta cần viết một hàm Swap(), hàm này mình sẽ viết ở bên dưới.

==> Lặp lại cho tới khi list được sắp xếp xong. 
*/

#include <iostream>
using namespace std;

// declare selectionSort void;
void selectionSort(int  arr[], int size)
{
    int small,pos,temp; // initializing small, pos , temp in void function
    for (int i = 0; i < size; i++) //initializing for loop
    {
        small = arr[i];
        pos = i;
        for (int j = i+1; j < size; j++)
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
        cout << arr[i] <<" ";
    }
    
    
}
int main(){
    int n;
    int arr[] = {2,4,6,1,3,9};
    n = 6;
    selectionSort(arr,n);
    return 0;
}