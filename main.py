from language import choose_power_vowels, choose_power_consonants, create_syllable, create_syllable_lists, create_simple_word

choose_power_vowels()
choose_power_consonants()
create_syllable()
vowel_syllables, consonant_syllables = create_syllable_lists()

words = []
for lots in xrange(0, 20):
    word = create_simple_word(vowel_syllables, consonant_syllables)
    words.append(word)

print vowel_syllables
print consonant_syllables
print words