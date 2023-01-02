#method-1
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        elif word==word.lower():
            return True
        elif word[1:]==word[1:].lower() and word[0]==word[0].upper():
            return True
        else:
            return False
          
  #method-2
  class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        elif word==word.lower():
            return True
        elif word==word.capitalize():
            return True
        else:
            return False
