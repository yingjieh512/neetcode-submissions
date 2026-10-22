class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        res = 1

        for right in range(1, len(arr)):

            if arr[right] == arr[right - 1]:
                left = right

            elif right >= 2:
                if (arr[right-2] < arr[right-1] < arr[right] or
                    arr[right-2] > arr[right-1] > arr[right]):
                    left = right - 1

            res = max(res, right - left + 1)

        return res