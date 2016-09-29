class Solution(object):
    def twosum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=len(nums)
        for i in range(count-1):
            for j in range(i+1,count):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return None


nums=[2,7,11,15]
sol=Solution()
print(sol.twosum(nums,27))


