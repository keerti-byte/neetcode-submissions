class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for num in nums:
            arr[num] = arr.get(num, 0) + 1
        sort = [[] for _ in range(len(nums) + 1)]
        for i, num in arr.items():
            index = arr[i]
            sort[num].append(i)
        result = []
        for i in range(len(sort) - 1, -1, -1):
            if sort[i]:
                result.extend(sort[i])
                if len(result) >= k:
                    return result