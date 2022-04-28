#include<iostream>
using namespace std;
 
void merge(int arr[],int l,int m,int r) 
{

        int i,j,k;
        int nL = m-l+1;
        int nR= r-m;    
        //creat temp arrays    
        int L[nL],R[nR];

        // copy element
        for (i = 0; i < nL; i++) // copy left part
        {
            L[i]=arr[l+i];
        }
        for ( j = 0; j < nR ; j++) // copy right part
        {
        R[j]=arr[m+1+j]; 
        }
        //merging step 7-8
        i = 0,j =0,k = l;
        while (i < nL && j <nR) 
        {
         if(L[i]<R[j]) // if left part is smaller than right part
         {
             arr[k] = L[i];
             i++;
         }
         else
         {
             arr[k] = R[j];
             j++;
         }
         k++;
        }
        // step 9; Elements remaining in left subarray
        while (i < nL)
        {
            arr[k] = L[i];
            i++,k++;
        }
        // element remaining in right subarray
        while (j < nR)
        {
            arr[k] = R[j];
            j++,k++;
        }      

}
void mergesort(int arr[],int l, int r)
{
    if(l<r)
    {
        int m =(l+r)/2;
        //step 1:

        // chia mảng trong 2 mang rieng biet
        mergesort(arr,l,m);  // left subarray
        mergesort(arr,m+1,r); // right subarray

        //step 2: merge the two halves
        merge(arr,l,m,r); // merge the two halves


    }

}

int main(){
    int n;
    int arr[] = {38,27,43,3,9,82,10};
    n = 7;
    mergesort(arr,0,n-1);
    //st10;
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    


}