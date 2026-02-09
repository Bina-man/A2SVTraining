class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strings = len(strs)
        first_string_element = strs[0]
        result = ""

        for s in range(len(first_string_element)):
            c = 1
            string_to_check = first_string_element[s]

            while c < strings:
                # check string length before accessing index
                if s >= len(strs[c]) or string_to_check != strs[c][s]:
                    return result
                c += 1

            result += string_to_check

        return result
