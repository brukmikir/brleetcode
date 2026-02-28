class Solution(object):
    def pancakeSort(self, arr):
        res = []

        for last in range(len(arr), 1, -1):
            max_i = 0
            for i in range(1, last):
                if arr[i] > arr[max_i]:
                    max_i = i

            if max_i != last - 1:
                if max_i != 0:
                    arr[:max_i + 1] = arr[:max_i + 1][::-1]
                    res.append(max_i + 1)

                arr[:last] = arr[:last][::-1]
                res.append(last)

        return res
        
        