class Solution:
    def isPalindrome(self, s: str) -> bool:

        stripped_s = ""
        for letter in s:
            if letter.isalnum():
                stripped_s += (letter)

        for i, letter in enumerate(stripped_s):
            #print(stripped_s[i], stripped_s[len(stripped_s) - 1 - i])
            if stripped_s[i].lower() != stripped_s[len(stripped_s) - 1 - i].lower():
                return False

        return True
        