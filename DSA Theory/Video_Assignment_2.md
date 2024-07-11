# Two-Pointer :
The two-pointer method uses two pointers to navigate through a data structure, typically starting from both ends and moving towards the center. This approach is useful for solving problems that require comparing elements or finding pairs that meet specific criteria.

## 1.  Palindrome Check using Two Pointers

**Palindrome** : A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward<br>
Examples : "MADAM", 12321, "())("

~~~python
def palindrome(str):
    start = 0          # starting pointer which at the start of the string
    end = len(str)-1   # end pointer which starts at the end of the string
    while end>=start:
        if(str[start] == str[end]):   # checking if the first and last value are equal
            start +=1                 # Incrementing
            end -=1                   # decrementing
        else:
            return False              # if not equal returning False
    return True
str = "MADAM"
palindrome(str)

Output : True
~~~

**Explanation** :
   - Start with pointers at both ends.
   - Move pointers towards the center, comparing characters.
   - If all characters match, it's a palindrome.
1. **MADAM:** : start pointer starts at 0 which menans str[0] = "M" and end pointer starts at 4 which means str[4] = "M"
                as both start and end values are same we decrement each by one value and check next elements untill end is qual to start.

2. **()()** : start pointer starts at 0 which menans str[0] = "(" and end pointer starts at 4 which means str[4] = ")"
              here both start and end values are different hence it goes to else and return False. Resulting that string is not a palindrome. This is the best case as we are getting result in first check

3. **)()(** : start pointer starts at 0 which menans str[0] = ")" and end pointer starts at 4 which means str[4] = "("
              here start is closing bracket and end is opening bracket both values are different hence it goes to else and return False. Resulting that string is not a palindrome.

Note : Explained the visual reprsentation in the video


## 2.  Two-Sum Problem : <a href="https://leetcode.com/problems/two-sum/description/">link</a>
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
## Example:
**Input:** `nums = [2, 7, 11, 15]`, `target = 9` <br>
**Output:** `[0, 1]` <br>
**Steps:**
1. Initialize the `left` pointer at index 0 and the `right` pointer at index 3.
2. Calculate the sum: `nums[0] + nums[3] = 2 + 15 = 17`. Since 17 > 9, move the `right` pointer to the left.
3. Calculate the sum: `nums[0] + nums[2] = 2 + 11 = 13`. Since 13 > 9, move the `right` pointer to the left.
4. Calculate the sum: `nums[0] + nums[1] = 2 + 7 = 9`. Since 9 == 9, return `[0, 1]`.

**CODE:**
~~~python
def two_sum(nums, target):
    N = len(nums)
    nums.sort()              # sorting the list inplace
    left_index = 0           # start index
    right_index = N-1        # end index
    while (left_index < right_index):
        left_val = nums[left_index]
        right_val = nums[right_index]
        total = left_val + right_val
        if total == target:       # checking sum is equal to target or not
            return [left_index, right_index]
        elif total > target:
            right_index -= 1     # decrementing the right index 
        elif total < target:
            left_index += 1      # incrementing the left_index

# nums = [1,21,3,14,5,60,7,6]
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
~~~
### Explanation and Main trick:  
To solve the two-sum problem using the two-pointer technique, we must assume the array is sorted. This works because we need to check if the sum of two elements equals the target. If the sum is greater than the target, we decrease the sum by moving the end pointer leftwards, as the array is sorted and this will lead us to a smaller number. Conversely, if the sum is less than the target, we increase the sum by moving the start pointer rightwards. Eventually, we will find the target sum and return the indices of the values. 

### Quick Tips
- Always check for edge cases: empty array, single element array, duplicates.
- For the two-pointer approach, ensure the array is sorted or sort it first.

### Time Complexity
- Sorting the array takes O(n log n).
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n) due to sorting.

Note : Visual reprsentation in powerpoint is explained in the video

## 3. Three sum Problem: <a href = "https://leetcode.com/problems/3sum/description/">link</a>
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

