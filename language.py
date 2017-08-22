import random

random.seed(231423)

def choose_language_flavour():
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    LANGUAGE_FLAVOURS = {
        "random": [9, 9, 20, 1, []],
        "rickandmorty": [10, 10, 20, 20, ['k', 'g', 'r', 'p']]
    }

    language_flavour = LANGUAGE_FLAVOURS["random"]

    return language_flavour, vowels, consonants


def choose_power_consonants(consonants):  # power letters are common in the language and tend to define it.

    power_consonants = ""
    previous_consonant = ""
    for consonant in xrange(0, 3):
        current_consonant = random.choice(consonants)
        while current_consonant == previous_consonant:
            current_consonant = random.choice(consonants)
        power_consonants += current_consonant
        previous_consonant = current_consonant
    return power_consonants


def choose_power_vowels(vowels):

    power_vowels = ""
    previous_vowel = ""
    for vowel in xrange(0, 3):
        current_vowel = random.choice(vowels)
        while current_vowel == previous_vowel:
            current_vowel = random.choice(vowels)
        power_vowels += current_vowel
        previous_vowel = current_vowel
    return power_vowels


def create_syllable(chosen_vowels, chosen_consonants, language_flavour, vowels, consonants):

    chance_of_double_consonant = language_flavour[0]
    chance_of_double_vowel = language_flavour[1]
    chance_of_unexpected_consonant = language_flavour[2]
    chance_of_unexpected_vowel = language_flavour[3]
    letters_in_syllables = 2
    syllable = ""
    previous_letter = "Con"
    remove_bad_cons_doubles = ['h']
    remove_bad_vowel_doubles = ['u', 'a']

    for letters in xrange(0, letters_in_syllables):
        if len(syllable) == 0:  # Choose a consonant or vowel as first letter
            if random.randint(1, 2) == 1:
                first_letter = random.choice(chosen_consonants)
                syllable += first_letter
                previous_letter = "Con"
            else:
                first_letter = random.choice(chosen_vowels)
                syllable += first_letter
                previous_letter = "Vow"

        if previous_letter == "Vow":  # if vowel used, use consonant this time
            if random.randint(0, chance_of_unexpected_consonant) == chance_of_unexpected_consonant:
                # occasionally add an non power letter to the syllable
                new_letter = random.choice(consonants)
            else:
                new_letter = random.choice(chosen_consonants)  # add power letter
            syllable += new_letter
            if random.randint(0, chance_of_double_consonant) == chance_of_double_consonant:
                # occasionally add a double letter to the syllable
                if new_letter not in remove_bad_vowel_doubles:
                    syllable += new_letter
            previous_letter = "Con"

        else:  # if consonant used, use vowel this time
            if random.randint(0, chance_of_unexpected_vowel) == chance_of_unexpected_vowel:
                new_letter = random.choice(vowels)
            else:
                new_letter = random.choice(chosen_vowels)
            syllable += new_letter
            if random.randint(0, chance_of_double_vowel) == chance_of_double_vowel:
                # Occasionally add a double letter to the syllable
                if new_letter not in remove_bad_cons_doubles:  # remove bad sounding doubles
                    syllable += new_letter
            previous_letter = "Vow"

    return syllable


def create_syllable_lists(chosen_vowels, chosen_consonants, language_flavour, vowels, consonants):

    vowel_syllables = []
    consonant_syllables = []

    for amount in xrange(0, 30):
        syllable = create_syllable(chosen_vowels, chosen_consonants, language_flavour, vowels, consonants)
        starting_with_vowel_syllable = [w for w in syllable.split() if w[0] in vowels]
        vowel_syllables += starting_with_vowel_syllable
        starting_with_consonant_syllable = [w for w in syllable.split() if w[0] not in vowels]
        consonant_syllables += starting_with_consonant_syllable
    return vowel_syllables, consonant_syllables


def create_simple_word(chosen_vowels, chosen_consonants, language_flavour, vowels, consonants):

    vowel_syllables, consonant_syllables = create_syllable_lists(chosen_vowels, chosen_consonants, language_flavour, vowels, consonants)
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
    word = word.title()
    return word

