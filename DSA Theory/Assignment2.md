Time Complexity
===============

We studied some time-complexity patterns. In this analysis exercise, you will explain them.

Question # 1
============

Pattern # 1 -- Constant time
----------------------------

    def func(lst):
        return lst[1]
    

    def func():
      x = 1
      x += 1
      print(x)
    

Explain why each of the the above two functions are constant time and what that means.<br>
  
**Answer:<br>**

Code 1:<br>
~~~python
  def func(lst):
    return lst[1]
~~~

In the above function we are passing input list and we are returning the second value in the list by indexing. Accessing the element one step and returning is another step. So, total of 2 steps by dropping out constants the time complexity of above code is constant 
O(1)

Code 2:
~~~python
def func():
    x = 1
    x += 1
    print(x)
~~~

In the provided code, variable assignment in line 1 accounts for one step, while accessing and updating the variable in line 2 adds three more steps. Similarly, accessing the variable and printing in line 3 involves two steps. Therefore, with a total of six steps, dropping out constants leads to a time complexity of O(1), indicating constant time complexity for the code.

Question # 2
============

Pattern # 2 -- Linear time
--------------------------

    def loop(N):
        count = 0
        for _ in range(N):
            count += 1
        return count
    

    def func(lst):
        # Assume lst is of length N
        lst.insert(0, 10)
    

Explain why each of the above two functions are linear time and what that means.

**Answer:<br>**

Code 1:<br>
~~~python
def loop(N):
    count = 0
    for _ in range(N):
        count += 1
    return count
~~~
In the provided code, variable assignment in line 1 accounts for one step, using a for loop of range(N) it cost N steps and all the variable assignments have cost N in line 2 adds 2N steps. Accessing and updating the variable in line 3 total of 3 steps repeating N times becomes 3N steps. Accessing a variable and returning it in line 4 involves two steps. Therefore, with a total of 1 + 2N + 3N + 2 = 5N + 3 steps, dropping out constants leads to a time complexity of O(N), indicating linear time complexity for the code.

Code 2:
~~~python
def func(lst):
    # Assume lst is of length N
    lst.insert(0, 10)
~~~
In the provided code, we are providing an input of list to a function of length N. We are inserting value 10 at zero index means we are inserting at the beginning of the list. For inserting it takes one step and shifting all the values to right takes N steps. Total of 
N + 1 steps, dropping out constants leads to a time complexity of O(N), indicating linear time complexity for the code.


Question # 3
============

Pattern # 3 -- Quadratic Time
-----------------------------

    def nested_loop(N):
        count = 0
        for _ in range(N):
            for _ in range(N):
                count += 1
        return count
    

    def nested_loop(lst):
        count = 0
        N = len(lst)
        for ele in range(N):
            lst.insert(0, ele)
    

Explain why each of the above two functions are quadratic time and what that means.

**Answer:**

Code 1:
~~~python
def nested_loop(N):
    count = 0
    for _ in range(N):
        for _ in range(N):
            count += 1
    return count
~~~
The provided function nested_loop(N) consists of two nested loops, each iterating N times. In line 1, a variable is initialized, taking one step. In line 2, using a for loop of range(N) it costs N steps and all the variable assignments have cost N total of 2N steps. In line 3, the nested loops increment the variable count by one each time, resulting in a total of 2N iterations for each iteration of the outer loop. Therefore, the total number of steps is proportional to 2N * N. In line 4, Accessing and updating the variable total of 3 steps repeating of N*N times.  Accessing a variable and returning it in line 5 involves two steps. Therefore, with a total of 1 + 2n + 2n^2 + 3n^2 + 2 = 5n^2 + 2n + 1 steps, dropping out constants leads to a time complexity of O(N^2), indicating quadratic time complexity for the code.

Quadratic time complexity means that as the size of the input (N) increases, the time it takes for the function to execute increases quadratically.

Code 2:
~~~python
def nested_loop(lst):
    count = 0
    N = len(lst)
    for ele in range(N):
        lst.insert(0, ele)
~~~
In the above code line 1 a variable is initialized, taking one step. In line 2, finding the length of a list is constant O(1) and assigning total of 2 steps and in line 3 using a for loop of range(N) it cost N steps and all the variable assignments have cost N total of 2N steps. In line 4, we are inserting at the beginning of a list which takes N+1 steps repeating of N times total of N(N+1) times. Therefore, with a total of 1 + 1 + 2N + N^2 + N = N^2 + 3N + 2 steps, dropping out constants leads to a time complexity of  
O(N^2), indicating quadratic time complexity for the code.

Question # 4
============

Pattern # 4 -- Single loop with different step size
---------------------------------------------------

    def loop(N):
        for _ in range(N, 1, k):
            pass
    

What is the time complexity of the above code and why?

**Answer:**

In the above code in line 1 using a for loop range(N, 1, K) is N/K steps(for loop will iterate N/K times) and assigning to a variable is N/K steps total of 2N/k steps. After dropping all the constants the total time complexity of the above code is O(N).

Question # 5
============

Pattern # 5 -- nested loops with different step size
----------------------------------------------------

    def func(N):
        for _ in range(N, 1, 3):
            for _ in range(N, 1, 2):
                pass
    

Explain the time complexity of the above code.

**Answer:**

In the above code in line 1 using a for loop range(N, 1, 3) is N/3 steps(for loop will iterate N/3 times) and assigning to a variable is N/3 steps total of 2N/3 steps. In line 2, nested for loop of range(N, 1, 2) which iterates N/2 times so total of N/2 steps and for variable assignment is N/2 total of N steps. After dropping all the constants the total time complexity of the above code is O(N^2) quadratic.


Question # 6
============

Pattern # 6 -- Log N
--------------------

    def func(N):
        i = 1
        count = 0
        factor = 2
        while (i < N):
            i *= factor
            count += 1
        return count 
    

Explain the time complexity of the above code. What is the give away sign for recognizing this time complexity?

**Answer:**

In the above function which is taking an input of N. In line 1,2,3 variable assignment which takes one step. In line 4, we are checking a condition 0 steps. in Line 5, we are multiplying i with factor and assigning it to i so the i increases exponentially so total of 4 steps repeating every time until condition satisfy and in line 6 incrementing count which takes 3 steps and in line 6 returning count which takes 2 steps.
After dropping all the constants i is increasing in a exponential factor. Hence the time complexity of the above code is O(logN)