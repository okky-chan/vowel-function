def printVowel(sentence):
    for vowel in 'aeiou':
        if vowel in sentence:
            print(vowel)

sentence = input('Enter your sentence: ')

printVowel(sentence)