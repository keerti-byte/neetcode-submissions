class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        right_product = 1
        left_product = 1
        for i in range(len(nums)):
            res.append(left_product)
            left_product = left_product * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right_product
            right_product = right_product * nums[i]
        return res