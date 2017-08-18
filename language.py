import random

vowels = "a","e","i","o","u"
consonants = ["b",'c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def choose_power_consonants():

    power_consonants = ""
    previous_consonant = ""
    for consonant in xrange(0, 5):
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


def create_syllables():

    letters_in_word = random.randint(2, 4)
    word = ""
    previous_letter = "Con"

    for letters in xrange(0, letters_in_word):
        if len(word) == 0:
            if random.randint(1, 2) == 1:
                first_letter = random.choice(chosen_consonants)
                word += first_letter
                previous_letter = "Con"
            else:
                first_letter = random.choice(chosen_vowels)
                word += first_letter
                previous_letter = "Vow"
        if previous_letter == "Vow":
            first_letter = random.choice(chosen_consonants)
            word += first_letter
            previous_letter = "Con"
        else:
            first_letter = random.choice(chosen_vowels)
            word += first_letter
            previous_letter = "Vow"
    return word

y = ""
for amount in xrange(0, 30):
    x = create_syllables()
    y += x+" "

print y
