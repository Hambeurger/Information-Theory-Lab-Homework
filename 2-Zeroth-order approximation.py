#2. Zeroth-order approximation

import random

text_length=10000

def generate_zeroth_order_text(length):
    characters="abcdefghijklmnopqrstuvwxyz "
    generated_text="".join(random.choice(characters) for i in range(length))
    return generated_text

def get_average_word_length(text):
    words=text.split()
    total_length=sum(len(word) for word in words)
    total_words=len(words)
    if total_words:
        return total_length/total_words
    else:
        return 0

text= generate_zeroth_order_text(text_length)
avg_text_length=get_average_word_length(text)

print(f"Generated zeroth-order text with text length {text_length}:\n{text}\n")
print(f"Average length of a word: {avg_text_length:.2f}")