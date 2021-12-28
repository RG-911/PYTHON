def pal(word):
    lower = word.lower()
    word_rev = lower[::-1]
    if lower == word_rev:
        return "This is word is palindrome: " + word_rev.upper()
    elif lower != word_rev:
        for i in range(len(word)):
            if lower[0: len(word) - i] == lower[0: len(word) - i][::-1]:
                palindrome = word_rev[0: i] + word[0: len(word) - i] + word[len(word) - i:]
                return "This word is palindrome of the orginal word: " + palindrome.upper()


S = "Georg"
print(pal(S))