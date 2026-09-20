class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)

        find1 = total // 2
        find2 = total // 2 - 1

        l1 = 0
        l2 = 0
        c = 0

        res1 = 0
        res2 = 0

        while l1 < len(nums1) or l2 < len(nums2):

            if l1 >= len(nums1):
                value = nums2[l2]
                l2 += 1

            elif l2 >= len(nums2):
                value = nums1[l1]
                l1 += 1

            elif nums1[l1] <= nums2[l2]:
                value = nums1[l1]
                l1 += 1

            else:
                value = nums2[l2]
                l2 += 1

            if c == find2:
                res2 = value

            if c == find1:
                res1 = value
                break

            c += 1

        if total % 2 == 1:
            return res1

        return (res1 + res2) / 2