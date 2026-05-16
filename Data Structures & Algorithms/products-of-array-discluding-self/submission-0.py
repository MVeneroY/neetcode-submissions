import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for index, num in enumerate(nums):
            pre = nums[:index]
            suf = nums[index+1:]
            products.append(math.prod(pre) * math.prod(suf))

        return products

