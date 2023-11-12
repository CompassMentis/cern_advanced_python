def greeting(language):
    def say_hello(name):
        print('Hello', name)

    def disez_bonjour(name):
        print('Bonjour', name)

    def zeg_hallo(name):
        print('Hallo', name)

    if language == 'English':
        return say_hello
    if language == 'French':
        return disez_bonjour
    if language == 'Dutch':
        return zeg_hallo


for name, language in [
    ('John', 'English'),
    ('Jacques', 'French'),
    ('Hendrik', 'Dutch')
]:
    function = greeting(language)
    function(name)

# Hello John
# Bonjour Jacques
# Hallo Hendrik
