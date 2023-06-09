class Solution:
    def isPalindrome(self, x: int) -> bool:
        wordlist = list(str(x)) 
        reverselist = wordlist[::-1]
        
        return wordlist == reverselist
    
solution = Solution()
input_number = 12321
result = solution.isPalindrome(input_number)
print(result) 