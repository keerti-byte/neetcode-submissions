class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # 1. Remove duplicates and sort
        nums_sort = sorted(set(nums))
        
        longest = 1
        current_streak = 1
        
        # 2. Start at index 1 and compare to the previous number
        for i in range(1, len(nums_sort)):
            # If the current number is exactly +1 from the previous...
            if nums_sort[i] == nums_sort[i-1] + 1:
                current_streak += 1
            else:
                # The streak is broken! Reset current_streak to 1
                current_streak = 1
            
            # Update the longest streak we've seen so far
            longest = max(longest, current_streak)
            
        return longest