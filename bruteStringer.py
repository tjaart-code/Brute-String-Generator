#!/usr/bin/env python3
import sys

# Symnium-8609 (2024) - bruteStringer.py
# First posted on HBH (https://hbh.sh/home)

########################################################################################
# Brute String Generator
# Start it with python3 bruteStringer.py 4 6 "abcdefghijklmnopqrstuvwxyz1234567890" "" output.txt
# This will produce all strings with length 4 to 6 using characters from a to z and numbers 0 to 9.
# The generated strings will be saved to output.txt.
# You need to edit these settings to fit your needs.
#
# Examples:
# 1. When the prefix is known, use it as the 4th parameter.
#    If you know the password is "MyPass***" and the *** are some numbers, call it with:
#    python3 bruteStringer.py 3 3 "1234567890" "MyPass" mypass_results.txt
#
# 2. python3 bruteStringer.py 2 3 "ab" ""
#    This will generate and save:
#    aa
#	 ab
#	 ba
#	 bb
#	 aaa
#	 aab
#	 aba
#	 abb
#	 baa
#	 bab
#	 bba
#	 bbb

########################################################################################

def rec(w, b, p, charset, file_handle):
    for c in charset:
        if b < w - 1:
            rec(w, b + 1, p + c, charset, file_handle)
        else:
            generated_string = p + c
            file_handle.write(generated_string + '\n')
            # Optional: Print progress (e.g., every 1000 strings)
            # if count % 1000 == 0:
            #     print(f"{count} strings generated...", end='\r')

def main():
    # Check for minimum required arguments
    if len(sys.argv) < 5:
        print("Usage: ./bruteStringer.py min_length max_length charset prefix [output_file]")
        sys.exit(1)
    
    try:
        min_length = int(sys.argv[1])
        max_length = int(sys.argv[2])
    except ValueError:
        print("Error: min_length and max_length should be integers.")
        sys.exit(1)
    
    if min_length <= 0 or max_length < min_length:
        print("Error: Ensure that min_length > 0 and max_length >= min_length.")
        sys.exit(1)
    
    charset = sys.argv[3]
    prefix = sys.argv[4]
    
    # Determine output file name
    if len(sys.argv) >= 6:
        output_file = sys.argv[5]
    else:
        output_file = "output.txt"
    
    try:
        with open(output_file, 'w') as file_handle:
            print(f"Generating strings from length {min_length} to {max_length}...")
            print(f"Using charset: {charset}")
            print(f"Prefix: '{prefix}'")
            print(f"Output will be saved to: {output_file}")
            print("Generation started...")
            
            for length in range(min_length, max_length + 1):
                rec(length, 0, prefix, charset, file_handle)
            
            print("Generation completed successfully.")
    except IOError as e:
        print(f"Error: Unable to write to file '{output_file}'. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
