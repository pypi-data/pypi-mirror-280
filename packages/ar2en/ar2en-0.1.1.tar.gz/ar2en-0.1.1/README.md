# ar2en

A CLI tool for converting text between Arabic and English keyboard layouts.

## Installation

You can install the package using pip:

```sh
pip install ar2en
```

## Usage

### Convert Text Directly

To convert text directly from Arabic to English keyboard layout, use:

```sh
ar2en "ضصث"
```

### Convert Text from Clipboard

To convert text from the clipboard and copy the result back to the clipboard:

```sh
ar2en -c
```

### Convert Text from a File

To convert text from a file and optionally copy the result to the clipboard:

```sh
ar2en -f input.txt -c
```

### Convert Text from English to Arabic

To convert text from English to Arabic keyboard layout:

```sh
ar2en -r "qwerty"
```

### Interactive Mode

To enter interactive mode and type the text to be converted:

```sh
ar2en -i
```

### Verbose Mode

To display detailed information about the conversion:

```sh
ar2en -v "ضصث"
```

### Save Output to a File

To save the converted text to an output file:

```sh
ar2en -f input.txt -o output.txt
```

### Full Help

For a full list of options and usage, use:

```sh
ar2en --help
```

## Examples

### Example 1: Simple Conversion

```sh
ar2en "ضصث"
```

Output:

```
wet
```

### Example 2: Conversion with Verbose Output

```sh
ar2en -v "ضصث"
```

Output:

```
The conversion of "ضصث" is "wet"
```

### Example 3: Conversion from Clipboard

```sh
ar2en -c
```

If the clipboard contains "ضصث", the clipboard will be updated with "wet".

### Example 4: Conversion from File and Save to Another File

```sh
ar2en -f input.txt -o output.txt
```

The content of `input.txt` will be converted and saved to `output.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Author

[gamalthecreator](https://github.com/gamalthecreator)
```
>>>>>>> d23772a (initial commit)
