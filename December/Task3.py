# 3)  Reverse the Order of Words in a Sentence

# Write a function that takes a sentence and reverses the order of its words.

def reverse(sentence):
    return ' '.join(sentence.split()[::-1])


print(reverse( " Spaces "))