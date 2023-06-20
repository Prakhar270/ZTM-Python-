from translate import Translator

translator = Translator(to_lang = 'ja')

#my_file = open('languages.txt', 'r')
#print(my_file.read())
try:
    with open(r'F:\extra work\ZTM(PYTHON)\working_with_file\languages.txt', mode =  'r') as my_file:
        value = my_file.read()
        out = translator.translate(value)
        print(out)
        with open(r'F:\extra work\ZTM(PYTHON)\working_with_file\text-jap.txt', mode = 'w') as my_file2:
            my_file2.write(out)
except FileNotFoundError as e:
    print("You enter wrong file")