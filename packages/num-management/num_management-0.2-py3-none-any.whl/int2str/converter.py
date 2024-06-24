class NumberToWords:
    _units = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    _teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    _tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    _thousands = [
        "", "thousand", "million", "billion"
    ]

    @classmethod
    def convert(cls, n):
        #for n 0
        if n == 0:
            return "zero"
        #for n negative
        if n < 0:
            return "negative " + cls.convert(-n)

        words_data = []
        for idx, parts in enumerate(cls._split_thousands(n)):
            if parts:
                words_data.append(cls._parts_convert_to_words(parts) + cls._thousands[idx])

        return ' '.join(reversed(words_data)).strip()

    @classmethod
    def _split_thousands(cls, n):
        parts = []
        while n > 0:
            parts.append(n % 1000)
            n //= 1000
        return parts

    @classmethod
    def _parts_convert_to_words(cls, n):
        words_data = []
        hundreds, remainder = divmod(n, 100)
        tens, units = divmod(remainder, 10)

        if hundreds:
            words_data.append(cls._units[hundreds])
            words_data.append("hundred")

        if tens >= 2:
            words_data.append(cls._tens[tens])
            if units:
                words_data.append(cls._units[units])
        elif tens == 1:
            words_data.append(cls._teens[units])
        elif units:
            words_data.append(cls._units[units])

        return ' '.join(words_data) + " "