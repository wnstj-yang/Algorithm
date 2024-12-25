class Solution(object):
    def intToRoman(self, num):
        # 나올 수 있는 값들을 나열하여 만들기
        symbols = [
            [ 'M', 1000],
            ['CM', 900],
            ['D', 500],
            ['CD', 400],
            ['C', 100],
            ['XC', 90],
            ['L', 50],
            ['XL', 40],
            ['X', 10],
            ['IX', 9],
            ['V', 5],
            ['IV', 4],
            ['I', 1],
        ]
        result = ''
        for key, val in symbols:
            div = num // val
            if div:
                result += key * div
                num -= val * div
        return result

        