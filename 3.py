class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        result = 0
        max_result = 0
        for i in range(len(s)):
            previous_pos = last_seen[s[i]] if s[i] in last_seen else -1
            if previous_pos < i-result:
                result += 1
            else:
                max_result = max(max_result, result)
                result = i-previous_pos
            last_seen[s[i]] = i
        max_result = max(max_result, result)
        return max_result
        
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))