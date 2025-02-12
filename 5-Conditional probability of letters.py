#5. Conditional probability of letters
#Step 1: Find the positions of the most two frequent characters in the text.
#Step 2: Extract all characters occurring immediately after these positions.
#Step 3: Calculate the conditional probability of each character occurring after this character.

print("Reading norm_hamlet.txt\n")
file_address=r"C:\Users\Tiger\Desktop\norm_hamlet.txt"

def read_file(file_address):
    with open(file_address,'r') as file:
        text=file.read().lower()
    file.close()
    return text

def count_and_sort_char_freq(text):
    characters="abcdefghijklmnopqrstuvwxyz"
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

text=read_file(file_address)
sorted_char_freq,sorted_num_freq=count_and_sort_char_freq(text)

characters="abcdefghijklmnopqrstuvwxyz"
# Extracting the two most frequent characters
most_freq_chars = [char[0] for char in sorted_char_freq[:2]] #['e', 't']
# Find positions of most frequent characters in the text
positions=[pos for pos, char in enumerate(text) if char in most_freq_chars]
# Dictionary to store counts of characters occurring after 'e' and 't'
conditional_prob={char: {sub_char: 0 for sub_char in characters} for char in most_freq_chars}
# Calculate counts of characters occurring after 'e' and 't'
for pos in positions:
    if pos+1<len(text) and text[pos] in most_freq_chars and text[pos+1] in characters:
        conditional_prob[text[pos]][text[pos+1]]+=1
# Calculate conditional probability for each character occurring after 'e' and 't'
for char in most_freq_chars:
    total_count = sum(conditional_prob[char].values())
    print(f"\nConditional probabilities after '{char}':")
    for sub_char, count in conditional_prob[char].items():
        probability = count / total_count if total_count > 0 else 0
        print(f"Probability of '{sub_char}' after '{char}': {probability:.4f}")