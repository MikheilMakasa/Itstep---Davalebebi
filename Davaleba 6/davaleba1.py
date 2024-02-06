def anagram_checker(word1, word2):
    word1 = word1.lower()
    word2= word2.lower()

    return sorted(word1) == sorted(word2)


word1 = "თივა"
word2 = "თავი"

if anagram_checker(word1, word2):
    print(f"{word1} და {word2} ანაგრამებია.")
else:
    print(f"{word1} და {word2} არაა ანაგრამები.")