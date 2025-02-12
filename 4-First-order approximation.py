#4. First-order approximation
import random

text_length=10000
print("Reading norm_hamlet.txt\n")
file_address=r"C:\Users\Tiger\Desktop\norm_hamlet.txt"

def read_file(file_address):
    with open(file_address,'r') as file:
        text=file.read().lower()
    file.close()
    return text

#Changes to this function: now adding space as a character
def count_and_sort_char_freq(text):
    characters="abcdefghijklmnopqrstuvwxyz "
    numbers="0123456789"
    char_freq={char:0 for char in characters}
    num_freq={num:0 for num in numbers}
    for char in text:
        if char in characters:
            char_freq[char]+=1
        elif char in numbers:
            num_freq[char]+=1
    sorted_char_freq=sorted(char_freq.items(),key=lambda x:x[1],reverse=True)
    sorted_num_freq=sorted(num_freq.items(),key=lambda x:x[1],reverse=True)
    return sorted_char_freq,sorted_num_freq

def generate_first_order_text(sorted_char_freq, text, length):
    chars=[char for char,freq in sorted_char_freq]
    prob=[freq/len(text) for char,freq in sorted_char_freq]
    generated_text=''
    for char in range(length):
        generated_text+=random.choices(chars,weights=prob)[0]
    return generated_text

def get_average_word_length(text):
    words=text.split()
    total_length=sum(len(word) for word in words)
    total_words=len(words)
    if total_words:
        return total_length/total_words
    else:
        return 0

text=read_file(file_address)
sorted_char_freq,sorted_num_freq=count_and_sort_char_freq(text)

#print("Characters Frequency (from most frequent to least frequent:")
#for char, freq in sorted_char_freq:
    #print(f"{char}: {freq}")

generated_text=generate_first_order_text(sorted_char_freq, text, text_length)
avg_text_length=get_average_word_length(generated_text)
print(f"Generated first-order text with text length {text_length}:\n{generated_text}\n")
print(f"Average length of a word: {avg_text_length:.2f}")