import random

vowels = "a","e","i","o","u"
consonants = ["b",'c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def choose_power_consonants():

    power_consonants = ""
    previous_consonant = ""
    for consonant in xrange(0, 6):
        current_consonant = random.choice(consonants)
        while current_consonant == previous_consonant:
            current_consonant = random.choice(consonants)
        power_consonants += current_consonant
        previous_consonant = current_consonant
    return power_consonants


def choose_power_vowels():

    power_vowels = ""
    previous_vowel = ""
    for vowel in xrange(0, 3):
        current_vowel = random.choice(vowels)
        while current_vowel == previous_vowel:
            current_vowel = random.choice(vowels)
        power_vowels += current_vowel
        previous_vowel = current_vowel
    return power_vowels

chosen_vowels = choose_power_vowels()
chosen_consonants = choose_power_consonants()
print chosen_consonants, " ", chosen_vowels


def create_syllable():

    letters_in_syllables = 2
    syllable = ""
    previous_letter = "Con"

    for letters in xrange(0, letters_in_syllables):
        if len(syllable) == 0:
            if random.randint(1, 2) == 1:
                first_letter = random.choice(chosen_consonants)
                syllable += first_letter
                previous_letter = "Con"
            else:
                first_letter = random.choice(chosen_vowels)
                syllable += first_letter
                previous_letter = "Vow"
        if previous_letter == "Vow":
            new_letter = random.choice(chosen_consonants)
            syllable += new_letter
            if random.randint(1, 10) == 10:
                syllable += new_letter
            previous_letter = "Con"
        else:
            new_letter = random.choice(chosen_vowels)
            syllable += new_letter
            previous_letter = "Vow"
    return syllable

def create_syllable_lists():

    vowel_syllables = []
    consonant_syllables = []

    for amount in xrange(0, 20):
        syllable = create_syllable()
        starting_with_vowel_syllable = [w for w in syllable.split() if w[0] in vowels]
        vowel_syllables += starting_with_vowel_syllable
        starting_with_consonant_syllable = [w for w in syllable.split() if w[0] not in vowels]
        consonant_syllables += starting_with_consonant_syllable
    return vowel_syllables, consonant_syllables


def create_simple_word(vowel_syllables, consonant_syllables):

    number_of_syllables = 1
    word = ''

    for syllables in xrange(0, number_of_syllables):
        if random.randint(1, 2) == 1:
            word += random.choice(vowel_syllables)
            word += random.choice(consonant_syllables)
            if random.randint(1, 2) == 1:
                word += random.choice(chosen_vowels)
        else:
            word += random.choice(consonant_syllables)
            word += random.choice(vowel_syllables)
            if random.randint(1, 2) == 1:
                word += random.choice(chosen_consonants)
            else:
                word += "s"
    return word
