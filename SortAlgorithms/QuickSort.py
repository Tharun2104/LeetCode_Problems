#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pi = self.partition(arr, low, high)  # Partitioning index
    
            self.quickSort(arr, low, pi - 1)  # Sort left partition
            self.quickSort(arr, pi + 1, high)  # Sort right partition
    def partition(self,arr,low,high):
        # code here
        i = low
        j = high - 1
        pivot = arr[high]
        while(i<=j):
            while(arr[i]<pivot and i<=j):
                i+=1    
            while (arr[j]>pivot and i<=j):
                j-=1
            if(arr[i]>=pivot and arr[j]<pivot and j>=i):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
        arr[high], arr[i] = arr[i], arr[high]
        return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        print("~")

# } Driver Code Ends