### Example 1
**Input:** `nums = [-1, 0, 1, 2, -1, -4]`<br>
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`<br>
**Explanation:** <br>
- `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`.
- `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`.
- `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`.

The distinct triplets are `[-1, 0, 1]` and `[-1, -1, 2]`. Notice that the order of the output and the order of the triplets does not matter.

### Comparison 2sum vs 3sum : 
The 3sum problem differs from the 2sum problem primarily in complexity and approach. While 2sum involves finding two numbers that add up to a target using two pointers directly, 3sum requires an additional outer loop to fix one element and then uses the two-pointer technique on the remaining elements. This results in a higher time complexity for 3sum (O(n^2)) compared to 2sum, and the array must be sorted first to efficiently apply the two-pointer method.

**CODE:**
~~~python
nums = [-1,0,1,2,-1,-4]

def threeSum(nums, target):
    combinations = []
    nums.sort() # n log n

    N = len(nums)
    for i in range(0, N-2):    # outer for loop here we are fixing a value
        right_p = i + 1        # right index
        left_p = N-1           # left index

        while (right_p < left_p):     # inner loop
            x, y, z = nums[right_p], nums[i], nums[left_p]
            triplet = x + y + z

            if triplet == target:     # checking the sum is equal to zero or not
                combinations.append([x,y,z])
                break
            elif triplet < target:
                right_p += 1          # moving the right pointer 
            elif triplet > target:
                left_p -= 1           # moving the left pointer
    return combinations

print(threeSum(nums, 0))
~~~

### Explanation and Trick:
The provided 3sum code first sorts the array to enable the two-pointer technique. It then iterates through the array, fixing one element and using two pointers to find the other two elements that sum to the target. If the sum of the three elements equals the target, the triplet is added to the result list. If the sum is less than the target, the right pointer is moved to the right; if greater, the left pointer is moved to the left. This process continues until all possible triplets are found.

In 2sum, we directly use two pointers to find two numbers that add up to the target. In 3sum, we need an additional loop to fix one element and then apply the two-pointer technique to find the remaining two numbers.


### Time Complexity

- **Sorting the array:** O(n log n)
- **Two-pointer traversal:** O(n^2) (using nested loop)
- **Overall time complexity:** O(n^2)



## 4. Container With Most Water: <a href = "https://leetcode.com/problems/container-with-most-water/description/">link</a>
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

**Example 1:**<br>
**Input**: `height = [1,8,6,2,5,4,8,3,7]`<br>
**Output**: `49`<br>
**Explanation**: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Demonstrating the Two-Pointer Approach:**<br>
Place one pointer at the start (left) and one at the end (right) of the array.
Show how the width of the container and the height (limited by the shorter line) are used to compute the area.
Move the pointers towards each other based on the height comparison between left and right, demonstrating the logic of maximizing the area.

**CODE:**
~~~python
def maxArea(height):
    height = [1,8,6,2,5,4,8,3,7]
    max_area = 0

    left_index = 0                      # left pointer
    right_index = len(height)-1         # right pointer

    while left_index < right_index:
        width = right_index - left_index   # finding the width to calculate the area
        low_height = min(height[left_index], height[right_index]) # finding the low height to find the area
        area = width * low_height
        if area > max_area:  
            max_area = area       # maximum area 
        if height[left_index] <= height[right_index]:
            left_index += 1     # moving the left pointer if it is the shortest
        else:
            right_index -= 1    # moving the right pointer as if it is the shortest
    return max_area

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
~~~
### Explanation and Trick:
 - Initialize pointers at the start and end.
 - Calculate area with the current pointers and update the maximum area if the current area is larger.
 - Move the pointers based on height if the left_index value is less than right value move the left pointer and vice versa.

**Key difference from 2sum and 3sum:** <br>
The water container problem differs from 2sum and 3sum in that it focuses on maximizing the area between two lines, requiring adjustments based on height and width, rather than finding sums. While 2sum and 3sum use fixed targets and sort or iterate with specific pair or triplet criteria, the water container problem uses a two-pointer approach that adjusts pointers based on the height to maximize area. This adjustment strategy reflects the need to consider both dimensions (height and width) for optimization.

**Key Point:** <br>
The key insight of the two-pointer technique is to maximize the area by starting with the widest possible container and then narrowing the width while trying to increase the height. We always move the pointer that points to the shorter height because the area is determined by the shorter of the two heights. By moving the pointer at the shorter height, we have a chance of finding a taller height that might increase the area.

### Time and Space Complexity: 
The time complexity of the water container problem is O(n) due to the single pass through the array with two pointers. The space complexity is O(1) as it uses only a few extra variables for tracking pointers and maximum area, with no additional data structures needed.


