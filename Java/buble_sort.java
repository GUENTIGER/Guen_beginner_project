public class buble_sort {

  public static void bublesort(int arr[], int n) {
    int temp;
    for ( int i = 0; i < n - 1; i++) {
      for ( int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
    System.out.print("Sorted Array: ");
    for (int i = 0; i < n; i++){// loops to sort the element
    System.out.print(arr[i] + " ");
    }
    
    
  }
  public static void main (String[] args) {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = arr.length; // get the length of the array
    bublesort(arr, n);
/* 
    System.out.print("Sorted Array: ");
    for (int i = 0; i < n; i++)  // print the sorted array
    System.out.print(arr[i] + " "); */
    

  } 
  
}
