class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        maxIndex = len(nums) - 1
        start = 0
        end = maxIndex
        while start <= end:
            middle = (end+start)//2
            print(middle)
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                if middle+1 > maxIndex:
                    return maxIndex+1
                if nums[middle+1] > target:
                    return middle+1
                start = middle+1
            elif nums[middle] > target:
                if middle-1 < 0:
                    return 0
                if nums[middle-1] < target:
                    return middle
                end = middle - 1
