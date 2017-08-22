from language import choose_power_vowels,\
    choose_power_consonants,\
    create_syllable_lists,\
    create_simple_word, \
    choose_language_flavour

language_flavour, vowels, consonants = choose_language_flavour()
power_vowels = choose_power_vowels(vowels)
power_consonants = choose_power_consonants(consonants)
vowel_syllables, consonant_syllables = create_syllable_lists(power_vowels, power_consonants, language_flavour, vowels, consonants)

words = []
for lots in xrange(0, 20):
    word = create_simple_word(power_vowels, power_consonants, language_flavour, vowels, consonants)
    words.append(word)

print vowel_syllables
print""
print consonant_syllables
print""
print words
print""
print 'The Village of', words[1], 'is nearby the', words[3], 'river'
print 'local custom is celebrate the ritual of', words[10], words[9]
print "around the time of the local harvest's"
