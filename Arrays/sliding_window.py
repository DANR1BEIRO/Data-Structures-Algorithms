# maximum length substring with two occurrences.

class SlidingWindow:
    def maximum_length_substring(self, string: str) -> int:
        left, right = 0, 0
        maximum_length = 1
        counter = {}

        counter[string[right]] = 1
        
        while right < len(string) -1:
            right += 1
            if string[right] in counter:
                counter[string[right]] += 1
            else:
                counter[string[right]] = 1
            
            while counter[string[right]] == 3:
                counter[string[left]] -= 1
                left += 1
                
            maximum_length = max(maximum_length, right - left + 1)
        return maximum_length
    

substring = SlidingWindow()
print(substring.maximum_length_substring("bcbbbcba"))
         

                
     