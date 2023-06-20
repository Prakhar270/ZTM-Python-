import pyjokes

jokes = pyjokes.get_jokes(language= 'en', category= 'neutral')

print(jokes)