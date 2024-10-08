#!/usr/bin/env python3
import sys
import argparse

def generate_combinations(length, current_depth, prefix, charset, file_handle):
    """
    Recursively generates all combinations of strings of a specified length
    using the provided charset and writes them to the file.
    """
    for char in charset:
        if current_depth < length - 1:
            # Continue building the string
            generate_combinations(length, current_depth + 1, prefix + char, charset, file_handle)
        else:
            # Write the completed string to the file
            file_handle.write(prefix + char + '\n')


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Brute-force string generator.")
    parser.add_argument('min_length', type=int, help="Minimum length of the generated strings.")
    parser.add_argument('max_length', type=int, help="Maximum length of the generated strings.")
    parser.add_argument('charset', type=str, help="Character set to use for string generation.")
    parser.add_argument('prefix', type=str, help="Prefix to prepend to all generated strings.")
    parser.add_argument('output_file', nargs='?', default='output.txt', help="Output file to store generated strings. Defaults to 'output.txt'.")

    args = parser.parse_args()

    # Validate min_length and max_length
    if args.min_length <= 0 or args.max_length < args.min_length:
        print("Error: Ensure that min_length > 0 and max_length >= min_length.")
        sys.exit(1)

    # Begin the string generation process
    try:
        with open(args.output_file, 'w') as file_handle:
            print(f"Generating strings of length {args.min_length} to {args.max_length}...")
            print(f"Using charset: {args.charset}")
            print(f"Prefix: '{args.prefix}'")
            print(f"Output will be saved to: {args.output_file}")
            print("Generation started...")

            for length in range(args.min_length, args.max_length + 1):
                generate_combinations(length, 0, args.prefix, args.charset, file_handle)

            print("Generation completed successfully.")
    except IOError as e:
        print(f"Error: Unable to write to file '{args.output_file}'. {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
