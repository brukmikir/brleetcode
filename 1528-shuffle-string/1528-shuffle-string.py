class Solution(object):

    def restoreString(self, s, indices):
        arr=[0] * len(s)
        for i in range(len(s)):
            arr[indices[i]]=s[i]
        return "".join(arr)