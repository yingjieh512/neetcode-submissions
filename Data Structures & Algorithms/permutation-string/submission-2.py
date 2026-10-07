class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0

        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            # 窗口太长，就从左边缩
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # 长度相同以后比较 frequency
            if right - left + 1 == len(s1):
                if window == need:
                    return True

        return False