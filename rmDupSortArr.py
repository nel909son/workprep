class Solution:
    def removeDuplicates(self, nums: []) -> int:
        #if list is empty
        if len(nums) == 0:
         return 0
        #store previous unique index
        previous = nums[0]
        #store index location bcz index 0 is unique already
        index = 1
        #loop through list after index 0
        for i in range(1,len(nums)):
            #if current value is same as previous this wont run
            if nums[i] != previous:
                #the previous most current unique value is now.. 
                previous = nums[i]
                #we know where to place this new unique value by using index
                nums[index] = nums[i]
                #now to move place for next unique value to live
                index+=1
        print(nums)
        print(index) 
        return index

  
    def rotate(self, nums: List[int], k: int) -> None:
        ##Input: nums = [1,2,3,4,5,6,7], k = 3
        ##Output: [5,6,7,1,2,3,4]
        pass


        
        
    


s = Solution()

s.removeDuplicates([0,1,1,1,2,2,3,3,4])