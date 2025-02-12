#Lab 6 Huffman Coding
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def create_huffman_tree(freq_dict):
    priority_queue = []
    for char, freq in freq_dict.items():
        heapq.heappush(priority_queue, Node(char, freq))

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_codes(node, code, codes):
    if node:
        if node.char:
            codes[node.char] = code
        generate_codes(node.left, code + '0', codes)
        generate_codes(node.right, code + '1', codes)

#Creates a code (e.g., as a dictionary from a character to a binary sequence representing it) given a list of frequency of characters.
def create(text):
    char_frequencies = defaultdict(int)
    for char in text:
        char_frequencies[char] += 1

    huffman_tree = create_huffman_tree(char_frequencies)
    codes = {}
    generate_codes(huffman_tree, '', codes)

    print("Binary Codes:")
    for char, code in sorted(codes.items()):
        print(f"{char}: {code}")

    return codes

#Creates encoded representation of the text
def encode(text, codes):
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text

#Decodes encoded text
def decode(encoded_text, codes):
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in codes.values():
            decoded_text += next((char for char, code in codes.items() if code == current_code))
            current_code = ''
    return decoded_text

if __name__ == "__main__":
    text = "This is the original text for Huffman Coding"
    print("Original Text:", text)

    if not text:
        print("Error: Empty input text.")
    else:
        # Create Huffman codes
        codes = create(text)

        # Encode the text
        encoded_text = encode(text, codes)
        print("Encoded Text:", encoded_text)

        # Decode the encoded text
        decoded_text = decode(encoded_text, codes)
        print("Decoded Text:", decoded_text)

        # Calculate bits for comparison
        original_bits = len(text) * 8
        compressed_bits = len(encoded_text)
        print(f"Number of bits in original text: {original_bits}")
        print(f"Number of bits in compressed text: {compressed_bits}")