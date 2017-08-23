import random
import time
import re

# random.seed(123456782)

class CreateLanguage(object):

    def __init__(self):
        self.character_of_language = self.create_character_of_language()
        vowels, consonants = self.get_letters()
        self.vowels = vowels
        self.consonants = consonants
        self.power_vowels = self.create_power_vowels()
        self.power_consonants = self.create_power_consonants()
        self.power_vowel_starts = self.create_power_vowel_starts()
        self.power_consonant_starts = self.create_power_consonant_starts()
        self.power_consonant_ends = self.create_power_consonant_ends()
        # self.power_vowel_doubles =
        # self.power_consonant_doubles =
        self.syllables = self.create_syllables(length_needed=1)
        # self.syllables_list = self.create_syllable_list()
        self.word_sets = []
        self.english_lang = self.import_english()
        self.dictionary = self.create_dictionary()

    def get_letters(self):
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        return vowels, consonants

    def create_character_of_language(self):
        number_of_power_vowels = random.randint(3, 5)
        number_of_power_consonants = random.randint(3, 10)
        number_of_power_vowel_starts = random.randint(3, 6)
        chance_of_vowel_starts = random.randint(5, 15)
        chance_of_consonant_starts = random.randint(5, 10)
        language_style_random = [number_of_power_vowels,
                                 number_of_power_consonants,
                                 number_of_power_vowel_starts,
                                 chance_of_vowel_starts,
                                 chance_of_consonant_starts,
                                 ["w", "y", "x", "z", 'h', 'q', 'v']
                                 ]
        language_style_simple = [3,
                                 15,
                                 3,
                                 15,
                                 8,
                                 ["w", "y", "x", "z", 'h', 'q', 'v']
                                 ]
        language_style_ri_and_mo = [5,
                                    5,
                                    3,
                                    15,
                                    8,
                                    ["w", "y", "x", "z", 'h'],
                                    "oai",
                                    "mrpgzw"
                                    ]
        language_style_japanese = [ 5,
                                    5,
                                    4,
                                    15,
                                    10,
                                    ["w", "y", "x", "z", 'h'],
                                    "uoia",
                                    "zytkj"
                                    ]
        language_style_nordic =[5,
                                5,
                                3,
                                2,
                                10,
                                ["w", "y", "x", "z", 'h'],
                                "aeio",
                                "flrjk"
                                ]
        language_style_aliens = [5,
                                 5,
                                 3,
                                 2,
                                 10,
                                 ["w", "y", "x", "z", 'h'],
                                 "aeio",
                                 "xzkyv"
                                ]
        language_style_choice = language_style_simple

        print language_style_choice
        return language_style_choice

    def create_power_vowels(self):
        vowels = ["a", "e", "i", "o", "u"]
        power_vowels = ""
        for vowel in xrange(0, self.character_of_language[0]):
            current_vowel = random.choice(vowels)
            while current_vowel in power_vowels:
                current_vowel = random.choice(vowels)
            power_vowels += current_vowel
        if len(self.character_of_language) > 6:
            power_vowels = self.character_of_language[6]
        return power_vowels

    def create_power_consonants(self):
        consonants = ["b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        power_consonants = ""
        for consonant in xrange(0, self.character_of_language[1]):
            current_consonant = random.choice(consonants)
            while current_consonant in power_consonants:
                current_consonant = random.choice(consonants)
            power_consonants += current_consonant
        if len(self.character_of_language) > 6:
            power_consonants = self.character_of_language[7]
        return power_consonants

    def create_power_vowel_starts(self):
        power_vowels = self.power_vowels
        power_vowels_starts = []
        for power_vowels_start in xrange(0, self.character_of_language[2]):
            current_power_vowel_start = random.choice(power_vowels)
            current_power_vowel_start += random.choice(power_vowels)
            while current_power_vowel_start[1] == current_power_vowel_start[0]:
                current_power_vowel_start = current_power_vowel_start[:-1]
                current_power_vowel_start += random.choice(power_vowels)
            while current_power_vowel_start in power_vowels_starts:
                current_power_vowel_start = random.choice(power_vowels)
                current_power_vowel_start += random.choice(power_vowels)
                while current_power_vowel_start[1] == current_power_vowel_start[0]:
                    current_power_vowel_start = current_power_vowel_start[:-1]
                    current_power_vowel_start += random.choice(power_vowels)
            power_vowels_starts.append(current_power_vowel_start)
        return power_vowels_starts

    def create_power_consonant_starts(self):
        # IMPORTS MY LANGUAGE TEXT FILE WHICH CONTAINS A LIST OF FICTIONAL "VERBS"
        power_consonants = self.power_consonants
        possible_power_consonant_starts = []
        with open('power_consonant_starts.txt') as ppcs:
            for line in ppcs:
                possible_power_consonant_starts.append(line.strip())
        possible_power_consonant_starts = possible_power_consonant_starts[:-1]
        power_consonant_starts = []
        for possible_starts in xrange(0, len(possible_power_consonant_starts)):
                if possible_power_consonant_starts[possible_starts][0] in power_consonants and possible_power_consonant_starts[possible_starts][1] in power_consonants:
                    useable_double = possible_power_consonant_starts[possible_starts]
                    power_consonant_starts.append(useable_double)

        return power_consonant_starts

    def create_power_consonant_ends(self):
        # IMPORTS MY LANGUAGE TEXT FILE WHICH CONTAINS A LIST OF FICTIONAL "VERBS"
        power_consonants = self.power_consonants
        possible_power_consonant_ends = []
        with open('power_consonant_ends.txt') as ppce:
            for line in ppce:
                possible_power_consonant_ends.append(line.strip())
        # possible_power_consonant_ends = possible_power_consonant_ends[:-2]
        print possible_power_consonant_ends
        power_consonant_ends = []
        for possible_ends in xrange(0, len(possible_power_consonant_ends)):
                if possible_power_consonant_ends[possible_ends][0] in power_consonants and possible_power_consonant_ends[possible_ends][1] in power_consonants:
                    useable_double = possible_power_consonant_ends[possible_ends]
                    power_consonant_ends.append(useable_double)

        return power_consonant_ends

    def create_syllables(self, length_needed):

        # Create First Letter
        power_vowels = self.power_vowels
        power_consonants = self.power_consonants
        power_vowel_starts = self.power_vowel_starts
        power_consonant_starts = self.power_consonant_starts
        letters = ['Vow', "Con"]

        syllable_length = length_needed
        syllable = ""
        previous_letter_type = random.choice(letters)

        for syllables in xrange(0, syllable_length):
            if previous_letter_type == "Con":  # create vowel, next time consonant
                if random.randint(1, 15) >= self.character_of_language[3]:
                    if len(power_vowel_starts) != 0:
                        current_letter = random.choice(power_vowel_starts)
                    else:
                        current_letter = random.choice(self.vowels)
                else:
                    current_letter = random.choice(power_vowels)
                syllable += current_letter
                previous_letter_type = 'Vow'
            else:
                if random.randint(1, 10) >= self.character_of_language[4]:
                    # one in ten starter letters are power_consonant_starts
                    if len(power_consonant_starts) != 0 and syllables == 0:  # must exist and be first letter
                        current_letter = random.choice(power_consonant_starts)
                    else:
                        current_letter = random.choice(self.consonants)
                else:
                    current_letter = random.choice(power_consonants)
                syllable += current_letter
                if random.randint(1, 10) >= self.character_of_language[4] and syllables > 0 and current_letter not in self.character_of_language[5]:
                    syllable += current_letter
                previous_letter_type = "Con"
        if previous_letter_type == "Con":
            syllable += random.choice(power_vowels)
        else:
            if random.randint(1, 10) >= self.character_of_language[4] and len(self.power_consonant_ends) > 0:
                syllable += random.choice(self.power_consonant_ends)
            else:
                syllable += random.choice(power_consonants)
        return syllable

    def import_english(self):
        english_words = []
        with open('english_words.txt') as english_lang:
            for line in english_lang:
                english_words.append(line.strip())
        return english_words

    def create_dictionary(self):
        already_known_alien_words = []
        with open('learned_alien_words.txt') as alien_lang:
            for line in alien_lang:
                already_known_alien_words.append(line.strip())

        translation = []
        english_words = self.english_lang
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for eng_word in english_words:
            length_of_word = len(eng_word)
            if eng_word in numbers:
                alien_word = eng_word
            elif length_of_word == 1:

                alien_word = random.choice(self.power_vowels)
            else:
                alien_word = self.create_syllables(length_of_word-1)
            while alien_word in translation:
                if length_of_word == 1:
                    alien_word = random.choice(self.power_vowels) + random.choice(self.consonants)
                else:
                    alien_word = self.create_syllables(length_of_word+1)
            translation.append(alien_word)
        with open('learned_alien_words.txt', 'r+') as alien_lang:
            for word in xrange(0, len(translation)):
                if word != 0:
                    alien_lang.write("\n")
                alien_lang.write(translation[word])
        return translation

    def translate_something(self):
        words_to_translate = []
        translation = []
        english_words = self.english_lang
        word_to_translate_string = ''
        not_wanted_list = ['.', ',', ';', ':', '!', '?', '`', '"', "'", '(', ')', '/']
        with open('translate_me.txt') as english_lang:
            for line in english_lang:
                for word in line.split():
                    if word == '':
                        break
                    lower_word = word.lower()

                    words_to_translate.append(lower_word)
                    word_to_translate_string += word+' '

        for word_to_translate in words_to_translate:
            for cleanups in not_wanted_list:
                word_to_translate = word_to_translate.replace(cleanups, '')
                word_to_translate = re.sub('-', '', word_to_translate)
                word_to_translate = re.sub('_', '', word_to_translate)
            if word_to_translate in english_words:
                for word_can_translate in xrange(0, len(english_words)):
                    if word_to_translate == english_words[word_can_translate]:
                        if len(self.dictionary) > 0:
                            translation.append(self.dictionary[word_can_translate])
            else:
                clean_word_eng = word_to_translate.lower()
                for cleanups in not_wanted_list:
                    clean_word_eng.replace(cleanups, '')
                if clean_word_eng != '':
                    with open('english_words.txt', "a") as english_lang:
                        english_lang.write(clean_word_eng)
                        english_lang.write("\n")
                    translation.append(clean_word_eng)
                    english_words.append(clean_word_eng)

        translation_conc = ''
        for translated_words in translation:
            translation_conc += translated_words+' '

        print translation
        print words_to_translate

        print word_to_translate_string
        print translation_conc




language = CreateLanguage()
words_sets = language.word_sets
language.translate_something()
print 'Power Vowels', language.power_vowels
print 'Power Consonants', language.power_consonants
print 'Power Vowel Starts', language.power_vowel_starts
print 'Power_consonant_Starts', language.power_consonant_starts
print "Power_consonant_ends", language.power_consonant_ends
# print language.syllables_list[0]
# print language.syllables_list[1]
# print language.syllables_list[2]
# print language.syllables_list[3]
# print language.word_sets
print language.english_lang
print language.dictionary

# paragraph = ''
# for lots in xrange(0, 10):
#     paragraph = ''
#     word_set = random.choice(words_sets)
#     random_syllable_set = random.choice(language.syllables_list)
#     paragraph += "The Village of "
#     paragraph += random.choice(word_set)+' '
#     paragraph += "lies in the valley of "
#     paragraph += random.choice(random_syllable_set)+random.choice(random_syllable_set)+" "
#     time.sleep(1)
#     print paragraph
#
# for many in xrange(0, 50):
#     sentence = ''
#     for words in xrange(0, 10):
#         word_set = random.choice(words_sets)
#         random_syllable_set = random.choice(language.syllables_list)
#         if random.randint(1, 2) == 1:
#             sentence += random.choice(word_set) + ' '
#         else:
#             sentence += random.choice(random_syllable_set) + ' '
#         if random.randint(1, 8) >= 8:
#             sentence += random.choice(language.power_vowels) + ' '
#         time.sleep(0.2)
#     sentence = sentence[:-1]
#     if random.randint(1, 2) == 1:
#         sentence += ','
#     else:
#         sentence += '.'
#     print sentence
#     time.sleep(1)

