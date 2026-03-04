class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        res=[]
        for p2 in range(len(arr2)):
            for p1 in range(len(arr1)):
                if (arr1[p1]==arr2[p2]):
                    res.append(arr1[p1])
        remain=[]
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                remain.append(arr1[i])
        remain.sort()
        res.extend(remain)
        return res
                
                
            


        
        
        

        
        