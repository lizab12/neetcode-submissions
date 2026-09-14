class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        zero_index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                zero_index = i
            else:
                product *= nums[i]

        # More than one zero
        if zeros > 1:
            return [0] * len(nums)

        # Exactly one zero
        if zeros == 1:
            result = [0] * len(nums)
            result[zero_index] = product
            return result

        # No zeros
        result = []

        for num in nums:
            result.append(product // num)

        return result