# Create a function to check if two strings are anagrams.

def anagrams(word1, word2):
    return "It's an anagram." if sorted(word1) == sorted(word2) else "It's not an anagram."

word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()

print(anagrams(word1, word2))
