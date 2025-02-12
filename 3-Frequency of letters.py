#3. Frequency of letters

print("The most frequent characters in English text are represented with most easy Morse Codes.")
print("Reading norm_hamlet.txt\n")
file_address = r"C:\Users\Tiger\Desktop\norm_hamlet.txt"

def read_file(file_address):
    with open(file_address, 'r') as file:
        text = file.read().lower()
    file.close()
    return text

def count_and_sort_char_freq(text):
    characters="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    char_freq={char: 0 for char in characters}
    num_freq={num: 0 for num in numbers}
    for char in text:
        if char in characters:
            char_freq[char]+=1
        elif char in numbers:
            num_freq[char]+=1
    sorted_char_freq=sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_num_freq=sorted(num_freq.items(),key=lambda x: x[1],reverse=True)
    return sorted_char_freq, sorted_num_freq

text=read_file(file_address)
sorted_char_freq, sorted_num_freq=count_and_sort_char_freq(text)
print("Characters Frequency (from most frequent to least frequent:")
for char, freq in sorted_char_freq:
    print(f"{char}: {freq}")
print("\nNumbers Frequency (from most frequent to least frequent:")
for num, freq in sorted_num_freq:
    print(f"{num}: {freq}")