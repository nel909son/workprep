class Solution:
    def removeDuplicates(self, nums: []) -> int:
        if len(nums) == 0:
         return 0
        length = 1
        previous = nums[0]
        index = 1
        for i in range(1,len(nums)):
            if nums[i] != previous:
                length += 1
                previous = nums[i]
                nums[index] = nums[i]
                index+=1
        print(length) 
        return length
        
    


s = Solution()

s.removeDuplicates([1,1,2])