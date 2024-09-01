# Solution 1 - Brute Force
def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False

# Solution 2 - Sorting
def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False

# Soluton 3 - Set Approach
def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for ele in nums:
            if ele in seen:
                return True
            
            seen.add(ele)
        
        return False