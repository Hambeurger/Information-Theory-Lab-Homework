#Lab 4: Conditional entropy of natural languages

import math
import matplotlib.pyplot as plt

file_addresses_natural_language= {
    "English": r"C:\Users\Tiger\Desktop\norm_wiki_en.txt",
    "Latin": r"C:\Users\Tiger\Desktop\norm_wiki_la.txt",
    "Esperanto": r"C:\Users\Tiger\Desktop\norm_wiki_eo.txt",
    "Estonian": r"C:\Users\Tiger\Desktop\norm_wiki_et.txt",
    "Somali": r"C:\Users\Tiger\Desktop\norm_wiki_so.txt",
    "Haitian": r"C:\Users\Tiger\Desktop\norm_wiki_ht.txt",
    "Navaho": r"C:\Users\Tiger\Desktop\norm_wiki_nv.txt"
}

file_addresses_sample={
    "Sample0": r"C:\Users\Tiger\Desktop\sample0.txt",
    "Sample1": r"C:\Users\Tiger\Desktop\sample1.txt",
    "Sample2": r"C:\Users\Tiger\Desktop\sample2.txt",
    "Sample3": r"C:\Users\Tiger\Desktop\sample3.txt",
    "Sample4": r"C:\Users\Tiger\Desktop\sample4.txt",
    "Sample5": r"C:\Users\Tiger\Desktop\sample5.txt",
}

def read_file(file_address):
    with open(file_address, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text

def calculate_entropy(data):
    probabilities = [float(data.count(c)) / len(data) for c in set(data)]
    entropy = - sum(p * math.log2(p) for p in probabilities)
    return entropy

def calculate_word_entropy(words):
    word_dict = {}
    total_words = len(words)
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    probabilities = [count / total_words for count in word_dict.values()]
    word_entropy = - sum(p * math.log2(p) for p in probabilities)
    return word_entropy

def calculate_conditional_entropy(data, order):
    sequences = {}
    for i in range(len(data) - order):
        sequence = data[i:i + order + 1]
        if sequence[:-1] not in sequences:
            sequences[sequence[:-1]] = []
        sequences[sequence[:-1]].append(sequence[-1])

    total_conditional_entropy = 0
    for sequence, next_chars in sequences.items():
        probabilities = [float(next_chars.count(c)) / len(next_chars) for c in set(next_chars)]
        conditional_entropy = - sum(p * math.log2(p) for p in probabilities)
        total_conditional_entropy += conditional_entropy

    return total_conditional_entropy / len(sequences)

print("Choose a natural language file:")
for name in file_addresses_natural_language.keys():
    print(f"{name}")
file_name_natural_language=input("Enter the name of the file: ")
file_address_natural_language = file_addresses_natural_language[file_name_natural_language]

print("Choose a sample language file:")
for name in file_addresses_sample.keys():
    print(f"{name}")
file_name_sample=input("Enter the name of the file: ")
file_address_sample = file_addresses_sample[file_name_sample]

text_natural_language = read_file(file_address_natural_language)
text_sample = read_file(file_address_sample)

# Character Entropy
char_entropy = calculate_entropy(text_natural_language)
print(f"Character entropy of text in {file_name_natural_language} is: {char_entropy:.4f}")

# Word Entropy
words = text_natural_language.split()
word_entropy = calculate_word_entropy(words)
print(f"Word entropy of text in {file_name_natural_language} is: {word_entropy:.4f}")

# Conditional Entropy for Order 0 to 3
orders = list(range(0, 4))

print("Calculating entropies, please wait...")
conditional_entropies_natural = [calculate_conditional_entropy(text_natural_language, order) for order in orders]
print(f"Conditional Entropy (0nd Order) in {file_name_natural_language} is: {conditional_entropies_natural[0]:.4f}")
print(f"Conditional Entropy (1nd Order) in {file_name_natural_language} is: {conditional_entropies_natural[1]:.4f}")
print(f"Conditional Entropy (2nd Order) in {file_name_natural_language} is: {conditional_entropies_natural[2]:.4f}")
print(f"Conditional Entropy (3nd Order) in {file_name_natural_language} is: {conditional_entropies_natural[3]:.4f}")

print("Calculating entropies, please wait...")
conditional_entropies_sample = [calculate_conditional_entropy(text_sample, order) for order in orders]
print(f"Conditional Entropy (0nd Order) in {file_name_sample} is: {conditional_entropies_sample[0]:.4f}")
print(f"Conditional Entropy (1nd Order) in {file_name_sample} is: {conditional_entropies_sample[1]:.4f}")
print(f"Conditional Entropy (2nd Order) in {file_name_sample} is: {conditional_entropies_sample[2]:.4f}")
print(f"Conditional Entropy (3nd Order) in {file_name_sample} is: {conditional_entropies_sample[3]:.4f}")

print("Generating the plot.")
plt.plot(orders, conditional_entropies_natural, marker='o', label=file_name_natural_language)
plt.plot(orders, conditional_entropies_sample, marker='o', label=file_name_sample)
plt.title('Conditional Entropy for Different Orders')
plt.xlabel('Conditional Entropy Order')
plt.ylabel('Conditional Entropy')
plt.xticks(orders)
plt.legend()
plt.grid(True)
plt.show()