class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = sorted(nums)
        ans = []

        for i in range(len(n) - 2):

            # skip duplicate first numbers
            if i > 0 and n[i] == n[i - 1]:
                continue

            target = -n[i]

            left = i + 1
            right = len(n) - 1

            while left < right:

                total = n[left] + n[right]

                if total == target:
                    ans.append([n[i], n[left], n[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and n[left] == n[left - 1]:
                        left += 1

                    while left < right and n[right] == n[right + 1]:
                        right -= 1

                elif total > target:
                    right -= 1

                else:
                    left += 1

        return ans