class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isalnum():
                t += i
        news = t.lower().replace(" ", "")
        news_reversed = news[::-1]
        if news == news_reversed:
            return True
        else:
            return False