from argparse import ArgumentParser, Namespace
import os
import pyperclip

ar_to_en = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p', 'ج': '[', 'د': ']',
    'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k', 'م': 'l', 'ك': ';', 'ط': '\'', 'ئ': "z",
    'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'ﻻ': 'b', 'ى': 'n', 'ة': 'm', 'و': ',', 'ز': '.', 'ظ': '/', 'ذ': '`',
    'َ': 'Q', 'ً': 'W', 'ُ': 'E', 'ٌ': 'R', 'ﻹ': 'T', 'إ': 'Y', '`': 'U', '÷': 'I', '×': 'O', '؛': 'P', '<': '{', '>': '}',
    'ِ': 'A', 'ٍ': 'S', ']': 'D', '[': 'F', 'ﻷ': 'G', 'أ': 'H', 'ـ': 'J', '،': 'K', '/': 'L', ':': ':', '"': 'Z', '~': 'X',
    'ْ': 'C', '}': 'V', '{': 'B', 'ﻵ': 'N', 'آ': 'M', '\'': '<', ',': '>', '.': '?', '؟': '~', 'ّ': '"'
}

en_to_ar = {v: k for k, v in ar_to_en.items()}

def ar_to_en_func(ar_str: str):
    return ''.join(ar_to_en.get(letter, letter) for letter in ar_str)

def en_to_ar_func(en_str: str):
    return ''.join(en_to_ar.get(letter, letter) for letter in en_str)

def auto_detect_and_convert(text: str):
    if all(char in ar_to_en or not char.isalpha() for char in text):
        return ar_to_en_func(text)
    else:
        return en_to_ar_func(text)

def main():
    parser = ArgumentParser(description="A CLI tool for converting text between Arabic and English keyboard layouts.")
    parser.add_argument('text', help='Text to be converted', type=str, nargs='?')
    parser.add_argument('-v', '--verbose', help='Provides a verbose description', action='store_true')
    parser.add_argument('-f', '--file', help='Path to the input file', type=str)
    parser.add_argument('-o', '--output', help='Path to the output file', type=str)
    parser.add_argument('-r', '--reverse', help='Convert from English to Arabic', action='store_true')
    parser.add_argument('-i', '--interactive', help='Enter interactive mode', action='store_true')
    parser.add_argument('-c', '--clipboard', help='Copy the result to the clipboard', action='store_true')

    args: Namespace = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            input_text = f.read()
    elif args.text:
        input_text = args.text
    elif args.interactive:
        input_text = input("Enter the text to be converted: ")
    else:
        input_text = pyperclip.paste()

    if args.reverse:
        output_text = en_to_ar_func(input_text)
    else:
        output_text = ar_to_en_func(input_text)

    if args.verbose:
        print(f'The conversion of "{input_text}" is "{output_text}"')

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
    else:
        print(output_text)

    if args.clipboard:
        pyperclip.copy(output_text)
        if args.verbose:
            print("Result copied to clipboard.")

if __name__ == '__main__':
    main()
