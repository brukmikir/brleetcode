class Solution(object):
    def findRestaurant(self, list1, list2):
        res=[]
        mini=float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if (i+j < mini):
                        res = [list1[i]]
                        mini=i+j
                    elif (i+j == mini):
                        res.append(list1[i])              
        return res 
