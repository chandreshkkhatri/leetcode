from typing import List


class Solution:
    def __init__(self):
        self.morse_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_set = set([])
        for word in words:
            transformed_word = self.transformedWord(word)
            morse_set.add(transformed_word)
        return len(morse_set)


    def transformedWord(self, word):
        t_word = ''
        for char in word:
            index = self.get_index_lowercase(char)
            morse_code = self.morse_array[index]
            print (morse_code)
            t_word = t_word + morse_code
        return t_word

    def get_index_lowercase(self, letter):
        return ord(letter) - ord('a')
    
if __name__ == "__main__":
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))