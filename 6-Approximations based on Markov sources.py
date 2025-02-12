#6. Approximations based on Markov sources
import random

text_length=10000
print("Reading norm_hamlet.txt\n")
file_address = r"C:\Users\Tiger\Desktop\norm_hamlet.txt"

def read_file(file_address):
    with open(file_address,'r') as file:
        text=file.read().lower()
    file.close()
    return text

def build_markov_model_order_1(text):
    markov_model={}
    for i in range(len(text)-1):
        current_char=text[i]
        next_char=text[i+1]
        if current_char not in markov_model:
            markov_model[current_char]={}
        if next_char not in markov_model[current_char]:
            markov_model[current_char][next_char]=0
        markov_model[current_char][next_char]+=1
    # Convert counts to probabilities
    for char, transitions in markov_model.items():
        total_transitions=sum(transitions.values())
        for next_char in transitions:
            transitions[next_char] /=total_transitions
    return markov_model

def build_markov_model_order_3(text):
    markov_model={}
    for i in range(len(text)-2):
        current_chars=text[i:i+3]
        prefix=current_chars[:-1]
        next_char=current_chars[-1]
        if prefix not in markov_model:
            markov_model[prefix]={}
        if next_char not in markov_model[prefix]:
            markov_model[prefix][next_char]=0
        markov_model[prefix][next_char]+=1
    # Convert counts to probabilities
    for prefix,transitions in markov_model.items():
        total_transitions=sum(transitions.values())
        for next_char in transitions:
            transitions[next_char]/=total_transitions
    return markov_model

def build_markov_model_order_5(text):
    markov_model={}
    for i in range(len(text)-4):
        current_chars=text[i:i + 5]
        prefix=current_chars[:-1]
        next_char=current_chars[-1]
        if prefix not in markov_model:
            markov_model[prefix]={}
        if next_char not in markov_model[prefix]:
            markov_model[prefix][next_char]=0
        markov_model[prefix][next_char]+=1
    # Convert counts to probabilities
    for prefix, transitions in markov_model.items():
        total_transitions=sum(transitions.values())
        for next_char in transitions:
            transitions[next_char] /=total_transitions
    return markov_model

def generate_text(markov_model,seed_chars,length):
    current_chars=seed_chars
    generated_text=current_chars
    order=len(list(markov_model.keys())[0])  # Determine the order from the model
    for _ in range(length):
        prefix=current_chars[-order:]
        if prefix in markov_model:
            next_char=random.choices(
                list(markov_model[prefix].keys()),
                weights=list(markov_model[prefix].values())
            )[0]
            generated_text+=next_char
            current_chars=current_chars[1:]+next_char
        else:
            break
    return generated_text

def get_average_word_length(text):
    words=text.split()
    total_length=sum(len(word) for word in words)
    total_words=len(words)
    if total_words:
        return total_length/total_words
    else:
        return 0

text = read_file(file_address)

markov_model_order_1=build_markov_model_order_1(text)
markov_model_order_3 = build_markov_model_order_3(text)
markov_model_order_5 = build_markov_model_order_5(text)

characters="abcdefghijklmnopqrstuvwxyz"
seed_char_1=random.choice(characters)
seed_chars_3=random.choice(list(markov_model_order_3.keys()))
seed_chars_5="probability"

generated_text_order_1=generate_text(markov_model_order_1, seed_char_1, text_length)
generated_text_order_3=generate_text(markov_model_order_3, seed_chars_3, text_length)
generated_text_order_5 = generate_text(markov_model_order_5, seed_chars_5, text_length)
avg_text_order_1_length=get_average_word_length(generated_text_order_1)
avg_text_order_3_length=get_average_word_length(generated_text_order_3)
avg_text_order_5_length=get_average_word_length(generated_text_order_5)

print(f"Generated first-order Markov source text with text length {text_length}, seed character '{seed_char_1}':\n{generated_text_order_1}\n")
print(f"Average length of a word in first-order Markov source text: {avg_text_order_1_length:.2f}\n")
print(f"Generated third-order Markov source text with text length {text_length}, seed characters '{seed_chars_3}':\n{generated_text_order_3}\n")
print(f"Average length of a word in third-order Markov source text: {avg_text_order_3_length:.2f}\n")
print(f"Generated fifth-order Markov source text with text length {text_length}, seed characters '{seed_chars_5}':\n{generated_text_order_5}\n")
print(f"Average length of a word in fifth-order Markov source text: {avg_text_order_5_length:.2f}\n")