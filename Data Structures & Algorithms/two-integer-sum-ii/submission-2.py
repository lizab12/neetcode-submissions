class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) -1
        si = -1
        def binS(s,i,j,index):
            while i<=j:
                mid = (i+j)//2
                if numbers[mid]>s:
                    j = mid - 1
                elif numbers[mid]<s:
                    i = mid +1
                else:
                    return mid
            return -1
        for i in range(len(numbers)):
            search = target - numbers[i]
            si = binS(search, i+1, end, -1)
            if(si>0):
                return [i+1,si+1]
        return [-1,-1]

        