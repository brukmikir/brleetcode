class Solution(object):
    def duplicateZeros(self, arr):
        l = 0
        n = len(arr)

        while l < n - 1:
            if arr[l] == 0:
                for i in range(n-1, l+1, -1):
                    arr[i] = arr[i-1]
                arr[l+1] = 0
                l += 2
            else:
                l += 1

        