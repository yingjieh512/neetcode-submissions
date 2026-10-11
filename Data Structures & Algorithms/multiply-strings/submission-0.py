class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)

        digits = "0123456789"

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                a = digits.index(num1[i])
                b = digits.index(num2[j])

                total = a * b + res[i + j + 1]

                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        result = ""
        started = False

        for x in res:
            if x != 0:
                started = True

            if started:
                result += digits[x]

        return result