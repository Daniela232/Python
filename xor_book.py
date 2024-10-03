# XOR two files byte by byte and output the result to another file

def xor_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()

    # XOR the content of the two files
    min_length = min(len(content1), len(content2))
    xor_result = bytes([b1 ^ b2 for b1, b2 in zip(content1[:min_length], content2[:min_length])])

    # Save the XOR result to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(xor_result)

    print(f"XOR result has been saved to '{output_file}'.")

# Main function to call the XOR logic
def main():
    file1 = 'Beyond.txt'
    file2 = 'Ethics.txt'
    output_file = 'xor_result.txt'

    # XOR the files and save the result
    xor_files(file1, file2, output_file)

if __name__ == "__main__":
    main()

