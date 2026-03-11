class Solution(object):
    def threeSum(self, nums):
        ans=[]
        nums.sort();
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1;

            while l<r:
                trisum=nums[i]+nums[l]+nums[r];

                if trisum>0:
                    r-=1;
                elif trisum<0:
                    l+=1;
                else:
                    ans.append([nums[i],nums[l],nums[r]]);
                    l+=1;
                    while nums[l]==nums[l-1] and l<r:
                        l+=1;
        return ans;