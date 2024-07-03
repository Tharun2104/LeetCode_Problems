**1. What is a data structure?** <br>
* A data structure is a format for organizing, processing, retrieving and storing data so it can be easily accessed and effectively used. Data structures serve as frameworks for arranging data for specific needs or objectives. <br>
  
**2. The first data structure we studied is a list, and we summarized seven properties of a list by asking seven questions. Answer these seven questions for a list and what the answer means. These answers should be about Python lists, not any other language. Use average case**
*  Reading/Index : Reading/Indexing or Accessing an element by its index in a list is O(1) constant because lists are contiguous arrays and the indexes are directly maps to a memory address. Hence accessing the element by its index is one step.
*  Searching for a value not contained within the list : Searching an element requires checking by iterating through each and every element in the list. So it takes N(100) steps. The average case for searching for a value not contained within the list is O(N). 
*  Insertion at the beginning of the list : Inserting an element at the beginning requires shifting all other elements one position to the right. So for inserting it takes one step and for shifting all other elements it takes N steps, total N+1 (100+1) steps for inserting at the beginning of the list. By dropping out the constants the time complexity is O(N).
*  Insertion at the end of the list : Appending an element to the end of the list takes one step in most cases. So the time complexity in O(1).
*  Deletion at the beginning of the list : Deleting the first element requires shifting all other elements one position to the left. So, for deleting one step and shifting all other elements requires N-1 steps, total of N (100) steps.
*  Deletion at the end of the list : Removing or popping out the last element from a list does not require shifting the elements so it takes only one step.
*  Sorting the list : Sorting of list generally takes NlogN steps. First it should iterate through the list and sort combinedly it takes NlogN steps. Generally sorting use different algorithms, the average case has time complexity of NlogN


**3. Why do you need to study different data structures? Why is a list not sufficient? Hint: Answer these questions by discussing operations you can perform on data structures.**
* Studying different data structures is essential. Some of the other data structures provides better performance in terms of time and space complexity for certain tasks than a list. Each data structure is optimized for specific operations. 
* Reasons by discussing basic operations:
  1. Insertion and Deletion : Insertion or Deletion takes N steps for lists in most cases. But for dictionary the average case of insertion or deletion a key value pair is constant O(1). Hence using a dictionary is much better than list.
  2. Searching : Searching for a unsorted list takes N steps because we have to iterate through each element. But for dictionary searching a key is constant one step.

**4. What is an algorithm?**
* An algorithm is a set of instructions or rules used to solve a problem or perform a task. <br>
  Examples:
  1. Binary Search: An efficient algorithm for finding a target value within a sorted array.
  2. Linear Search: A basic algorithm for finding a target value within an array by sequentially checking each element.

**5. Time complexity of algorithms is measured in terms of steps instead of pure time. Why is that?**
* Time complexity is measured in steps rather than pure time because it helps us understand how the number of operations an algorithm performs grows as the input size increases and the actual execution time of an algorithm can vary depending on hardware.

**6. We compared linear search to binary search. Which searching algorithm is better and why? Answer this answer by first talking about what binary search assumes and the cost of ensuring that assumption. Then compare how many steps it would take linear search to find an element vs binary search.**
* Binary search algorithm efficiently locates a target value within a sorted data by iteratively dividing the search range in half until the target is located.
* Binary search assumes the data is sorted initially can lead to an extra time cost. This is because sorting the data requires a time complexity of NlogN.
* Linear Search algorithm for finding a target value within data by sequentially checking each element.
* Comparing number of steps:
  1. Binary Search takes approximately logN steps to find an element in a sorted list of size N. Because efficiently halves the search space with each iteration, leading to logarithmic time complexity.
  2. Linear search takes approximately N steps to find an element in a list of size N because it sequentially checks each element in the list until the target is found or the end of the list is reached, resulting in linear time complexity.

