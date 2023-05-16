from translate import Translator

translator = Translator(to_lang="ja") #converts text to Japanese, please reference: https://en.wikipedia.org/wiki/ISO_639-1
try:
    with open('../input-file.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('../output-file.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your filepath!')
