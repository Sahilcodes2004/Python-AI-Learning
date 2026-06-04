def talk(phrase):
    def say(word):
        print(word)
    words=phrase.split(' ')
    for word in words:
        say(word)

talk("hello we are doings th python coding")