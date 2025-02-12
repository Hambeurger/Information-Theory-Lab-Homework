#1. Preparation

#print("Reading norm_hamlet.txt\n")
#file_address = r"C:\Users\Tiger\Desktop\norm_hamlet.txt"

print("Reading norm_romeo_and_juliet.txt\n")
file_address = r"C:\Users\Tiger\Desktop\norm_romeo_and_juliet.txt"

#print("norm_wiki_sample.txt\n")
#file_address = r"C:\Users\Tiger\Desktop\norm_wiki_sample.txt"

def read_file(file_address):
    with open(file_address, 'r') as file:
        text = file.read().lower()
    file.close()
    return text

text = read_file(file_address)
print(f"The text is:\n{text}")