# 2) Count the Number of Unique Words in a Text

# Write a function that counts the number of unique words in a string, ignoring case sensitivity and punctuation.


def counting(sentence):
    if sentence == '':
        return 0
    else:
        return len(set(sentence.lower().split()))


print(counting("One word"))