public class quickSort {
   static int  partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int temp, swap;
    int i = low - 1;
    for ( int j = low; j <= high-1; j++){
      if(arr[j] <= pivot)
      {
        i++;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
    swap = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = swap;
    return (i+1);
  } 
  static void QuickSort(int arr[], int left, int right) {
    if(left < right)
    {
      int pindex = partition(arr, left,right);
      QuickSort(arr, left, pindex-1);
      QuickSort(arr, pindex+1,right);
    }
  }
  public static void  main(String[] args){
    int element;
    int arr[] ={10,80,30,90,40,50,70,100,5,89,1000};
    element = arr.length;
    QuickSort(arr,0, element-1);
    for(int i = 0; i < element; i++){

      System.out.print(arr[i] + " ");
    }
  }

}


