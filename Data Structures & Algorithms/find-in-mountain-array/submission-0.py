class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def findPeak():
            left, right = 0, mountainArr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binarySearch(left, right, target, asc=True):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                if asc:
                    if val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if val < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        peak = findPeak()
        leftRes = binarySearch(0, peak, target, True)
        if leftRes != -1:
            return leftRes
        return binarySearch(peak + 1, mountainArr.length() - 1, target, False)
