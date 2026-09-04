class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)          # O(n) build, O(1) lookup
        longest = 0

        for num in num_set:          # iterate the set, not the original list
            # only start counting at the BEGINNING of a streak
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:   # walk forward in O(1) per step
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest