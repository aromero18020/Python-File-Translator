# Python-File-Translator
This code snippet demonstrates the usage of the `translate` library to translate text from one language to another, specifically from English to Japanese. It reads the input text from a file, translates it using the `Translator` class, and writes the translated text to an output file.

## Prerequisites

Before running this code, ensure that you have the following:

- Python installed on your system (version 3 or higher).
- The `translate` library installed. You can install it using the following command: pip install translate

### You can refer to the ISO 639-1 language codes for other language options: https://en.wikipedia.org/wiki/ISO_639-1

## Notes
 - Make sure to provide the correct filepath for the input file. Adjust the file path (../input-file.txt) as necessary to match the actual location of your input file.
 - The translated text will be written to the output file (output-file.txt) in UTF-8 encoding.
 - You can modify the code to translate text to a different target language by changing the to_lang parameter when creating the Translator object.
