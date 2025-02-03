class SlidingWindow:
    def maximumLenSubstring(self, string: str) -> int:
        if not string:
            return 0

        left, right = 0, 0 # starting pointers
        max_length = 1
        counter = {} # store character counts

        counter[string[0]] = 1

        while right < len(string) -1:
            right += 1

            if string[right] in counter:
                counter[string[right]] += 1
            else:
                counter[string[right]] = 1

            while counter[string[right]] == 3:
                counter[string[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

s = SlidingWindow()
print(s.maximumLenSubstring("aabbaaa")) # 4


            