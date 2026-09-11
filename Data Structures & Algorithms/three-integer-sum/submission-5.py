class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        ans = []
        for i in range(len(num) - 2):          # Trick 2!
            if num[i] > 0: break               # Trick 1!
            if i > 0 and num[i] == num[i-1]: continue
            
            l, r = i + 1, len(num) - 1
            while l < r:
                total = num[i] + num[l] + num[r]
                if total == 0:
                    ans.append([num[l], num[r], num[i]])
                    l += 1
                    r -= 1
                    while l < r and num[l] == num[l - 1]:
                        l += 1
                    while l < r and num[r] == num[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans