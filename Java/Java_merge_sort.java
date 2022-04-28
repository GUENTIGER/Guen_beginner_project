import java.util.*;

public class Java_merge_sort { // Merge sort algorithm
    static List<Integer> mergeSort(List<Integer> list) { 
        if (list.size() <= 1) { // if the list has only one element, return the list 
            return list;
        }
        int middleIndex = list.size() / 2; // get the middle index of the list after dividing it by 2 to split the list in half
        List<Integer> leftList =
            mergeSort(list.subList(0, middleIndex)); // get the left list 
        List<Integer> rightList =
            mergeSort(list.subList(middleIndex, list.size())); // get the right list
        List<Integer> sortedList = new ArrayList<Integer>(); // create a new list
        int leftIndex = 0; 
        int rightIndex= 0; 
        int leftLength = leftList.size(); 
        int rightLength = rightList.size();
        while (leftIndex < leftLength&& rightIndex < rightLength) { // while the left and right index are less than the length of the left and right list
            if (leftList.get(leftIndex) < rightList.get(rightIndex)) {
                sortedList.add(leftList.get(leftIndex)); // add the left list to the sorted list when if condition is true
                leftIndex++; // then increment the left index
            } else {
                sortedList.add(rightList.get(rightIndex)); // add the right list to the sorted list when if condition is not true
                rightIndex++;
            }
        }
        sortedList.addAll(leftList.subList(leftIndex, leftLength)); 
        sortedList.addAll(rightList.subList(rightIndex, rightLength));
        return sortedList; // return the sorted list
    }

    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>(Arrays.asList(32, 100, 1, 2, 29, 28, 88, 3, 50, 67, 37, 1, 57, 20)); // create a list
        System.out.println(mergeSort(list));
    }
}

