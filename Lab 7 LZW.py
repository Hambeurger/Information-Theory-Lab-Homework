#Lab 7 LZW
def compress(uncompressed):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_sequence = ''

    for symbol in uncompressed:
        extended_sequence = current_sequence + symbol
        if extended_sequence in dictionary:
            current_sequence = extended_sequence
        else:
            result.append(dictionary[current_sequence])
            dictionary[extended_sequence] = next_code
            next_code += 1
            current_sequence = symbol

    if current_sequence:
        result.append(dictionary[current_sequence])

    return result


def decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = [chr(compressed[0])]
    previous_sequence = chr(compressed[0])

    for code in compressed[1:]:
        if code in dictionary:
            sequence = dictionary[code]
        elif code == next_code:
            sequence = previous_sequence + previous_sequence[0]
        else:
            raise ValueError('Bad compressed sequence')

        result.append(sequence)
        dictionary[next_code] = previous_sequence + sequence[0]
        next_code += 1
        previous_sequence = sequence

    return ''.join(result)


if __name__ == "__main__":
    # Test on text files
    with open("norm_wiki_sample.txt", "r") as file:
        original_text = file.read()

    compressed_text = compress(original_text)
    print("Compressed:", compressed_text)

    decompressed_text = decompress(compressed_text)
    print("Decompressed:", decompressed_text)

    #Test on image file (lena.bmp)
    with open("lena.bmp", "rb") as file:
        original_image = file.read()

    compressed_image = compress(original_image)
    print("Compressed Image:", compressed_image)

    decompressed_image = decompress(compressed_image)
    print("Decompressed Image Length:", len(decompressed_image))