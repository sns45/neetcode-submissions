class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}

        for i, num in enumerate(nums):
            targetNum = target - num
            if targetNum in targetMap:
                return [targetMap[targetNum], i]
            else:
                targetMap[num] = i
        
        return [-1, -1]