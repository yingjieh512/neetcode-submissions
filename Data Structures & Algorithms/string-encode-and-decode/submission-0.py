class Solution:
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            j += 1
            res.append(s[j:j + length])

            i = j + length

        return res